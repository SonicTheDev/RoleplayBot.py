import discord
from discord.ext
from discord import Webhook, RequestsWebhookAdapter
import random
import sys

client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Roleplay Bot Running")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="HELP MENU", description="Here is my List of Commands", color=(64255))
    embed.add_field(name="MAIN", value="!help - This message\n!ping - Checks the latency of the bot\n!say - Make me say anything\n!esay - Make me say anything in an embed", inline=False)
    embed.add_field(name="UTILITIES", value="!restart - Restarts the Bot", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("What do you want me to say?")
    else:
        raise error

@client.command()
async def esay(ctx, *, question):
    embed = discord.Embed(description=f'{question}', color=(65535))
    await ctx.send(embed=embed)
    await ctx.message.delete()

@esay.error
async def esay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("What do you want me to say?")
    else:
        raise error




@client.command()
async def commandnamehere(ctx, *, question):
    async with aiohttp.ClientSession() as session:
        if ctx.guild.id == YOURSERVERID:
            webhook = Webhook.from_url('WEBHOOKTOKENHERE', adapter=AsyncWebhookAdapter(session))
            await webhook.send(content=f'{question}', username="WEBHOOKNAMEHERE", avatar_url="WEBHOOKPFPURL")
            await ctx.message.delete()
        else:
            await ctx.send("This command can only be used in Sonics Bot Hub Discord Server")
            return





client.run("YOURBOTTOKEN")
