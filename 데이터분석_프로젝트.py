# -*- coding: utf-8 -*-
"""데이터분석 프로젝트

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HxBw0I76Y4Xeipga9mxlhlk9CJWGXHrA
"""

!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver/usr/bin

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

!pip install webdriver_manager

!pip install chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager
import time
import chromedriver_autoinstaller

options = ChromeOptions()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
options.add_argument('user-agent=' + user_agent)
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options) # <- options로 변경

# import pandas as pd

# df=pd.DataFrame(columns=['이름','출루율','장타율','OPS','삼진'])
# print(df)

from selenium.webdriver.common.keys import Keys
import pandas as pd

# 스탯티즈 접속
driver.get('https://statiz.sporki.com/stats/?m=main&m2=batting&m3=default&so=WAR&ob=DESC&year=2024&sy=&ey=&te=&po=&lt=10100&reg=C100&pe=&ds=&de=&we=&hr=&ha=&ct=&st=&vp=&bo=&pt=&pp=&ii=&vc=&um=&oo=&rr=&sc=&bc=&ba=&li=&as=&ae=&pl=&gc=&lr=&pr=200&ph=&hs=&us=&na=&ls=1&sf1=WAROff&sk1=&sv1=&sf2=WAROff&sk2=&sv2=')


df=pd.DataFrame(columns=['이름','타율','출루율','장타율','ops','삼진','WAR','wRC+'])
a=0

for i in range(3,150):
  obp=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[28]')
  slg=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[28]')
  ops = driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[30]')
  name=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[2]/div/a')
  so=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[23]')
  avg=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[27]')
  war=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[33]')
  wrc=driver.find_element('xpath',f'/html/body/div[2]/div[5]/section/div[8]/table/tbody/tr[{i}]/td[32]')

  df.loc[a]=[name.text,avg.text,obp.text,slg.text,ops.text,so.text,war.text,wrc.text]
  a+=1

print(df.head())
print(df.info())
df.to_csv('kbo스탯.csv',index=False,encoding="utf-8-sig")

# 단계 1: 폰트 설치
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
!apt-get -qq -y install fonts-nanum > /dev/null
#fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'

#font = fm.FontProperties(fname=fontpath, size=9)

#fm._rebuild()



fe = fm.FontEntry(
    fname=r'/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', # ttf 파일이 저장되어 있는 경로
    name='NanumGothic')                        # 이 폰트의 원하는 이름 설정
fm.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 18, 'font.family': 'NanumGothic'}) # 폰트 설

import os
os.kill(os.getpid(), 9)

# 단계 3: 한글 폰트 설정
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

# 마이너스 표시 문제
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 설정
fe = fm.FontEntry(
    fname=r'/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', # ttf 파일이 저장되어 있는 경로
    name='NanumGothic')                        # 이 폰트의 원하는 이름 설정
fm.fontManager.ttflist.insert(0, fe)              # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 18, 'font.family': 'NanumGothic'}) # 폰트 설

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import plotly.express as px

df=pd.read_csv('./레그킥완2.csv',index_col='이름',encoding= 'cp949')

df_grouped=df.groupby('LegKick')['장타율'].mean().reset_index()
df_grouped['LegKick'] = df_grouped['LegKick'].map({1: '레그킥 O', 0: '레그킥 X'})
bar_fig = px.bar(df_grouped,
                 x='LegKick',
                 y='장타율',
                 labels={'LegKick': '레그킥 여부', '장타율': '평균 장타율'},
                 title='레그킥 여부에 따른 평균 장타율 차이',
                 text='장타율')
bar_fig.update()

df_grouped3=df.groupby('LegKick')['삼진'].mean().reset_index()
df_grouped3['LegKick'] = df_grouped3['LegKick'].map({1: '레그킥 O', 0: '레그킥 X'})
bar_fig3 = px.bar(df_grouped3,
                 x='LegKick',
                 y='삼진',
                 labels={'LegKick': '레그킥 여부', '삼진': '평균 삼진'},
                 title='레그킥 여부에 따른 평균 삼진 차이',
                 text='삼진')
bar_fig3.update()

df_grouped4=df.groupby('LegKick')['출루율'].mean().reset_index()
df_grouped4['LegKick'] = df_grouped4['LegKick'].map({1: '레그킥 O', 0: '레그킥 X'})
bar_fig4 = px.bar(df_grouped4,
                 x='LegKick',
                 y='출루율',
                 labels={'LegKick': '레그킥 여부', '출루율': '평균 출루율'},
                 title='레그킥 여부에 따른 평균 출루율 차이',
                 text='출루율')
bar_fig4.update()

df2=df.reset_index()
df2.drop(['이름'],axis=1,inplace=True)
sns.heatmap(df2.corr(),cmap='Blues',annot=True, annot_kws={"size": 10})
plt.show()

