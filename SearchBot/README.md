# SearchBot

SearchBot is a Discord bot that allows users to search Google using the `/search` command. The bot uses SerpAPI to fetch search results and returns them in a JSON format.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/SearchBot.git
```

2. Change to the project directory:

```
cd SearchBot
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Discord bot token and SerpAPI key:

```
DISCORD_TOKEN=your_discord_bot_token
SERPAPI_KEY=your_serpapi_key
```

## Usage

1. Run the bot:

```
python main.py
```

2. Invite the bot to your Discord server.

3. Use the `/search` command followed by your search query:

```
/search your_search_query
```

The bot will return the search results in a JSON format.

## UI (Optional)

If you want to use the optional UI with Tailwind CSS, follow these steps:

1. Install Tailwind CSS and its dependencies:

```
npm install
```

2. Build the CSS file:

```
npx tailwindcss build src/styles.css -o templates/styles.css
```

3. Open `templates/index.html` in your browser to view the UI.