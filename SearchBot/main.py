import discord
from discord.ext import commands
from discord_slash import SlashCommand
from search import searchGoogle

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@slash.slash(name="search", description="Search Google using SerpAPI")
async def search_command(ctx, query: str):
    search_results = await searchGoogle(query)
    await ctx.send(content=f"Search results for '{query}':\n{search_results}")

if __name__ == "__main__":
    from config import TOKEN
    bot.run(TOKEN)