import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from imgurpython import ImgurClient
from config import *
from utilityFunction import lists
from utilityFunction.CommandFunc import *
from datetime import datetime

imgur = ImgurClient(imgurC, ImgurL)


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["dick", "penis"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dong(self, ctx, *, user: discord.Member):
        """Detects user's dong length"""
        state = random.getstate()
        random.seed(user.id)
        dong = "8{}D".format("=" * random.randint(0, 30))
        random.setstate(state)
        em = discord.Embed(title="{}'s Dong Size".format(user), description="Size: " + dong,
                           colour=discord.Colour.magenta())
        await ctx.send(embed=em)

    @commands.command()
    async def roll(self, ctx, rolls: str):
        """rolls a die"""
        resultString, results, numDice = random.randint(rolls)
        e1 = discord.Embed(title=roll_str(rolls) + f" for %s" % ctx.message.author.name,
                           color=discord.Color.dark_teal())
        await ctx.send(embed=e1)
        if resultString == '20':
            e3 = discord.Embed(title=f":tada:" % + ctx.message.author.mention + f":tada:\n"
                                                                                f"***Critical Success!***\n"
                                                                                f"" + resultString)
            await ctx.send(embed=e3)
        elif resultString == '1':
            e4 = discord.Embed(title=f":roll_of_paper:" % + ctx.message.author.mention + f":roll_of_paper:\n"
                                                                                         f"***Critical Failure!***\n"
                                                                                         f"" + resultString)
            await ctx.send(embed=e4)
        elif numDice == '1':
            await ctx.send(ctx.author.mention + "  :game_die:\n**Result:** " + resultString)
        else:
            e2 = discord.Embed(title=":game_die: Results!",
                               timestamp=datetime.utcnow(),
                               color=discord.Color.magenta(), description=f"Here " + ctx.author.mention +
                                                                          "\n__***All them dice***___\n\n**Result:** "
                                                                          + resultString + "\n**Total:** " + str(
                    results))
            e2.set_thumbnail(url='https://i.imgur.com/fYonsqN.jpg')
            await ctx.send(embed=e2)

    @roll.error
    async def roll_error(self, ctx, error):
        """on error for die"""
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Slow tf down, your dice will be there in a second", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cumscript(self, ctx):
        """transcript of cumzon"""
        cum = open('text_dir/cumscript.txt').read().splitlines()
        await ctx.send(random.choice(cum))
        await ctx.message.delete()

    @cumscript.error
    async def cumscript_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Really? Is this song that appealing to you?", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def img_src(self, ctx, *text: str):
        """Allows the user to search for an image from imgur"""
        rand = random.randint(0, 29)
        if text == ():
            await ctx.send('**Please enter a search term**')
        elif text[0] != ():
            items = imgur.gallery_search(" ".join(text[0:len(text)]), advanced=None, sort='rising', window='all',
                                         page=0)
            await ctx.send(items[rand].link)
            await ctx.message.delete()

    @img_src.error
    async def img_src_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="You literally can just go to imgur", color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def cat(self, ctx):
        await ctx.send("Enjoy a random cat!")
        source = requests.get('http://theoldreader.com/kittens/600/400/js').text
        soup = BeautifulSoup(source, 'html.parser')
        img = soup.find('img')
        rcurl = "http://theoldreader.com" + str(img['src'])
        e = discord.Embed()
        e.color = discord.Color.magenta()
        e.set_image(url=rcurl)
        await ctx.send(embed=e)
        await ctx.message.delete()

    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dog(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/gallery/vgW1p/images?client_id={imgurC}").json()
        em = discord.Embed(title="The goodest of bois")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @dog.error
    async def dog_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def birb(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/gallery/QWmIV/images?client_id={imgurC}").json()
        em = discord.Embed(title="birb")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @birb.error
    async def birb_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def otter(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/gallery/BZA8d/images?client_id={imgurC}").json()
        em = discord.Embed(title="Otters :D")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @otter.error
    async def otter_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def plat(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/album/kWZ6JNv/images?client_id={imgurC}").json()
        em = discord.Embed(title="Platypussssss!!!!!! :D")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @plat.error
    async def plat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bun(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/gallery/FQsx8/images?client_id={imgurC}").json()
        em = discord.Embed(title="buns :D")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @bun.error
    async def bun_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def insult(self, ctx):
        """random insult"""
        lines = open('text_dir/insults.txt').read().splitlines()
        await ctx.send(random.choice(lines))
        await ctx.message.delete()

    @insult.error
    async def insult_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="<:3463_pepeone:708017294097383484>  Error!",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)

    @commands.command()
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @commands.command()
    async def guess(self, ctx):
        num = random.randint(0, 100)
        for i in range(0, 5):
            await ctx.send('guess')
            response = await self.wait_for('self')
            guess = int(response.content)
            if guess > num:
                await ctx.send('bigger')
            elif guess < num:
                await ctx.send('smaller')
            else:
                await ctx.send('you got it!')

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def daddy(self, ctx):
        author = ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dadjoke-api.herokuapp.com/api/v1/dadjoke") as r:
                data = await r.json()
                d = discord.Embed(title=f":milk: Hey, I found the milk", description=data['joke'],
                                  color=discord.Color.magenta()
                                  , timestamp=datetime.utcnow())
                await ctx.send(embed=d)

    @daddy.error
    async def daddy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Dad jokes are temporary, just like your actual dad",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(FunCog(bot))
