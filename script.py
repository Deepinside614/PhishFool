import subprocess
import time
import os
import random

def generate_text(size_chars = 1000):
    return ''.join(random.choices('01\n', k=size_chars))

def send_imessage(to_contact, message):
    """Send an iMessage using AppleScript to a contact or phone number."""
    service_type = "iMessage"

    script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type is {service_type}
        set targetBuddy to buddy "{to_contact}" of targetService
        send "{message}" to targetBuddy
    '''

    script += "end tell"
    
    subprocess.run(['osascript', '-e', script], check=True)

def auto_reply():
    """Automatically reply to iMessages."""
    chat_name=str(input("TYPE IMESSAGE ACCOUNT OF THE PHISHER (EITHER EMAIL OR NUMBER):"))
    while True:
        text=generate_text()
        reply_message = f"THIS IS AN AUTOMATED RESPONSE F**K U.\nSYSTEM RESPONSE: ACCESS DENIED! PHISHING DETECTED. YOU CAN'T HACK ME!\n{text}"
        send_imessage(chat_name, reply_message)

        time.sleep(0.1)

if __name__ == "__main__":
    auto_reply()
