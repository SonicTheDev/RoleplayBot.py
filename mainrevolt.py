import voltage
from voltage.ext import commands
import random
import json
import asyncio
import aiohttp

client = commands.CommandsClient("!")

@client.listen("ready")
async def ready():
    print("Roleplay Revolt Bot Running")

@client.command(description="Masquerade")
async def commandnamehere(ctx, *, message):
    await ctx.send(f'{message}', masquerade=voltage.MessageMasquerade(name="WEBHOOKNAMEHERE", avatar="WEBHOOKPFPURL"))
    await ctx.message.delete()

@client.command(description="Make the bot say your message")
async def say(ctx, *, question):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@client.command(description="Make the bot say your message in an embed")
async def esay(ctx, *, question):
    embed = voltage.SendableEmbed(description=f'{question}', color='#00FF4F')
    await ctx.send(embed=embed)
    await ctx.message.delete()



client.run("YOURBOTTOKEN")
