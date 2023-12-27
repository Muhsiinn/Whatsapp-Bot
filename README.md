# WhatsApp Bot

This project implements a WhatsApp chatbot using Flask and Twilio, providing various commands and functionalities.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- [ngrok](https://ngrok.com/) (for local development and testing)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Muhsiinn/whatsapp-bot.git
   cd whatsapp-bot

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

### Configuration
Update the configuration in config.py with your Twilio credentials and any other necessary settings.

### Running The Application 

1. Start ngrok to expose your local Flask app to the internet:
   
   ```bash 
   ngrok http 5000

2. Update your Twilio WhatsApp number's messaging webhook URL to the ngrok URL:

   ```bash
   https://your-ngrok-url.ngrok.io/bot

3. Run The Flask app :
   
   ```bash
   python main.py

Your WhatsApp chatbot is now running and accessible through the configured ngrok URL.

Usage
Send a message to your Twilio WhatsApp number.

Use the following commands:

1. wiki <query>: Search Wikipedia for the given query.
2. hello: Greet the chatbot.
3. upcoming <team>: Get upcoming fixtures for a specific team.
4. live football: Get live football results.
5. search <query>: Perform a Google search.
6. wolfbot <command>: Execute a command using the Wolfbot.
## Feel free to customize the commands and functionalities based on your requirements.

This is an old fun project that i modified lately, and I encourage you to feel free to modify, improve, and build upon it. Whether you want to add new features, fix bugs, or simply experiment with the code, your contributions are highly appreciated.
