
import discord
from discord import Embed
from discord import embeds
from discord import channel
from discord import colour
from discord.ext import commands
from discord.ext.commands import command
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands import Cog
from discord.player import AudioPlayer
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.chrome import service
import urllib3
import re
import random
import datetime
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup, element
from datetime import date, datetime
from logging import PlaceHolder
from typing import Container, Optional, Text
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotInteractableException, JavascriptException, NoSuchElementException   
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager     


options = Options()
options.headless = True


s = False

client = commands.Bot(command_prefix=".",case_insensitive=True)
request = ""
url = "https://www.flightsimaddons.net/search?q="
url1 = ""
state = False
#respone = urllib.request.urlopen(url1)
#soup = BeautifulSoup(respone,'html.parser')






@client.event
async def on_ready():
    print("bot is ready")






@commands.cooldown(1,10,BucketType.user)








@client.command()
async def request(ctx,*,arg):
    await ctx.send("Passing ur request"+ ' ' + arg + ' ' + "standby")
    if arg.isupper():
        arg = arg.casefold()
    print(arg)
    author = ctx.author
    url1 = url + arg
    url_full = url1.replace(" ", "%20")
    web_r = uReq(url_full)
    s = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=s,options=options)
    driver.get(url_full)
    page_soup = soup(web_r,"lxml")
    html = driver.execute_script("return document.documentElement.outerHTML")
    html_page_soup = soup(html,"lxml")   



    links_table = []   
    for ul in html_page_soup.find_all("div",{"archive-page-content widget-content"}):
        for li in ul.find_all('a'):
           links_table.append(li['href'])


    full_link = []

    for path in links_table:
        if arg in path:
            full_link.append(path)
    try:
        element = full_link[0]
    except:
        element = links_table[0]
        

    
    print(element)

  

    if element == '/' or '':
        await ctx.send(f'{author.mention} :x: I cant find this on FSA!')
        await logs(author,arg,datetime.utcnow(),"Error")
    else:
        embed = discord.Embed(title="Request(click here)",url=element,description="Ur request")
        await author.send(embed=embed)
        await ctx.send(f'{author.mention} :white_check_mark: Link was sent to dm')
        await logs(author,arg,datetime.utcnow(),"Succes")
        links_table.clear()
        s = False
    



async def logs(author,request,when,state):
    channel = client.get_channel(873019204603891783)
    await channel.send(f'User: {author}, Request: {request}, Time: {when}, State: {state}')


@client.command()
async def requestUGCX(ctx):
    await ctx.send("Passing ur request")
    author = ctx.author
    try:

       embed = discord.Embed(title="Request(click here)",url="https://www.flightsimaddons.net/2021/12/p3d-fs2crew-all-access-pack.html",description="Ur reqeust")
       await author.send(embed=embed)
       await ctx.send(f':white_check_mark: Link was sent to dm')
    except:
        await ctx.send("problem")

ulr_f1 = "https://www.formula1.com/en/latest.html"
ulr_f1_1 =  "https://www.formula1.com"
articles = []
response = uReq(ulr_f1)
soup1 = soup(response,'lxml')

@client.command()
async def F1News(ctx):
    for a in soup1.find_all('a',attrs={'href': re.compile("/en/latest/article.")}):
        articles.append(a['href'])
    x = random.choice(articles)
    finish_url = ulr_f1_1 + x
    await ctx.send(f' '+finish_url)
    articles.clear()
    return

@client.command()
async def f1champion(ctx):
    with open('worldchampion.jpg','rb') as f:
        picture = discord.File(f)
        await ctx.send(file=discord.File('worldchampion.jpg'))


@client.command()
async def colui(ctx):
    await ctx.send("is retard")


@client.command()
async def fsainv(ctx):
    await ctx.send("https://discord.gg/7kYwGSw832")

@client.command()
async def fslabs(ctx):
    timestamp = datetime.utcnow()
    await ctx.send("FSLabs update in release channel isn't released rn. Status on " ' '+str(timestamp)+' ')
    

        

    

@client.command()
async def requestRutracker(ctx,arg1,*,arg2):

    await ctx.send("Passing ur request"+ ' ' + arg2 + ' ' + "standby")
    author = ctx.author
    request_user = arg2
    request_forum = arg1
    timestamp = datetime.utcnow()
    url4 = ''
    if request_forum == "P3DS":
        url4 = 'https://rutracker.org/forum/viewforum.php?f=2060'
    elif request_forum == "XPS":
        url4 = 'https://rutracker.org/forum/viewforum.php?f=2143'
    elif request_forum == "XPP":
        url4 = 'https://rutracker.org/forum/viewforum.php?f=2012'
    elif request_forum == "P3DP":
        url4 = 'https://rutracker.org/forum/viewforum.php?f=2145'
    url_full = url4.replace(" ", "%20")
    web_r = uReq(url_full)
    driver = webdriver.Firefox()
    driver.get(url4)
    page_soup = soup(web_r,"lxml")
    full_code = []
    html = driver.execute_script("return document.documentElement.outerHTML")
    html_page_soup = soup(html,'lxml')
    links = html_page_soup.find_all('a')
    x=''
    for link in links:
        if link.find(text=re.compile(request_user)):
           x=link.get('href')                
    url3 = 'https://rutracker.org/forum/'

    if x:
             element = url3 + x
             embed = discord.Embed(title="Request(click here)",url=element,description="Ur request")
             await author.send(embed=embed)
             await ctx.send(f':white_check_mark: Link was sent to dm')
             await logs(author,arg2,timestamp,"Succes")
    elif x == '':
             await ctx.send(':x: I cant find this on Rutracker!')
             await logs(author,arg2,timestamp,"Error")


       
          
            
            




    


       
    

   


        


client.run("-")