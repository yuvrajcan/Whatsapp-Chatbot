# WhatsApp Auto-Reply Chatbot

This WhatsApp chatbot automatically reads incoming messages and responds using OpenAI's GPT-4 model. It extracts messages, processes them, and replies in Hindi based on the context of the conversation.

## Features
- **Automated Message Reply**: Reads new messages and responds automatically.
- **Multi-Language Support**: Replies in Hindi while analyzing messages in English and Hindi.
- **AI-Powered Responses**: Uses GPT-4 to generate contextual replies.

## Prerequisites
Ensure you have Python installed (Python 3.7 or later).

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies using pip:
   ```bash
   pip install pyautogui clipboard openai
   ```

## Required Libraries/Modules
- `pyautogui`: Automates GUI interactions.
- `time`: Manages execution delays.
- `clipboard`: Handles copy-paste functionality.
- `openai`: Integrates with OpenAI's GPT model.

## Setup
1. Replace `sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your **OpenAI API** key.
2. Open WhatsApp Web on your computer.
3. Ensure the script's cursor positions match your screen layout. You may need to adjust the x, y coordinates for clicking and dragging text.

## Usage
1. Run the script:
   ```bash
   python whatsapp_bot.py
   ```
2. The bot will continuously monitor incoming messages and respond automatically.

## Error Handling
- If messages are not being copied correctly, verify the cursor positions.
- Ensure WhatsApp Web is open and active.
- If responses are incorrect, check API key validity and internet connection.

## Future Enhancements
- Improve cursor position detection dynamically.
- Add logging for message history.
- Support more languages and context-based replies.

## License
This project is open-source and free to use. Feel free to modify and enhance it!

