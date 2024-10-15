# Description of Counter Phishing Annoyance Script for imessages

This Python script is designed to automatically send rapid, automated responses to phishers targeting you via iMessage account. Utilizing the `subprocess` module to execute AppleScript commands, the script effectively interacts with the Messages app on macOS to deliver messages to the specified contact.

## Key Features:

### Random Message Generation:
The function `generate_text(size_chars=1000)` creates a string of random binary characters (0s and 1s), simulating a flood of nonsensical data. This adds to the confusion and frustration for the phishing attacker.

### iMessage Integration:
The `send_imessage(to_contact, message)` function utilizes AppleScript to send an iMessage to the specified contact. This method ensures that the messages are sent seamlessly from your iMessage account.

### Automated Replies:
The `auto_reply()` function prompts the user to input the iMessage account of the suspected phisher (either an email address or a phone number). It then enters an infinite loop where it continuously sends a predefined, aggressive response, combined with randomly generated text. The response reads:

This message is intended to be disruptive and to signal to the phisher that their attempts are being recognized and thwarted.

### Rapid Messaging:
The script includes a short delay of 0.1 seconds between messages to ensure a steady stream of responses without overwhelming the system.

## Purpose:
The main aim of this script is to serve as a deterrent against phishing attempts by engaging in disruptive communication. By sending an automated barrage of responses, the script not only annoys the phisher but also highlights the vigilance of the user against phishing attacks.

## Disclaimer:
This script is intended for educational and ethical use only. Sending unsolicited messages may violate terms of service or local laws. Use responsibly and only with the intention of protecting against phishing attempts.
