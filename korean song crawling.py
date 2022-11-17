from selenium import webdriver
import pandas as pd 
import time
#import selenium.webdriver.support.ui as ui
data={
      'year':[],
      'week':[],
      'rank':[],
      'song':[],
      'singer':[],
      #'score':[]
      }

year=[2015,2016,2017,2018]
week=[i for i in range(1,52)]

driver = webdriver.Chrome()
for x in year:  # x 單次年
    for y in week: # 單次週
        #url=getUrl(x,y)
        #2018-16
        driver.get('https://circlechart.kr/page_chart/onoff.circle?nationGbn=T&serviceGbn=ALL&targetTime='+str(y)+'&hitYear='+str(x)+'&termGbn=week&yearTime=3')
        #wait=ui.WebDriverWait(driver, 9)
        if(x >= 2018 and y >= 17): #防止抓不到
            break
        else:
            for i in range(1,101):
                xPath1='//*[@id="pc_chart_tbody"]/tr['+str(i)+']/td[3]/div/section[2]/div/div[1]'
                songName=driver.find_element("xpath",xPath1).text
                xPath2='//*[@id="pc_chart_tbody"]/tr['+str(i)+']/td[3]/div/section[2]/div/div[2]'
                singer=driver.find_element("xpath",xPath2).text
                #xPath3='//*[@id="pc_chart_tbody"]/tr['+str(i)+']/td[4]/span'
                #score=driver.find_element("xpath",xPath3).text
                data['song'].append(songName)
                data['singer'].append(singer)
                #data['score'].append(score)
                data['rank'].append(i)
                data['year'].append(x)
                data['week'].append(y)
                print(x,y,i)
            
driver.close()
df=pd.DataFrame(data)
df.to_excel (r'C:/Users/roy60/Desktop/10_27_Taiwanese popular song data from kkbox/kpopSong2.xlsx', index = False, header=True)
