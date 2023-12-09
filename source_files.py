import requests 
import string 
from bs4 import BeautifulSoup
import wolframalpha
import json
from googlesearch import search
import http.client
from datetime import datetime

def url_maker(input_text):
    # Function to generate a Wikipedia URL based on the input text
    x = string.capwords(input_text)
    lists = x.split()
    search_term = "_".join(lists)
    url = f"https://en.wikipedia.org/wiki/{search_term}"
    return url

def wikibot(url):
    # Function to extract information from Wikipedia page
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    
    info_list = []  # To store the extracted information
    
    infobox = soup.find('table', {'class': 'infobox'})
    if infobox:
        rows = infobox.find_all('tr')
        for row in rows:
            heading = row.find('th')
            detail = row.find('td')
            if heading and detail:
                info_list.append("{}   ::   {}".format(heading.text, detail.text))
                info_list.append("---------------------")

    paragraphs = soup.find_all('p')
    for i in range(1, min(2, len(paragraphs))):  # Limit to at most 2 paragraphs
        info_list.append(paragraphs[i].text)
    
    # Join the list elements into a single string using newlines
    return '\n'.join(info_list)

def get_latest_match_results():
    # Function to get the latest football match results
    url = 'https://api.football-data.org/v2/matches'
    headers = {'X-Auth-Token': "Your api key "}

    response = requests.get(url, headers=headers)
    data = response.json()
    matches = data.get("matches",[])
    home = []
    away  = []

    for match in matches:
        hometeam = match.get("homeTeam","N/A")
        hometeam = hometeam.get("name","N/A")
        awayteam = match.get("awayTeam","N/A")
        awayteam = awayteam.get("name","N/A")
        home.append(hometeam)
        away.append(awayteam)
    results = []
    for i, j in zip(home, away):
        results.append(f"{i} -----VS----- {j}")
    formatted = "\n".join(results)
    return formatted

def search_google(query):
    # Function to perform a Google search and return results
    google_results = []

    for result in search(query, num_results=5):  # Search and get top 5 results
        google_results.append(result)

    formatted_results = "\n\n".join(google_results)
    return "Google Search Results:\n" + formatted_results

def wolfbot(query):
    # Function to interact with Wolfram Alpha API
    api_key = "Your api key"
    url = f"http://api.wolframalpha.com/v1/conversation.jsp?appid={api_key}&i={query}"
    results = requests.get(url)
    data = results.text
    response_json = json.loads(data)
    show = response_json.get("result")
    return show

def get_upcoming_fixtures(team_name):
    # Function to get upcoming football fixtures for a given team
    team_name_to_id = {
    "manchester united": 33,
    "newcastle": 34,
    "bournemouth": 35,
    "fulham": 36,
    "huddersfield": 37,
    "watford": 38,
    "wolves": 39,
    "liverpool": 40,
    "southampton": 41,
    "arsenal": 42,
    "burnley": 44,
    "everton": 45,
    "leicester": 46,
    "tottenham": 47,
    "west ham": 48,
    "chelsea": 49,
    "manchester city": 50,
    "brighton": 51,
    "crystal palace": 52,
    "barcelona": 529,
    "atletico madrid": 530,
    "athletic club": 531,
    "valencia": 532,
    "villarreal": 533,
    "las palmas": 534,
    "malaga": 535,
    "sevilla": 536,
    "leganes": 537,
    "real sociedad": 548,
    "kerala blasters": 3477,
    "ajax": 194,
    #Add more team mappings here 
    }

    if team_name.lower() not in team_name_to_id:
        return "Sorry, I don't have upcoming fixtures information for that team."
    
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    team_id = team_name_to_id[team_name.lower()]

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "Your api key"
    }

    conn.request("GET", f"/fixtures?team={team_id}&status=NS&next=5", headers=headers)
    
    res = conn.getresponse()
    data = res.read()

    response_json = json.loads(data.decode("utf-8"))

    formatted_upcoming_fixtures = ""
    for fixture in response_json['response']:
        event_date = datetime.strptime(fixture['fixture']['date'], "%Y-%m-%dT%H:%M:%S%z")
        formatted_date = event_date.strftime("%Y-%m-%d %H:%M:%S")

        home_team = fixture['teams']['home']['name']
        away_team = fixture['teams']['away']['name']

        formatted_upcoming_fixtures += f"Date: {formatted_date}\n"
        formatted_upcoming_fixtures += f"Match: {home_team} vs {away_team}\n"
        formatted_upcoming_fixtures += "--------------------------\n"

    return formatted_upcoming_fixtures

def liveresults():
    # Function to get live football match results
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "Your api key"
    }

    conn.request("GET", "/fixtures?live=all", headers=headers)

    res = conn.getresponse()
    data = res.read()

    response_json = json.loads(data.decode("utf-8"))

    formatted_output = ""
    for fixture in response_json['response']:
        home_team = fixture['teams']['home']['name']
        away_team = fixture['teams']['away']['name']
        score = f"{fixture['goals']['home']} - {fixture['goals']['away']}"
        status = fixture['fixture']['status']['short']
    
        formatted_output += f"Match: {home_team} vs {away_team}\n"
        formatted_output += f"Score: {score}\n"
        formatted_output += f"Status: {status}\n"
        formatted_output += "--------------------------\n"
    
    return formatted_output

def get_insult():
    # Function to get a random insult
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    response = requests.get(url)
    data = response.json()
    insult = data.get("insult")
    return insult


