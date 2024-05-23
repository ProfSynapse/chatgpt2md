import json
import os
import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.ERROR, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_input(prompt, default=None):
    value = input(prompt)
    if not value and default is not None:
        return default
    return value

def main():
    setup_logging('conversion.log')

    try:
        json_file = get_user_input("Enter the path to the conversations.json file: ")
        output_dir = get_user_input("Enter the output directory for markdown files (default: 'obsidian_import'): ", default='obsidian_import')
        tags_input = get_user_input("Enter tags separated by commas (default: 'chatgpt'): ", default='chatgpt')
        tags = [tag.strip() for tag in tags_input.split(',')]
        search_term = get_user_input("Enter the search term to filter conversations by: ")

        with open(json_file, 'r') as f:
            data = json.load(f)

        os.makedirs(output_dir, exist_ok=True)

        for convo in data:
            if any(search_term in msg['content'] for msg in convo['message']):
                filename = f"{convo['id']}.md"
                with open(os.path.join(output_dir, filename), 'w') as f:
                    f.write(f"---\ntitle: {convo['title']}\ndate: {convo['create_time']}\ntags:\n")
                    for tag in tags:
                        f.write(f"- {tag}\n")
                    f.write("---\n\n")
                    for msg in convo['message']:
                        f.write(f"*{msg['role']}*: {msg['content']}\n\n")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
    except KeyError as e:
        logging.error(f"Missing key in JSON: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
