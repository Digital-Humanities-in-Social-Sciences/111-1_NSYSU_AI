import datetime
startDate = "20141227"
endDate = "20221101"
startDate = datetime.datetime.strptime(startDate, '%Y%m%d')
endDate = datetime.datetime.strptime(endDate, '%Y%m%d')
days = (endDate - startDate).days + 1

dates = [] 
count=1

for dayNum in range(days):
    # 從起始日開始依次
    date = (startDate + datetime.timedelta(days=dayNum))
    count+=1
    if(count>=7):
        dates.append(date.strftime('%Y%m%d'))
        count=1

import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

tw='297'

#year=list(range(2015,2023))
#month=list(range(1,13))

thisYearMonth={
    "year":2022,
    "month":11,
    "day":1
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
    for i in range(49):
        allData['date'].append(data['data']['date'])
        allData['rank'].append(data['data']['charts']['newrelease'][i]['rankings']['this_period'])
        allData['artist'].append(data['data']['charts']['newrelease'][i]['artist_name'])
        allData['songName'].append(data['data']['charts']['newrelease'][i]['song_name'])
        allData['songUrl'].append(data['data']['charts']['newrelease'][i]['song_url'])
        allData['lyric'].append(getLyric(data['data']['charts']['newrelease'][i]['song_url']))
        print(data['data']['date'],data['data']['charts']['newrelease'][i]['rankings']['this_period'])
    return 0


def urlDate(year,month,day,cat):
    return 'https://kma.kkbox.com/charts/api/v1/daily?category='+cat+'&date='+year+'-'+month+'-'+day+'&lang=tc&limit=50&terr=tw&type=newrelease'

for i in dates:
    url=urlDate(i[0:4], i[4:6], i[6:8],tw)
    check50data(url)
    print(i,"done")
df=pd.DataFrame(allData)
df.to_excel (r'C:/Users/roy60/Desktop/10_27_Taiwanese popular song data from kkbox/tpopSong.xlsx', index = False, header=True)


#for i in year:
#    for j in month:
#        if(int(i)>=int(thisYearMonth['year']) and int(j) >int(thisYearMonth['month'])):
#            break
#        else:
#            i=str(i)
#            j=str(j)
#            url=urlDate(i,j,tw)
#            check50data(url)



