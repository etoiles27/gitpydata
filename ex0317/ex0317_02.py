singer1 = {}
singer1['이름'] ='트와이스'
singer1['구성원 수'] = 9
singer1['데뷔']='서바이벌 식스틴'
singer1['대표곡']='SIGNAL'


singer2 = {}
singer2['이름'] ='BTS'
singer2['구성원 수'] = 7
singer2['데뷔']='2Cool'
singer2['대표곡']='Dynamite'


singer3 = {}
singer3['이름'] ='블랙핑크'
singer3['구성원 수'] = 4
singer3['데뷔']='Square one'
singer3['대표곡']='How you like that'

singer4 = {}
singer4['이름'] ='에스파'
singer4['구성원 수'] = 4
singer4['데뷔']='Black Mamba'
singer4['대표곡']='Dream come True'

singerList =[singer1,singer2,singer3,singer4]
print(singerList)


singL = [{'이름': '트와이스', '구성원 수': 9, '데뷔': '서바이벌 식스틴', '대표곡': 'SIGNAL'}, 
         {'이름': 'BTS', '구성원 수': 7, '데뷔': '2Cool', '대표곡': 'Dynamite'}, 
         {'이름': '블랙핑크', '구성원 수': 4, '데뷔': 'Square one', '대표곡': 'How you like that'}
         ]
singL.append({'이름': '에스파', '구성원 수': 4, '데뷔': 'Black Mamba', '대표곡': 'Dream come True'})

print(singL)