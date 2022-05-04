
import re

rate="후기평점 4.8점"
rate1 = rate[5:-1]

re_rate=re.sub(r'[^0-9.]','',rate)




text = "123aabcA456!!@@ass"
re_text1 =re.sub(r'[a-z]','',text)
re_text =re.sub(r'[^A-Za-z0-9]','',text)




link ="https://www.coupang.com/vp/products/6199612862?itemId=12292717325&vendorItemId=79562995636&q=%EB%85%B8%ED%8A%B8%EB%B6%81&itemsCount=36&searchId=c6fb4b7d75644f3c802541c513c359a2&rank=3&isAddedCart="

n_s = link.find("itemId=")
n_e = link.find("&")

print(link[n_s+7:n_e])