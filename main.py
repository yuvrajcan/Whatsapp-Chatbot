import pyautogui
import time
import clipboard
from openai import OpenAI

client = OpenAI(
    api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)


def wait_for_response(previous_text):
    """Waits until a new response is detected in the chat before proceeding."""
    while True:
        time.sleep(2)  # Check every 2 seconds
        pyautogui.click(491, 163)  # Click to focus on chat box
        pyautogui.hotkey('ctrl', 'c')  # Copy latest message
        selected_text = clipboard.paste().strip()  # Remove unnecessary spaces
        
        # If the copied text is new and non-empty, return it
        if selected_text and selected_text != previous_text:
            return selected_text


# Add a small delay before starting to ensure you have time to switch to the target window
time.sleep(2)

# Click the icon
pyautogui.click(x=170, y=746)

previous_text = ""

while True:
    # **Wait for a response before proceeding**
    selected_text = wait_for_response(previous_text)
    previous_text = selected_text  # Update previous_text to avoid duplicates

    print("Selected text:", selected_text)

    # Move to start position of text selection
    pyautogui.moveTo(478, 153)

    # Click and hold to start dragging
    pyautogui.mouseDown()

    # Drag to end position
    pyautogui.dragTo(1309, 654, duration=1)

    # Release mouse button
    pyautogui.mouseUp()

    # Copy selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(491, 163)

    print("Selected text:", selected_text)  # Debugging output

    # Generate response using GPT-4
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "system", "content": "You are a person named Yuvraj who speaks English as well as Hindi. You are a coder. You analyze the chat and give the response in Hindi according to the context of the chat. Generate small responses."},
            {"role": "user", "content": selected_text}
        ]
    )

    response = completion.choices[0].message.content

    # Copy the response to clipboard
    clipboard.copy(response)

    # Click at the specified position and paste
    pyautogui.click(602, 697)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
