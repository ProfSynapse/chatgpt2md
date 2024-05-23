# ChatGPT to MD

Hey there! 👋 Welcome to the ChatGPT Conversation Exporter! This nifty Python script helps you filter and export your ChatGPT conversations to markdown files, making it a breeze to organize and search through your chats. 🔍📝

## What does it do? 🤔

This script takes a JSON file containing all your ChatGPT conversations and lets you:
- Filter conversations based on a search term (can be anything, like an emoji or a keyword)
- Export the filtered conversations to individual markdown files
- Add custom tags to the exported files for easy categorization
- Save the markdown files to a directory of your choice

Pretty cool, right? 😎

## How to use it 🛠️

Using this script is super easy! Just follow these steps:

1. Make sure you have Python installed on your machine. If you don't, head over to the [Python website](https://www.python.org/downloads/) and grab the latest version.

2. Download the `chatgpt_exporter.py` script from this repo and save it somewhere on your computer.

3. Open your terminal or command prompt and navigate to the directory where you saved the script.

4. Run the script by typing `python chatgpt_exporter.py` and hit Enter.

5. The script will prompt you for some info:
   - The path to your `conversations.json` file (this is the file containing all your ChatGPT conversations)
   - The output directory where you want to save the exported markdown files (default is `obsidian_import`)
   - Any tags you want to add to the exported files, separated by commas (default is `chatgpt`)
   - The search term you want to use to filter your conversations

6. Sit back and let the script work its magic! ✨ It'll filter your conversations and export the matching ones to markdown files in the output directory you specified.

7. Once the script is done, you'll find your exported conversations in the output directory, ready to be imported into your favorite note-taking app or shared with the world! 🌍

## Troubleshooting 🚧

If something goes wrong, don't panic! The script logs any errors to a file called `conversion.log` in the same directory. Check this file for clues on what might have gone wrong.

If you're still stuck, feel free to open an issue on this repo, and we'll do our best to help you out! 💪

## Happy exporting! 🎉

That's it! You're now ready to filter and export your ChatGPT conversations like a pro. Happy organizing and searching! 🗂️🔎
