

list_names = ['주바다','공유진','김샛별','송선유','양홍욱']
# cnt = 1
# for list_name in list_names:
#     print('{}.{} '.format(cnt,list_name))
#     cnt +=1


# index를 넣고 싶을땐 enumerate 함수를 사용해주면된다. 
for i, list_name in enumerate(list_names):
    print('{}.{} '.format(i+1,list_name))

# enumerate 안에 start를 사용하면 시작인덱스를 지정할 수 있다.
for i, list_name in enumerate(list_names, start=1):
    print('{}.{} '.format(i,list_name))