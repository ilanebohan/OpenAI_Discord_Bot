from cmath import log
import discord
from discord.ext import commands
import OpenAI

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("The bot is ready!")

@client.command()
async def hello(ctx): # Send "Hi" message to the channel (Usable by anyone) -> Respond to !hello command    
    await ctx.send("Hi")

@client.command()
@commands.is_owner()
async def log(ctx): # Send the logs to the channel (Only used by the bot owner) -> Respond to !log command
    f = open("log_user.txt", "r")
    for line in f:
        await ctx.send(line)
    f.close()

@client.command()
@commands.is_owner()
async def count_request(ctx): # Send the number of requests logged in (Only used by the bot owner) -> Respond to !count_request command
    i = 0
    f = open("log_user.txt", "r")
    for line in f:
        i += 1
    f.close()
    await ctx.send(f"{i} requests sent during this session") 

@client.command()
@commands.is_owner()
async def shutdown(context): # Shutdown the bot (Only used by the bot owner) -> Respond to !shutdown command
    exit()
    
    
def send_author_and_content_to_logs(Content): # Send the author and content of the message to the logs
    list_user.append(Content) # Append the user ID, user and message to list_user
    f = open("log_user.txt", "w") # Open the file to write the logs
    for it in list_user: 
        f.write("%s\n" % it) # Write the list_user to the log_user.txt file
    f.close()

responses = 0
list_user = []

@client.event
async def on_message(message): # Event triggered when a message is sent in the channel
    # If the message is not from the bot (else the bot is responding to himself) 
    # and is in the bot channel (can be optimized using channel ID : message.channel.id == <CHANNELID>)
    # and if the message is not a command -> not starting with "!" (Overriding the default provided on_message forbids any extra commands from running.)
    if message.author != client.user and message.channel.name == "bot" and message.content.startswith("!") == False: 
        chat_log = ""
        question = message.content
        answer = OpenAI.askQuestion(question, chat_log) # Ask the question and get the answer by OpenAI
        chat_log = OpenAI.append_interaction_to_chat_log(question, answer,chat_log) # Append the question and answer to the chat log
        await message.channel.send(answer)
        send_author_and_content_to_logs(str(message.author.id) + 'User : ' + str(message.author) + 'Message : ' + str(message.content))
    if message.content.startswith("!") == True: # If the message is a command
        await client.process_commands(message) # Process the command


client.run("Your Discord Key") # Bot token
