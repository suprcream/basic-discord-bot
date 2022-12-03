import random
import discord
import settings
from discord.ext import commands

def main():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        print(f"User : {bot.user}")
        print(f"ID : {bot.user.id}")
        channel = bot.get_channel(961700835472056350)
        await channel.send(f"{bot.user} is ready!!!")

    @bot.command(
        aliases=["Ping","p"],
        brief="Respon pong",
        description="I will respon Pong",
        hidden=True
    )
    async def ping(ctx):
        await ctx.send("pong")
    
    # user input command
    # @bot.command()
    # async def say(ctx, word):
    #     await ctx.send(word)
    
    # @bot.command()
    # async def say2(ctx, *sentence):
    #     await ctx.send(" ".join(sentence))
    
    @bot.command()
    async def choose(ctx, *options):
        choice = random.choice(options)
        await ctx.send(choice)
    
    # error handling
    @bot.command()
    async def say(ctx, *,sentence = None):
        if sentence == None:
            await ctx.send("What should I say??😾")
        else:
            await ctx.send(sentence)
    
    @bot.command()
    async def say2(ctx, *,sentence = None):
        if sentence == None:
            await ctx.send("What should I say??😾")
        else:
            await ctx.send(sentence)
    
    @say2.error
    async def say2_error(ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("What should I say??😾")

    #embed
    @bot.command()
    async def embed(ctx):
        member = ctx.author
        Color = member.color
        embed = discord.Embed(
            title=f"{member.name}",
            description="this is desc",
            color= Color,
            url="https://twitter.com/suprcream_",
        )
        embed.set_thumbnail(url=f'{member.avatar}')
        embed.set_author(
            name=f'{member.name}',
            icon_url=f'{member.avatar}',
            url="https://twitter.com/suprcream_"
            )
        embed.set_image(url=f'https://pbs.twimg.com/profile_banners/1273652946153005057/1614152020/1080x360')
        embed.add_field(
            name="Field1",
            value=f'{member.id}',
            inline=False
        )
        embed.add_field(
            name="Joined at",
            value=f'{member.joined_at}',
            inline=True
        )
        embed.add_field(
            name="Created at",
            value=f'{member.created_at}',
            inline=True
        )
        embed.set_footer(text="this is footer")
        await ctx.send(embed=embed)
    

    bot.run(settings.TOKEN)

if __name__ == "__main__":
    main()