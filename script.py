import subprocess
import time
import os
import random

def generate_text(size_chars=1000):
    return ''.join(random.choices('01\n', k=size_chars))

def send_imessage(to_contact, message):
    """Send an iMessage using AppleScript to a contact or phone number."""
    service_type = "iMessage"
    
    script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type is {service_type}
        set targetBuddy to buddy "{to_contact}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    
    subprocess.run(['osascript', '-e', script], check=True)

def auto_reply():
    """Automatically reply to iMessages."""
    chat_name = str(input("TYPE IMESSAGE ACCOUNT OF THE PHISHER (EITHER EMAIL OR NUMBER): "))
    
    responses = [
        "You're wasting your time here!",
        "Nice try, but I'm not falling for it!",
        "Is this the best you can do?",
        "Try harder next time!"
    ]
    
    while True:
        text = generate_text()
        reply_message = f"{random.choice(responses)}\nSYSTEM RESPONSE: ACCESS DENIED! PHISHING DETECTED!\n{text}"
        
        try:
            send_imessage(chat_name, reply_message)
        except subprocess.CalledProcessError as e:
            print(f"Failed to send message: {e}")
        
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    auto_reply()
