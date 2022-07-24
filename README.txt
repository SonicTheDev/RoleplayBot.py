CUSTOM ROLEPLAY DISCORD BOT.PY
in discord.py (python)

This source code is for you to be able to create your own custom Roleplay discord.py bot for your RP server/Channel.
DISCLAIMER: This works better if you have one channel for RP cause webhooks are involved.

========================================================================================================

REQUIREMENTS
- discord.py (Do "py -3 -m pip install -U discord.py" to install discord.py on your device - Don't include the "")
- Knowledge of discord.py and python
- A discord bot application created with a bot token copied.

========================================================================================================

SETUP
1. Download or Fork this source code.
2. Create your Discord bot application and copy your token (if you have not already done so)
3. At client.run("YOURBOTTOKEN") (at the bottom), replace YOURBOTTOKEN with your own Discord bot token.
4. At client = commands.Bot(command_prefix = '!'), replace ! with the prefix you want to use.
5. At @client.command() async def commandnamehere(ctx, *, question):, here is some things to do:
- Replace commandnamehere with the command name you want to use to execute the command.
- Replace YOURSERVERID with the Server ID you want to use the bot in.
- Replace WEBHOOK TOKEN HERE with your Webhook url
- Replace WEBHOOK NAME HERE with the name of the webhook
- Replace WEBHOOKPFPURL with the url for the pfp of the webhook.
6. For more characters, copy and paste the command where @client.command() async def commandnamehere(ctx, *, question): is and repeat step 6 for additional RP characters.
7. Run the Bot.

========================================================================================================

LICENSE: We are using the MIT license so you can pretty much do whatever you want with it.