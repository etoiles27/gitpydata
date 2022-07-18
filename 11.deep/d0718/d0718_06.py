from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = '파이썬 파이썬 파이썬 워드클라우드 워드클라우드 라이브러리 좋아 좋아 예시 워드클라우드 워드클라우드 데이터분석 데이터 분석 파이썬 파이썬 파이썬 파이썬 딥러닝 딥러닝 딥러닝 머신러닝'

wordcloud = WordCloud(font_path='C:\Windows\Fonts\gulim.ttc').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()