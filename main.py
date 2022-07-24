import discord
from discord.ext
from discord import Webhook, RequestsWebhookAdapter
import random

client = commands.Bot(command_prefix = '!')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Roleplay Bot Running")

@client.command()
async def help(ctx):
    await ctx.send("!help\n!ping\n!say")

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()



@client.command()
async def commandnamehere(ctx, *, question):
    async with aiohttp.ClientSession() as session:
        if ctx.guild.id == YOURSERVERID:
            webhook = Webhook.from_url('WEBHOOK TOKEN HERE', adapter=AsyncWebhookAdapter(session))
            await webhook.send(content=f'{question}', username="WEBHOOK NAME HERE", avatar_url="WEBHOOKPFPURL")
            await ctx.message.delete()
        else:
            await ctx.send("This command can only be used in Sonics Bot Hub Discord Server")
            return



client.run("YOURBOTTOKEN")
