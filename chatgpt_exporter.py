import json
import os
import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_input(prompt, default=None):
    value = input(prompt)
    if not value and default is not None:
        return default
    return value

def get_valid_filename(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\n']
    filename = ''.join(c if c not in invalid_chars else '_' for c in title)
    return filename[:100]  # Limit filename length to 100 characters

def get_message_content(message):
    try:
        content = message['content']
        if isinstance(content, dict):
            if 'parts' in content:
                return content['parts'][0]
            elif 'text' in content:
                return content['text']
            elif 'result' in content:
                return content['result']
            else:
                # Handle unexpected structures by converting the whole content dictionary to a string
                logging.warning(f"Unexpected content structure: {content}")
                return json.dumps(content, indent=2)
        elif isinstance(content, str):
            return content
        else:
            logging.warning(f"Unexpected content structure: {content}")
            return ''
    except (KeyError, IndexError) as e:
        logging.warning(f"Error accessing message content: {e}")
        return ''

def main():
    setup_logging()

    try:
        json_file = get_user_input("Enter the path to the conversations.json file: ")
        output_dir = get_user_input("Enter the output directory for markdown files (default: 'obsidian_import'): ", default='obsidian_import')
        tags_input = get_user_input("Enter tags separated by commas (default: 'chatgpt'): ", default='chatgpt')
        tags = [tag.strip() for tag in tags_input.split(',')]
        search_term = get_user_input("Enter the search term to filter conversations by: ")

        logging.info(f"Input file: {json_file}")
        logging.info(f"Output directory: {output_dir}")
        logging.info(f"Tags: {tags}")
        logging.info(f"Search term: {search_term}")

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        os.makedirs(output_dir, exist_ok=True)

        exported_count = 0
        for convo in data:
            try:
                valid_messages = [msg for msg in convo['mapping'].values() if msg.get('message') is not None]
                if any(search_term in get_message_content(msg['message']) for msg in valid_messages):
                    title = get_valid_filename(convo['title'])
                    filename = f"{title}.md"
                    file_path = os.path.join(output_dir, filename)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        create_date = datetime.fromtimestamp(convo['create_time']).strftime('%Y-%m-%d')
                        f.write(f"---\ntitle: {convo['title']}\ndate: {create_date}\ntags:\n")
                        for tag in tags:
                            f.write(f"- {tag}\n")
                        f.write("---\n\n")

                        for msg in valid_messages:
                            role = msg['message']['author'].get('role', 'unknown')
                            content = get_message_content(msg['message'])
                            if content:  # Only write non-empty content
                                f.write(f"*{role}*: {content}\n\n")

                    exported_count += 1
                    logging.info(f"Exported conversation: {file_path}")
            except (KeyError, IndexError) as e:
                logging.error(f"Error processing conversation: {e}")
                logging.error(f"Conversation ID: {convo.get('id', 'Unknown')}")

        logging.info(f"Exported {exported_count} conversations.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
