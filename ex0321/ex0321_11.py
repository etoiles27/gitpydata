def dic_func(**para):
    for k, v in para.items():
        print('{} --> {}명'.format(k,v))

dic_func(트와이스=9,소녀시대=7,걸스데이=4,블랙핑크=4)


# def dic_func(para):
#     for k, v in para.items():
#         print('{} --> {}명'.format(k,v))
# mydic = {'트와이스':9,'소녀시대':7,'걸스데이':4 }
# dic_func(mydic)
