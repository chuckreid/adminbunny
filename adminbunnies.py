import os, discord, random, traceback, datetime
from discord.ext import commands
from dotenv import load_dotenv

fusilli = 0
cookie = 0

# Loading Discord token and guild IDs from an external resource
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents)

# Anything within this event will run whenever the bot initially logs into guild
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    

# Anything within this event will run whenever there is a new member to the guild
@client.event
async def on_member_join(member):
    try:
        welcome_messages = [
            f'COOKIE: Welcome, {member.mention}! ...do you have any carrots?',
            f'FUSILLI: Welcome, {member.mention}! ...got any carrots?',
            'COOKIE: Hey, a new friend! *binkies*',
        ]
    # Print exception to console
    except Exception as e:
        print(e)

# Anthing within this event will run whenever a message is sent in the chat channel
@client.event
async def on_message(message):
    global fusilli
    global cookie
    try:
        # A growing collection of facts about my two bunnies
        pellet_messages = [
            'COOKIE FACT:\nCookie joined the Reid family in November 2022, exactly 1 year after Fusilli.',
            'COOKIE FACT:\nCookie is Fusilli\'s half-sister.  They have different father bunnies.',
            'COOKIE FACT:\nCookie\'s name was originally \'Miss Piggy\'.\nWe didn\'t want to fat shame our bunny.',
            'COOKIE FACT:\nCookie is not too fond of physical human contact. \nHowever, it is possible to get her in your arms for a snuggle.',
            'COOKIE FACT:\nCookie\'s birthday is in May.',
            'COOKIE FACT:\nCookie was named by Elizabeth. The color of her fur reminded Elizabeth of a cookie.',
            'FUSILLI FACT:\nChuck regularly calls Fusilli by the nickname, \'Fus\'.  This is because Fusilli is very bold in everything he does,\nlike an unrelenting force...',
            'FUSILLI FACT:\nMost bunnies like fruits and veggies. Fusilli eats pizza and chips.',
            'FUSILLI FACT:\nFusilli\'s astrological sign is Leo. This makes sense because Fusilli loves to bask in the spotlight and celebrate...himself!',
            'FUSILLI FACT:\nFusilli has a lynx coloured fur, and it\'s SUPER soft!',
            'FUSILLI FACT:\nIt took almost a year of being bonded that Fusilli finally groomed Cookie.\nMeanwhile, Cookie is always taking care of Fusilli.',
            'FUSILLI FACT:\nFusilli has never been picked up. IT IS FORBIDDEN.'
        ]
        # A growing collection of bunny responses to receiving a carrot from a member in chat; chosen at random
        carrot_messages = [
            'COOKIE: Can I have a carrot?',
            'COOKIE: I wish I had a carrot...',
            'COOKIE: Somebody say carrot? Yes, please!',
            'COOKIE: "C" is for cookie...and carrot!',
            'COOKIE: "What are the chances that your carrot is for me?'
            'FUSILLI: Can I have a carrot?',
            'FUSILLI: I wish I had a carrot...',
            'FUSILLI: Hey, Cookie! There are carrots over here!'
        ]
        # A growing collection of bunny actions to occur; chosen at random 
        lettuce_messages = [
            '*Cookie just did a little binky!*',
            '*Fusilli just did a little binky!*',
            '*Cookie just did a huge binky!*',
            '*Fusilli just did a huge binky!*',
            '*Cookie is doing zoomies around the chat room!*',
            '*Fusilli is doing zoomies around the chat room!*',
            '*Cookie is napping...*',
            '*Fusilli is napping...*'
        ]
        # Check if message in chat was sent by the bot before continuing; Avoids infinite loops
        if message.author == client.user:
            return
        else:
            if '🥕' in message.content and 'fusilli' in message.content.lower():
                response = random.choice(carrot_messages)
                await message.channel.send(response)
                # await message.channel.send("*Cookie is eating a carrot*")
                await message.channel.send("*Fusilli is eating a carrot*")
                fusilli += 1
                return
            
            if '🥕' in message.content and 'cookie' in message.content.lower():
                response = random.choice(carrot_messages)
                await message.channel.send(response)
                await message.channel.send("*Cookie is eating a carrot*")
                # await message.channel.send("*Fusilli is eating a carrot*")
                cookie += 1
                return
            
            # Bunnies do an action if LETTUCE is mentioned in chat
            if 'lettuce' in message.content.lower() or '🥬' in message.content:
                response2 = random.choice(lettuce_messages)
                await message.channel.send(response2)
                return
        
            # Learn a bunny fact about COOKIE or FUSILLI
            if '!bunnyfact' in message.content.lower():
                response3 = random.choice(pellet_messages)
                await message.channel.send(response3)
                return
            
            if '!carrotcount' in message.content.lower():
                curr_date = datetime.datetime.now()
                form_date = curr_date.strftime("%B %d %Y %H:%M:%S")
                message1 = '-------- TOTAL CARROT SCOREBOARD --------'
                message2 = f'As of {form_date}'
                message3 = f'Total carrots given to Fusilli: {fusilli}'
                message4 = f'Total carrots given to Cookie : {cookie}'
                await message.channel.send(message1)
                await message.channel.send(message2)
                await message.channel.send(message3)
                await message.channel.send(message4)
                return


    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

client.run(TOKEN)
