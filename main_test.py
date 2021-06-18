from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Le bot est prêt")


@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()


bot.run("ODUwMzc0OTYzODE0NDY1NTM2.YLozZg.AuUy_j7naDumjcLP2Kt4lDjb7Z8")
