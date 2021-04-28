import discord
from discord.embeds import Embed
from discord.ext import commands
from requests import __title__

from actions import search, download
import Keys

client = commands.Bot(command_prefix='!')


@client.command(name='status')
async def status(context):
    await context.message.channel.send('AnimeXplorer is online Now :P')


@client.command(name='version')
async def version_info(context):
    myEmbed = discord.Embed(
        title='Current Version', description='This bot is currentlty version 1.0', color=0xBA55D3)
    myEmbed.add_field(name='Version Code : ', value='v1.0.0', inline=False)
    myEmbed.add_field(name='Date Released : ',
                      value='28 Apr 2021', inline=False)

    await context.message.channel.send(embed=myEmbed)


@client.command(name='search')
async def search_cmd(cxt, *arg):
    query = ' '.join(arg)
    res = search(query)
    if(len(res)>0):
        embdMssg = discord.Embed(title='Found '+str(len(res))+' results:', color=0x58d68d)
        for item in res:
            embdMssg.add_field(name=item['title']+' : ',value='V_ID : '+item['vid_id']+', DATE : '+item['date'],inline=False) 

        await cxt.message.channel.send(embed=embdMssg)
    else:
        await cxt.message.channel.send()


@client.command(name='download')
async def download_cmd(cxt, arg):
    res = download(arg)
    data = res['data'][0]
    cover = res['episode'][0]['cover']
    embdMssg = discord.Embed(
        title=data['title2'], description=data['description'], color=0x00ffff)
    embdMssg.set_image(url=cover)
    embdMssg.add_field(name='Stream Link :', value=data['stream'])
    embdMssg.add_field(name='Download Link :', value=data['download'])
    embdMssg.set_footer(text='Download Id :'+data['download_id'])


    await cxt.message.channel.send(embed=embdMssg)

client.run(Keys.BOT)
