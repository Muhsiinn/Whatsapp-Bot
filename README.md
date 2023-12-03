# WhatsApp Chatbot with Flask

## Overview

This is a simple Flask application that functions as a WhatsApp chatbot. The bot can perform various tasks, including searching Wikipedia, providing football match results, generating Google search results, interacting with Wolfram Alpha API, and more.

## Prerequisites

- Python 3.x
- Flask
- Twilio
- Beautiful Soup
- Wolfram Alpha API Key
- Football Data API Key
- Twilio Account SID and Auth Token

## Installation

1. Install the required Python libraries:

   ```bash
   pip install flask twilio beautifulsoup4 requests wolframalpha googlesearch-python
Obtain API keys:

Wolfram Alpha API Key: https://products.wolframalpha.com/api/
Football Data API Key: https://www.football-data.org/
Twilio Account SID and Auth Token: Twilio.com
Replace the placeholder API keys and Twilio credentials in the app.py file with your actual keys.

Usage
Run the Flask application:

bash
Copy code
python app.py
Expose the application to the internet using tools like Ngrok.

Configure Twilio to send incoming WhatsApp messages to the publicly accessible URL provided by Ngrok.

Send WhatsApp messages to interact with the chatbot.

Features
Wikipedia Search: Start a message with a dot (.) followed by the search query to get information from Wikipedia.

Introduction: Send "hello" to receive an introduction message.

Upcoming Fixtures: Include the word "upcoming" in your message followed by a football team's name to get upcoming fixtures.

Football Results: Send a message starting with "football" to get live football match results.

Google Search: Start a message with "google" followed by the search query to get Google search results.

Wolfram Alpha Interaction: Start a message with a plus sign (+) followed by a query to interact with Wolfram Alpha.

Customization
Add more friend names and funny comments to the friend_comments dictionary in the bot function.
Disclaimer
This chatbot script is provided as-is. Use it responsibly and ensure compliance with Twilio's usage policies.


Feel free to modify the content based on your specific needs and provide additional information if necessary.

