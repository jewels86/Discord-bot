import discord
from discord.ext import commands
from commands import tasks
import os

# Hardcoded bot token (use with caution)
TOKEN = os.environ["HACKLY_BOT_TOKEN"]

# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    try:
        await tasks.init(bot=bot)  # Initialize tasks
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="hello", description="Replies with Hello, World!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, World!")

@bot.tree.command(name="goodnight", description="Have sweet dreams!")
async def goodnight(interaction: discord.Interaction):
    await interaction.response.send_message("GOOD NIGHT! HAVE LOTS OF SWEET DREAMS AND SLEEP TIGHT! BEEP BOOP!")

bot.run(TOKEN)
