import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.font_manager as fm
from matplotlib import font_manager, rc
import subprocess

st.title('matplotlib 그래프에서 한글 폰트 설정 방법')
st.write('Streamlit cloud에서 matplotlib 이용할 때 한글 폰트를 사용한 예입니다.')

# 설치된 나눔 폰트 출력
temp = subprocess.call(["ls","-al", "/usr/share/fonts/truetype/nanum/"])
print(temp)

# font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_path = '/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
st.write("사용할 폰트 이름:", font_name)

matplotlib.rcParams['font.family'] = font_name
matplotlib.rcParams['axes.unicode_minus'] = False

# 선 그래프 그리기

a = np.random.rand(100) * 100
df = pd.DataFrame(a)

# plt.rcParams["font.family"] = 'NanumGothic'

ax = df.plot(grid=True, figsize=(15, 5))
ax.set_title("랜덤값 그래프", fontsize=30) # 그래프 제목을 지정
ax.set_xlabel("x축 값(기간)", fontsize=20)             # x축 라벨을 지정
ax.set_ylabel("y축 값(랜덤)", fontsize=20)         # y축 라벨을 지정
plt.xticks(fontsize=15)                    # X축 눈금값의 폰트 크기 지정
plt.yticks(fontsize=15)                    # Y축 눈금값의 폰트 크기 지정   

fig = ax.get_figure()                          # fig 객체 가져오기    
st.pyplot(fig)                                 # 스트림릿 웹 앱에 그래프 그리기
