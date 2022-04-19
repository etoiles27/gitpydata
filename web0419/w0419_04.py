import requests
import re # 정규표현식 라이브러리

url = "http://www.google.com"
res = requests.get(url) # url 파일정보 가져오기
res.raise_for_status()  # 200코드 확인

# print(res.text)

# if res.status_code==requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("비정상입니다.")

# 정규표현식


p = re.compile("ca.e") # 문자열의 시작
temp=input("문자를입력하세요 >> ")
m = p.search(temp)
if m:
    print("매칭단어 : " , m.group()) # compile 정규표현식에 맞는 부분 출력
    # print("매칭단어 : " , m.string) # compile 정규표현식에 맞는 입력문자 전체출력
    # print("매칭단어 : " , m.start()) # compile 정규표현식에 맞으면 시작위치
    # print("매칭단어 : " , m.end())    #  compile 정규표현식에 맞으면 끝나는 위치 
    # print("매칭단어 : " , m.span())    #  compile 정규표현식에 맞으면 시작, 끝나는 위치 
else:
    print("매칭되는 단어가 없습니다.")



# # match: 정확히 일치해야. 
# # search: (-> 문서 전체에 하나만 찾아준다)단어내 포함되어있으면 찾아준다 
# # findall -> 전체를 다 찾아준다. 
# p = re.compile("ca.e") # 문자열의 시작
# m = p.match("good care  good cafe ")
# if m:
#     print("매칭단어 : " , m.group())
# else:
#     print("매칭되는 단어가 없습니다.")

# n = p.search("good care  good cafe ")
# if n:
#     print("매칭단어 : " , n.group())
# else:
#     print("매칭되는 단어가 없습니다.")
    
# k= p.findall("good care  good cafe")
# if len(k)==0:
#     print("매칭 단어가 없습니다.")
# else:
#     print(k)





# img="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"
# p = re.compile("^/images") # 문자열의 시작
# m = p.match(img)
# if m:
#     print("http://www.google.com"+ m.group())
# else:
#     print("매칭되는 태그가 없습니다.")




# p=re.compile("ca.e") # 정규표현식 세팅

# print("정규표현식과 일치하는지 확인합니다")
# temp = input("문자를 입력하세요 >> ")

# m=p.match(temp)    # 입력된 문자 case가 정규표현식과 일치하는지 확인

# if m:
#     print("일치하는 문자 : ",m.group())
# else:
#     print("해당문자는 일치하지 않습니다.")