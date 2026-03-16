# FAQ Bot Miami

An AI-powered FAQ chatbot for local businesses in Miami — built with Python and OpenAI API.

## What it does

Businesses in Miami receive dozens of messages every day asking the same questions — hours, pricing, services, availability. This bot answers them automatically, 24/7, in English and Spanish.

## Features

- Answers frequently asked questions instantly
- Supports both English and Spanish
- Customizable for any local business (dental clinics, restaurants, salons, etc.)
- Runs continuously until stopped
- Secure API key management with .env

## Built with

- Python 3
- OpenAI API (GPT-4o-mini)
- python-dotenv

## Setup
```bash
git clone https://github.com/Ruisanchezjavier/faq-bot-miami
cd faq-bot-miami
python3 -m venv env
source env/bin/activate
pip install openai python-dotenv
```

Add your OpenAI API key to a `.env` file:
```
OPENAI_API_KEY=your_key_here
```

Run the bot:
```bash
python3 bot.py
```

## Author

Javier Ruisanchez — Full Stack Developer · Miami, FL  
[LinkedIn](https://linkedin.com/in/javier-ruisanchez) · [GitHub](https://github.com/Ruisanchezjavier)
