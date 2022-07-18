
from konlpy.tag import Okt

# konlpy 선언
okt = Okt()

text = '한글 자연어 처리는 재밌다. 이제부터 열심히 해야지 ㅎㅎㅎㅎㅎ'

print(okt.morphs(text))
print(okt.nouns(text)) # 명사만
print(okt.phrases(text)) # 어절단위
print(okt.pos(text)) # 품사도 함께 추출 (튜플)
print(okt.pos(text, join=True)) 

