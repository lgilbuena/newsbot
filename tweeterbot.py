import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import worker
import main

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

news_channel_id = None
started = False
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))
    

@bot.event
async def on_message(message):
    global started
    if message.author.bot:
        return
    await bot.process_commands(message)

    if worker.get_data(1):
        if len(worker.get_data(0)) == 0:
            channel = bot.get_channel(worker.get_data(1))
            if channel:
                await channel.send('You must add news queries for the bot to be fully functioning using the command "!addq *insert query here*" ')
        elif not started:
            started = True
            test_drive.start()
        
            
@bot.command()
async def setchannel(ctx):
    global news_channel_id
    if worker.get_data(1):
        ctx.send("You already have a news channel set.")
        return 
    else:
        worker.modify_data(1,ctx.channel.id)
        await ctx.send("This channel has been set to send new information")
        

@bot.command()
async def addq(ctx, *args):
    query = ' '.join(args)
    worker.modify_data(0,query)
    await ctx.send('Added query!')

@bot.command()
async def getq(ctx):
    await ctx.send(worker.get_data(0))

@tasks.loop(hours=24)
async def test_drive():
    if worker.get_data(1) and len(worker.get_data(0)) > 0:
            channel = bot.get_channel(worker.get_data(1))
            if channel:
                 await channel.send(main.get_news())
bot.run(TOKEN)