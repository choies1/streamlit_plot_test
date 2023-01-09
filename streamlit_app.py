import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.font_manager as fm
from matplotlib import font_manager, rc
import subprocess

# 설치된 나눔 폰트 출력
print("--> font output test")

# temp = subprocess.call(["ls","-al", "/usr/share/fonts/truetype/nanum/"])
# print(temp)

font_path = '/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf'

font_name = font_manager.FontProperties(fname=font_path).get_name()
print("font_name", font_name)
# rc('font', family=font_name)
matplotlib.rcParams['font.family'] = font_name


# usr/share/fonts/truetype/nanum/NanumGothic.ttf
# sudo cp /usr/share/fonts/truetype/nanum/Nanum* /usr/local/lib/python3.4/dist-packages/matplotlib/mpl-data/fonts/ttf/

# for my_font in fm.fontManager.ttflist:
#   if 'Nanum' in my_font.name:
#     st.write(my_font)
  
# for font in fm.fontManager.ttflist:
#   print(font.fname)

# fontprop = fm.FontProperties(fname=path)

# matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

st.title('Streamlit matplotlib 이용 그래프에서 한글 표시 방법')

st.write("네이버(하나은행 제공)에서 환율을 정보를 가져옵니다.")
st.markdown("## 주요 통화")


# 선 그래프 그리기

a = np.random.rand(100) * 100
df = pd.DataFrame(a)

# plt.rcParams["font.family"] = 'NanumGothic'

ax = df.plot(grid=True, figsize=(15, 5))
ax.set_title("주가(종가) 그래프", fontsize=30) # 그래프 제목을 지정
ax.set_xlabel("기간", fontsize=20)             # x축 라벨을 지정
ax.set_ylabel("주가(원)", fontsize=20)         # y축 라벨을 지정
plt.xticks(fontsize=15)                    # X축 눈금값의 폰트 크기 지정
plt.yticks(fontsize=15)                    # Y축 눈금값의 폰트 크기 지정   

fig = ax.get_figure()                          # fig 객체 가져오기    
st.pyplot(fig)                                 # 스트림릿 웹 앱에 그래프 그리기
