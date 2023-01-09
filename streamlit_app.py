import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.font_manager as fm

import subprocess

#print([f.fname for f in fm.fontManager.ttflist])

# 설치된 폰트 출력
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

my_font = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

if my_font in font_list:
  st.write(my_font)

nanum_font_list = fm.findSystemFonts(fontpaths='/usr/share/fonts/truetype/nanum/')

for font in nanum_font_list:
    print(f"Name: {fm.FontProperties(fname=font).get_name()} | Path: {font}")
    
# /home/appuser/venv/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/cmss10.ttf
  
# temp = subprocess.call(["sudo", "cd", "/usr/share/fonts/truetype/nanum/"])
temp = subprocess.call(["ls","-al", "/usr/share/fonts/truetype/nanum/"])
print(temp)

temp = subprocess.call(["fc-cache","-fv"])
print(temp)

# temp = subprocess.call(["cp", "/usr/share/fonts/truetype/nanum/Nanum*", "/home/appuser/venv/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/"])
# print(temp)
# cp /usr/share/fonts/truetype/nanum/Nanum* /usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf').get_name()
rc('font', family=font_name)


# usr/share/fonts/truetype/nanum/NanumGothic.ttf
# sudo cp /usr/share/fonts/truetype/nanum/Nanum* /usr/local/lib/python3.4/dist-packages/matplotlib/mpl-data/fonts/ttf/

for my_font in fm.fontManager.ttflist:
  if 'Nanum' in my_font.name:
    st.write(my_font)
  
# for font in fm.fontManager.ttflist:
#   print(font.fname)

# path = '/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf'
# fontprop = fm.FontProperties(fname=path)

# matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

st.title('Streamlit matplotlib 이용 그래프에서 한글 표시 방법')

st.write("네이버(하나은행 제공)에서 환율을 정보를 가져옵니다.")
st.markdown("## 주요 통화")


# 선 그래프 그리기

a = np.random.rand(100) * 100
df = pd.DataFrame(a)

plt.rcParams["font.family"] = 'NanumGothic'

ax = df.plot(grid=True, figsize=(15, 5))
ax.set_title("주가(종가) 그래프", fontsize=30) # 그래프 제목을 지정
ax.set_xlabel("기간", fontsize=20)             # x축 라벨을 지정
ax.set_ylabel("주가(원)", fontsize=20)         # y축 라벨을 지정
plt.xticks(fontsize=15)                    # X축 눈금값의 폰트 크기 지정
plt.yticks(fontsize=15)                    # Y축 눈금값의 폰트 크기 지정   

fig = ax.get_figure()                          # fig 객체 가져오기    
st.pyplot(fig)                                 # 스트림릿 웹 앱에 그래프 그리기
