# Developed with love by spy404
# ------ libs ------ #
import os
import discord
import pwinput
from discord.ext import commands
from discord.embeds import Embed
from pystyle import Center
from colorama import Fore, init

# ------ setup ------ #
init()
if os.name == "nt":
    os.system("title Unban all - spy404#6985")
os.system("cls" if os.name == "nt" else "clear")
banner = Center.XCenter("""
 ######  ########  ##    ## ##          #####   ##        
##    ## ##     ##  ##  ##  ##    ##   ##   ##  ##    ##  
##       ##     ##   ####   ##    ##  ##     ## ##    ##  
 ######  ########     ##    ##    ##  ##     ## ##    ##  
      ## ##           ##    ######### ##     ## ######### 
##    ## ##           ##          ##   ##   ##        ##  
 ######  ##           ##          ##    #####         ##  
""")
print(Fore.GREEN + banner)

# ------ inputs ------ #
token = pwinput.pwinput(prompt = "token: \n>>> ", mask = "*")

# ------ commands ------ #
client = commands.Bot(command_prefix = "spy!", intents = discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")

@commands.has_permissions(ban_members=True) 
@client.command()
async def unban(ctx):
    counter = 0
    banned = ctx.guild.bans()
    async for users in banned:
        user = users.user
        try:
            await ctx.guild.unban(user)
            print(Fore.GRENN + f"Unbanned user: {user}")
        except:
            print(Fore.RED + f"Can't Unbanned user: {user}")
        counter += 1
    await ctx.channel.send(f"Unbanned {counter} members")

client.run(token)