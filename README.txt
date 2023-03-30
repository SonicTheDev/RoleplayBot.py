CUSTOM ROLEPLAY DISCORD BOT.PY
in discord.py (python)

This source code is for you to be able to create your own custom Roleplay discord.py bot for your RP server/Channel.
In Discord.py 2.0 and has been made better.

DISCLAIMER: This works better if you have one channel for RP cause webhooks are involved.

========================================================================================================

SETUP
1. Download or Fork this source code and Create your Discord bot application at discord.com/developers
- Make sure to copy your bot token. You will need this.
- Make sure Message Content intent is enabled as well.
2. At client.run("YOURBOTTOKEN") which is located at the bottom, replace YOURBOTTOKEN with your own Discord bot token.
3. At client = commands.Bot(command_prefix = '!'), replace ! with the prefix you want to use.
4. At @client.command() async def commandnamehere(ctx, *, question):, here is some things to do:
- Replace commandnamehere with the command name you want to use to execute the command.
- Replace YOURSERVERID with the Server ID you want to use the bot in.
- Replace WEBHOOKTOKENHERE with your Webhook url
- Replace WEBHOOKNAMEHERE with the name of the webhook
- Replace WEBHOOKPFPURL with the url for the pfp of the webhook.
5. For more characters, copy and paste the command where @client.command() async def commandnamehere(ctx, *, question): is and repeat step 6 for additional RP characters.
6. Run the Bot.

========================================================================================================

NOTICE: Older Commits for Discord.py may no longer work as older commits uses discord.py 1.7.x which may be deprecated.

========================================================================================================

LICENSE: We are using the MIT license so you can pretty much do whatever you want with it.