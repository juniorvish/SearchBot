import discord
from discord.ext import commands
from search import searchGoogle

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.command(name="search")
async def search_command(ctx, *, search_query: str):
    search_results = searchGoogle(search_query)
    await ctx.send(embed=search_results)

def run_bot(token):
    bot.run(token)

if __name__ == "__main__":
    from config import DISCORD_TOKEN
    run_bot(DISCORD_TOKEN)