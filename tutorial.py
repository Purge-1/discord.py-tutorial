#                         -----------------------------------------
#
#                                          discord.py Tutorial
#                          -----------------------------------------
#
#                 This is Under MIT License If you remove credits you will be sued by me.
#
#
#                             You will Learn how to make discord bots easily
#
#
#
#                                         Project by Purge#0005
#
#
#
#
#
import discord
from discord.ext import commands

token = 'your token here :D'

client = commands.Bot(command_prefix="*") #prefix is fully your choice.
client.remove_command('help') # Removing the help command to make a custom one.

client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"*help")) #Make your status (ANY)

@client.command()
async def help(ctx):
  embed = discord.Embed(title = "Help Center", description = "All commands of this bot is displayed here!")
  embed.add_field(name = "*hello", value = "Greet the bot.")
  embed.add_field(name = "*embed", value = "Example Embed.") #Setup the name and the value for each command
  await ctx.send(embed=embed)

# With the other commands you can go update it.

@client.command()
async def hello(ctx):
	await ctx.author.send('Hello There :wave:')
	# Simple Sending the bot a message to your dms. If you want it to send it in a channel just remove author and do await ctx.send('Message')

# Starting with embeds now

@client.command()
async def embed(ctx):
	embed = discord.Embed(title = "Example", description = "Type your description.")
	embed.add_field(name="Example", value = "Type your value.")
	embed.add_field(name= "Example", value = "Type your value.")
	embed.add_field(name= "Example", value = "Type your value.") #You can add alot of fields this is just an example
	await ctx.send(embed=embed)

# Reaction Sending 
# Make the bot send a reation when you do a command.
@client.command()
async def reaction(ctx):
	await ctx.send("I will put a reaction")
	await ctx.message.add_reaction("✅")

client.run(token)