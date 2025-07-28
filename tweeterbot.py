import discord
from discord.ext import commands, tasks

news_channel_id = None

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))
    

@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    if message.author.bot:
        return
    await bot.process_commands(message)
@bot.command()
async def setchannel(ctx):
    global news_channel_id
    if news_channel_id:
        ctx.send("You already have a news channel set.")
        return 
    else:
        news_channel_id = ctx.channel.id
        await ctx.send("This channel has been set to send new information")
        test_drive.start()


@tasks.loop(days=1)
async def test_drive():
    if news_channel_id:
            channel = bot.get_channel(news_channel_id)
            if channel:
                 await channel.send('bellow!')

bot.run(TOKEN)