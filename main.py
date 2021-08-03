import os
import discord
from discord import Message
from discord.client import Client
from discord.ext.commands import has_permissions, MissingPermissions, errors
from discord.ext import commands, tasks
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!!',  intents=intents)

@client.command(pass_context = True)
async def dm(ctx, *, args=None):
  if args!= None:
    members = ctx.guild.members
    for member in members:
        try:
          await member.send(args)
        except:
            print ('didnt work')


client.run(os.getenv('TOKEN'))