# Whatsapp-Bot
 
# Python Script Documentation

## Description
This Python script includes functions for various purposes such as searching Wikipedia, retrieving football match results, performing Google searches, interacting with Wolfram Alpha API, and more.

## Requirements
- Python 3.x
- Required Python libraries: `requests`, `string`, `BeautifulSoup`, `wolframalpha`, `json`, `googlesearch-python`, `http.client`

## Setup
1. Install the required Python libraries:
   ```bash
   pip install requests
   pip install beautifulsoup4
   pip install wolframalpha
   pip install google
2. Obtain API keys:
   Wolfram Alpha API Key: https://products.wolframalpha.com/api/
   Football Data API Key: https://www.football-data.org/

Functions
url_maker(input_text)
Generates a Wikipedia URL based on the input text.

wikibot(url)
Extracts information from a Wikipedia page.

get_latest_match_results()
Gets the latest football match results using the Football Data API.

search_google(query)
Performs a Google search and returns the top 5 results.

wolfbot(query)
Interacts with the Wolfram Alpha API.

get_upcoming_fixtures(team_name)
Gets upcoming football fixtures for a given team using the Football Data API.

liveresults()
Gets live football match results using the Football Data API.

get_insult()
Gets a random insult from evilinsult.com.

Notes
Ensure that you have the necessary API keys for the Wolfram Alpha API, Football Data API, and RapidAPI.
Disclaimer
This script is provided as-is. Use it responsibly and ensure compliance with API usage policies.