import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.font_manager as fm

# path = '/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf'
# fontprop = fm.FontProperties(fname=path)

matplotlib.rcParams['axes.unicode_minus'] = False

st.title('Streamlit matplotlib 이용 그래프에서 한글 표시 방법')

st.write("네이버(하나은행 제공)에서 환율을 정보를 가져옵니다.")
st.markdown("## 주요 통화")


# 선 그래프 그리기

a = np.random.rand(100) * 100
df = pd.DataFrame(a)

ax = df.plot(grid=True, figsize=(15, 5))
ax.set_title("주가(종가) 그래프", fontsize=30) # 그래프 제목을 지정
ax.set_xlabel("기간", fontsize=20)             # x축 라벨을 지정
ax.set_ylabel("주가(원)", fontsize=20)         # y축 라벨을 지정
plt.xticks(fontsize=15)                    # X축 눈금값의 폰트 크기 지정
plt.yticks(fontsize=15)                    # Y축 눈금값의 폰트 크기 지정   

fig = ax.get_figure()                          # fig 객체 가져오기    
st.pyplot(fig)                                 # 스트림릿 웹 앱에 그래프 그리기
