import hikari
from config import *

bot = hikari.GatewayBot(token=TOKEN, intents=hikari.Intents.ALL)

@bot.listen(hikari.GuildMessageCreateEvent)
async def foo(event: hikari.GuildMessageCreateEvent) -> None:
    if event.content.lower() == 'Foo':
        await event.message.respond(content='Bar')



def main():
    bot.run()

if __name__ == '__main__':
  main()
