import discord
import os
import asyncio
from discord.ext import tasks, commands
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix="!", intents=intents)

@tasks.loop(seconds=60) # 60 վայրկյանը բավարար է, քանի որ ստուգում ենք ժամը և րոպեն
async def scheduled_message():
    now = datetime.now()
    
    # weekday() - երկուշաբթին 0 է, կիրակին՝ 6
    # Ստուգում ենք՝ արդյոք երկուշաբթի է (0), ժամը 10 է, և րոպեն 00 է
    if now.weekday() == 0 and now.hour == 10 and now.minute == 0:
        channel = client.get_channel(1526230179792424970)
        if channel:
            await channel.send("<@&1526224777457565727> այսօր Ձեր 2 շաբաթյա թարմացման օրն է, խնդրում ենք ուշադրություն դարձնել որպեսզի թարմացման կետերը չգերազանցեն 5-ը՝ ներառելով հետագայի անելիքները, ձախողումները կամ կախումները։")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    if not scheduled_message.is_running():
        scheduled_message.start()

token = os.getenv('DISCORD_TOKEN')
client.run(token)