import discord
from discord.ext import commands
import random
import time
import re
import asyncio
import threading
from threading import Timer

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print('Bot is online')

@bot.command(aliases=['p','pong'])
async def ping(ctx):
    await ctx.send(f':ping_pong: {round(bot.latency * 1000)}ms')

@bot.command(aliases = ['s', 'tempmute', 'tm'])
async def study(ctx, *, timeForMute: str = 'x'):
    guild = ctx.guild
    member = ctx.message.author
    studyRole = discord.utils.get(guild.roles, name="Study")
    role = discord.utils.find(lambda r: r.name == 'Study', ctx.message.guild.roles)
    if timeForMute == "x":
        await ctx.send(f"Please enter the amount of you want to study for with this format `;study 1h`")
    elif role in member.roles:
        await ctx.send(f"You already have the study role")
    else:
        await member.add_roles(studyRole)
        if timeForMute.isdecimal(): 
            print('decimal')
            muteTime = int(timeForMute)
            if (muteTime > 999999999):
                muteTime = 100000000
            await member.send(f"You've set a study timer for {muteTime} seconds")
            await asyncio.sleep(muteTime)
            await member.remove_roles(studyRole)
            await member.send(f"Your study time is up!, time studied for was {muteTime} seconds.")
        else:
            match = re.match(r"([0-9]+)([a-z]+)", timeForMute, re.I)
            if match:
                items = match.groups()
                muteTime = int(items[0])
                if (items[1] == 's'):
                    await member.send(f"You've set a study timer for {muteTime} seconds")
                elif (items[1] == 'm'):
                    await member.send(f"You've set a study timer for {muteTime} minutes")
                    muteTime *= 60
                elif (items[1] == 'h'):
                    await member.send(f"You've set a study timer for {muteTime} hours")
                    muteTime *= 3600
                elif (items[1] == 'd'):
                    await member.send(f"You've set a study timer for {muteTime} days")
                    muteTime *= 3600 * 24
                if (muteTime > 999999999):
                    muteTime = 100000000
                await ctx.send(f"The study role was added to you for {muteTime} seconds")
                await asyncio.sleep(muteTime)
                await member.remove_roles(studyRole)
                await member.send(f"Your study time is up!, time studied for was {muteTime} seconds.")

@bot.command(aliases=['8ball','8b'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
    await ctx.send(f'{random.choice(responses)}')

@bot.command(aliases=['says','saying'])
async def say(ctx, *, question):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{question}')

@bot.command(aliases = ['k', 'kicks'])
async def kick(ctx, member : discord.Member, * , reason=None):
    role = discord.utils.find(lambda r: r.name == 'Moderator', ctx.message.guild.roles)
    if role in member.roles:
        await ctx.send(f"This user is a moderator/admin and cannot be banned")
    elif (not ctx.author.guild_permissions.ban_members):
        await ctx.send(f"This command requires ``Kick Members Permissions``")
    else:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} was kicked')
        await member.send(f'You have been kicked from `{ctx.guild}` for reason: {reason}')

@bot.command(aliases = ['b', 'banhammer'])
async def ban(ctx, member : discord.Member, * , reason=None):
    role = discord.utils.find(lambda r: r.name == 'Moderator', ctx.message.guild.roles)
    if role in member.roles:
        await ctx.send(f"This user is a moderator/admin and cannot be banned")
    elif (not ctx.author.guild_permissions.ban_members):
        await ctx.send(f"This command requires ``Ban Members Permissions``")
    else:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned')

@bot.command(aliases = ['unb', 'forgive'])
async def unban(ctx, member):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send(f"This command requires ``Unban Members Permissions``")
        return
    else:
        bannedUsers = await ctx.guild.bans()
        memberName, memberD = member.split('#')
        for banEntry in bannedUsers:
            user = banEntry.user
            if (user.name, user.discriminator) == (memberName, memberD):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} was unbanned')
                return

@bot.command(aliases = ['m', 'muting'])
async def mute(ctx, member : discord.Member, * , reason=None):
    guild = ctx.guild
    role = discord.utils.find(lambda r: r.name == 'Moderator', ctx.message.guild.roles)
    if role in member.roles:
        await ctx.send(f"This user is a moderator/admin and cannot be muted")
    elif (not ctx.author.guild_permissions.manage_roles):
        await ctx.send(f"You do not have manage roles permissions")
    else:
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        await member.add_roles(mutedRole, reason=reason)
        if (not reason == None):
            await ctx.send(f"{member.mention} was muted for {reason}")
        else:
            await ctx.send(f"{member.mention} was muted (no reason given)")

@bot.command(aliases=['u','unmuting'])
async def unmute(ctx, member : discord.Member, * , reason=None):
    guild = ctx.guild
    role = discord.utils.find(lambda r: r.name == 'Muted', ctx.message.guild.roles)
    if (not ctx.author.guild_permissions.manage_roles):
        await ctx.send(f"This command requires ``Manage Roles Permissions``")
    elif role in member.roles:
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        await member.remove_roles(mutedRole, reason=reason)
        await ctx.send(f"{member.mention} was unmuted")
    else:
        await ctx.send(f"You can only unmute users who are muted")

@bot.command(aliases=['purge', 'delete', 'del', 'd', 'c'])
async def clear(ctx, amount=1):
    if (ctx.author.guild_permissions.manage_messages):
         await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send(f"You do not have the permissions to delete messages")

bot.run('ODMwNDc1OTI5NDQ4MjE4NjU1.YHHO-w.n1FJaVVpInBkCe8WkohCHuzGaKQ')