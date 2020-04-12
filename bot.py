import discord
from discord.ext import commands
import asyncio
import random

TOKEN = 'NjgxOTgwNjc1MzY0MzU2MTQx.XoyTiA.KP7HJMxnaZv0FUmP_gJqMAp9BsM' # Hier kommt dein Token

bot = commands.Bot(command_prefix='!') # Prefix wird nicht gebraucht

@bot.event
async def on_ready():
    print('Rainbow Bot ist bereit!') # Terminal Anzeige 

    try:
        home = bot.get_guild(669959794773458974) # Hier deine Server ID einfügen
        role= home.get_role(698095999348113538) # Hier Rollen ID einfügen (Rainbow Rolle)
        while True:
            color = [0xF4FA58, 0x2EFE2E, 0xFF00BF, 0x00eaff, 0xffc100, 0x070101] # Farben ändern oder neue einsetzen
            r = random.choice(color)
            colors = discord.Color(r)
            await role.edit(colour=colors)
            await asyncio.sleep(9) # Interval ändern / Rainbow-Schnelligkeit einstellen
    except Exception as error:
        print(error)

bot.run(TOKEN)

#                               BLUE Discord: https://discord.gg/germany
#
#                               BLUE YouTube: https://www.youtube.com/bluek1ng
#
# To-Do
# 1. Channel ID einfügen (Zeile 13)
# 2. Emoji einfügen (zeile 14)
# 3. Bot Token einfügen (Zeile 16)
# 4. Bot starten und Spaß haben
# 5. BLUE Server lieben und boosten! xD
#
#
#                               Python benutzen und Bot erstellen? Einleitung dazu findest du hier: https://youtu.be/RYbHpqHCjrY
