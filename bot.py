from cmath import log
import discord
from discord.ext import commands
from requests import request
import OpenAIFILE


intents = discord.Intents().all()
client = commands.Bot(command_prefix="!")

sarcastic_mode = False

@client.event
async def on_ready():
    print("The bot is ready!")

@client.command()
async def hello(ctx): # Send "Hi" message to the channel (Usable by anyone) -> Respond to !hello command    
    await ctx.send("Hi")

@client.command()
async def sqlHelp(ctx): # Send "SQL Help" message to the channel (Usable by anyone) -> Respond to !sqlHelp command
    await ctx.send("Example of text : 'find all users who live in California and have over 1000 credits' -> OpenAI gonna send : 'SELECT * FROM users WHERE state = 'CA' AND credits > 1000'")

@client.command()
async def sqlRequest(ctx): # Send the requested SQL request to the channel (Usable by anyone) -> Respond to !sqlRequest command
    if ctx.message.author != client.user and ctx.message.channel.name == "bot":
        chat_log = ""
        request = ctx.message.content.replace("!sqlRequest ", "")
        answer = OpenAIFILE.create_sql_request(request) # Ask the question and get the answer by OpenAI
        chat_log = OpenAIFILE.append_interaction_to_chat_log(request, answer,chat_log) # Append the question and answer to the chat log
        await ctx.send(answer)
        send_author_and_content_to_logs(str(ctx.message.author.id) + 'User : ' + str(ctx.message.author) + 'Message : ' + str(ctx.message.content))

@client.command()
async def sarcastic_enabled(ctx):
    global sarcastic_mode
    if (sarcastic_mode == False and OpenAIFILE.ai_sarcastic_mode == False):
        sarcastic_mode = True
        OpenAIFILE.ai_sarcastic_mode = True
        await ctx.send("Sarcastic Mode enabled")
    else:
        await ctx.send("Sarcastic Mode already enabled")

@client.command()
async def sarcastic_disabled(ctx):
    global sarcastic_mode
    if (sarcastic_mode == True and OpenAIFILE.ai_sarcastic_mode == True):
        sarcastic_mode = False
        OpenAIFILE.ai_sarcastic_mode = False
        await ctx.send("Sarcastic Mode disabled")
    else:
        await ctx.send("Sarcastic Mode already disabled")

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
        print (sarcastic_mode)
        if (sarcastic_mode == True):
            answer = OpenAIFILE.sarcastic_response(question) # Ask the question and get the answer by OpenAI
        if (sarcastic_mode == False):
            answer = OpenAIFILE.askQuestion(question) # Ask the question and get the answer by OpenAI
        chat_log = OpenAIFILE.append_interaction_to_chat_log(question, answer,chat_log) # Append the question and answer to the chat log
        await message.channel.send(answer)
        send_author_and_content_to_logs(str(message.author.id) + 'User : ' + str(message.author) + 'Message : ' + str(message.content))
    if message.content.startswith("!") == True: # If the message is a command
        await client.process_commands(message) # Process the command


client.run("Your discord key") # Bot token
