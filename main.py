# Common
from io import BytesIO
import aiohttp
import os

# Discord Library
from discord import Embed, File
from discord.ext import commands

# Local
from features.common import get_quote_api, get_covid_api
from features.images import get_image, get_image_nsfw
from features.keep_alive import keep_alive

PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix=PREFIX)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello cái địt mẹ mày.')


"""
Common
"""


@client.command(name='quote')
async def get_quote(ctx):
    quote = get_quote_api()
    await ctx.send(Embed(title=quote))


@client.command(name='covid')
async def covid(ctx):
    data = get_covid_api()
    embed_message = Embed(title="COVID-19", color=0xe74c3c)
    embed_message.add_field(
        name='Thế Giới',
        value='Thông tin về dịch ở ngoài Thế giới.',
        inline=False)
    embed_message.add_field(
        name='Đang điều trị', value=data[0][0], inline=True)
    embed_message.add_field(name='Khỏi', value=data[0][1], inline=True)
    embed_message.add_field(name='Tử vong', value=data[0][2], inline=True)

    embed_message.add_field(
        name='Việt Nam', value='Thông tin về dịch ở Việt Nam.', inline=False)
    embed_message.add_field(
        name='Đang điều trị', value=data[1][0], inline=True)
    embed_message.add_field(name='Khỏi', value=data[1][1], inline=True)
    embed_message.add_field(name='Tử vong', value=data[1][2], inline=True)
    embed_message.set_footer(text="API từ Mạnh Tuấn J2Team")
    await ctx.send(embed=embed_message)


@client.command(name='say')
async def say_name(ctx, arg=None):
    if arg is None:
        await ctx.send("Mày đéo đưa tên thì tao đọc bằng gì???")
    await ctx.send(f'Địt con mẹ mầy, {arg}')


@client.command(name='me')
async def get_info_me(ctx):
    author = ctx.message.author
    _embed = Embed(title=author.name, color=0x3498db)
    _embed.add_field(name='Rank', value='Admin', inline=True)
    _embed.add_field(name='Point', value='99999', inline=True)
    _embed.add_field(name='Cash', value='999999999', inline=False)
    _embed.set_thumbnail(url=author.avatar_url)
    await ctx.send(embed=_embed)


"""
Images
"""


@client.command(name='roses')
async def send_roses_image(ctx):
    image_url = get_image('roses')
    async with aiohttp.ClientSession() as session:
        # note that it is often preferable to create a single session to use multiple times later - see below for this.
        async with session.get(image_url) as resp:
            buffer = BytesIO(await resp.read())
    await ctx.send(file=File(fp=buffer, filename="roses_blackpink.jpg"))


@client.command(name='get')
async def send_img(ctx, arg=None):
    if arg is None:
        await ctx.send("Đmm, thiếu tham số kìa.")
    image_url = get_image(str(arg))
    async with aiohttp.ClientSession() as session:
        # note that it is often preferable to create a single session to use multiple times later - see below for this.
        async with session.get(image_url) as resp:
            buffer = BytesIO(await resp.read())
    await ctx.send(file=File(fp=buffer, filename="something.jpg"))


@client.command(name='meme')
async def send_meme(ctx):
    image_url = get_image('meme')
    async with aiohttp.ClientSession() as session:
        # note that it is often preferable to create a single session to use multiple times later - see below for this.
        async with session.get(image_url) as resp:
            buffer = BytesIO(await resp.read())
    await ctx.send(file=File(fp=buffer, filename="meme.jpg"))


@client.command(name='beauty')
async def send_beauty(ctx):
    image_url = get_image('beauty')
    async with aiohttp.ClientSession() as session:
        # note that it is often preferable to create a single session to use multiple times later - see below for this.
        async with session.get(image_url) as resp:
            buffer = BytesIO(await resp.read())
    await ctx.send(file=File(fp=buffer, filename="beauty.jpg"))


@client.command(name='mlem')
async def send_mlem(ctx):
    image_url = get_image('mlem')
    async with aiohttp.ClientSession() as session:
        # note that it is often preferable to create a single session to use multiple times later - see below for this.
        async with session.get(image_url) as resp:
            buffer = BytesIO(await resp.read())
    await ctx.send(file=File(fp=buffer, filename="mlem.jpg"))


'''
No Safe For Work
'''


@client.command(name='nsfw')
async def send_img_nsfw(ctx, arg=None):
    if arg is None:
        await ctx.send("Đmm, thiếu tham số kìa.")
    image_url = get_image_nsfw(str(arg))
    async with aiohttp.ClientSession() as session:
        # note that it is often preferable to create a single session to use multiple times later - see below for this.
        async with session.get(image_url) as resp:
            buffer = BytesIO(await resp.read())
    await ctx.send(file=File(fp=buffer, filename="nsfw.jpg"))


"""
Games
"""

keep_alive()
client.run(TOKEN)