# File: app.py

import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from source_files import (
    url_maker, wikibot, get_latest_match_results, search_google, wolfbot,
    get_upcoming_fixtures, liveresults, get_insult
)

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming = request.values.get("Body", '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Dictionary mapping friend names to funny comments
    friend_comments = {
        'example': ["comment "],
        # Add more friends and comments here
    }

    # Check for friend names and send funny comments
    for friend_name, funny_comments in friend_comments.items():
        if friend_name in incoming:
            w = get_insult()
            msg.body(w)
            return str(resp)  # Return response and don't proceed to Wikipedia search

    # If no friend name found, proceed with Wikipedia search
    if incoming.startswith('.'):
        query = incoming[1:].strip()
        y = url_maker(query)
        response_text = wikibot(y)
        msg.body(response_text)
    elif incoming.startswith("hello"):
        x = "Hello, I am Lillian Weinberg. Muhsin's assistant 👩🏼"
        msg.body(x)
    elif "upcoming" in incoming:
        # Extract the team name from the user's message
        team_name = incoming.replace("upcoming", "").strip()
        
        # Get the upcoming fixtures for the specified team
        upcoming_fixtures = get_upcoming_fixtures(team_name)
        msg.body(upcoming_fixtures)
    elif incoming.startswith("football"):
        w = liveresults()
        msg.body(w)
    elif incoming.startswith("google"):
        incoming = incoming[6:].strip()
        x = search_google(incoming)
        msg.body(x)
    elif incoming.startswith("+"):
        incoming = incoming[1:].strip()
        x = wolfbot(incoming)
        msg.body(x)
    else:
        msg.body("Sorry the following command is not configured")

    return str(resp)

if __name__ == '__main__':
    app.run()
