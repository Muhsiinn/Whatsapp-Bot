# File: app.py

import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# app.py
from config import Config
from src.source_files import (
    url_maker, wikibot, get_upcoming_fixtures, live_results, search_google, wolfbot,
    get_insult
)

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming = request.values.get("Body", '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Dictionary mapping friend names to professional comments
    friend_comments = {
        'example': ["comment "],
        # Add more friends and comments here
    }

    # Check for friend names and send professional comments
    for friend_name, professional_comments in friend_comments.items():
        if friend_name in incoming:
            insult = get_insult()
            msg.body(insult)
            return str(resp)  # Return response and don't proceed to Wikipedia search

    # If no friend name found, proceed with other commands
    if incoming.startswith("wiki"):
        query = incoming[5:].strip()
        url = url_maker(query)
        response_text = wikibot(url)
        msg.body(response_text)
    elif incoming.startswith("hello"):
        greeting = "Greetings! I am Lillian Weinberg, the virtual assistant for Muhsin. How may I assist you today?"
        msg.body(greeting)
    elif incoming.startswith("upcoming"):
        # Extract the team name from the user's message
        team_name = incoming.replace("upcoming", "").strip()
        
        # Get the upcoming fixtures for the specified team
        upcoming_fixtures = get_upcoming_fixtures(team_name)
        msg.body(upcoming_fixtures)
    elif incoming.startswith("live football"):
        results = live_results()
        msg.body(results)
    elif incoming.startswith("search"):
        search_query = incoming[6:].strip()
        search_result = search_google(search_query)
        msg.body(search_result)
    elif incoming.startswith("wolfbot"):
        wolf_command = incoming[8:].strip()
        wolf_response = wolfbot(wolf_command)
        msg.body(wolf_response)
    else:
        msg.body("I apologize, but the requested command is not recognized. Please try a valid command.")

    return str(resp)

if __name__ == '__main__':
    app.run()
