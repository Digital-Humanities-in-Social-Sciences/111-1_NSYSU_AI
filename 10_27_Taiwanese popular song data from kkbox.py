# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 04:23:47 2022

@author: roy60
"""
#artist=data['data']['charts']['newrelease'][0]['artist_name']
#song_name=data['data']['charts']['newrelease'][0]['song_name']
#rank=data['data']['charts']['newrelease'][0]['rankings']['this_period']
#url=data['data']['charts']['newrelease'][0]['song_url']

import pandas as pd
import requests
import json
import time 
from bs4 import BeautifulSoup
tw='297'
kor='314'

year=list(range(2018,2023))
month=list(range(1,13))

thisYearMonth={
    "year":2022,
    "month":10
    }

allData={
    "date":[],
    "rank":[],
    "artist":[],
    "songName":[],
    "songUrl":[],
    "lyric":[]
    }

def getLyric(LyricUrl):
    if(LyricUrl!='#'):
        song_response=requests.get(LyricUrl)
        soup=BeautifulSoup(song_response.text, "html.parser")
        lyric = soup.find("div", class_="lyrics").text
        return lyric
    else:
        return 'NaN'


def check50data(kkbox_url):
    kkBoxUrl=kkbox_url
    response = requests.get(kkBoxUrl)# 取得歌曲資訊json檔
    data = json.loads(response.text)# 將json字串轉為Python的字典型態
    for i in range(50):
        allData['date'].append(data['data']['date'])
        allData['rank'].append(data['data']['charts']['newrelease'][i]['rankings']['this_period'])
        allData['artist'].append(data['data']['charts']['newrelease'][i]['artist_name'])
        allData['songName'].append(data['data']['charts']['newrelease'][i]['song_name'])
        allData['songUrl'].append(data['data']['charts']['newrelease'][i]['song_url'])
        allData['lyric'].append(getLyric(data['data']['charts']['newrelease'][i]['song_url']))
    return 0


def urlDate(year,month,cat):
    return 'https://kma.kkbox.com/charts/api/v1/daily?category='+cat+'&date='+year+'-'+month+'-1&lang=tc&limit=50&terr=tw&type=newrelease'




for i in year:
    for j in month:
        if(int(i)>=int(thisYearMonth['year']) and int(j) >int(thisYearMonth['month'])):
            break
        else:
            i=str(i)
            j=str(j)
            url=urlDate(i,j,kor)
            check50data(url)
            time.sleep(3)

df=pd.DataFrame(allData)
df.to_excel (r'C:\Users\roy60\Desktop\kkbox\export_dataframe_kr.xlsx', index = False, header=True)
