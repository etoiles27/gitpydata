# 자판기 프로그램

Mymoney=[0] # 카드에 충전된 금액 
coffee = ["아메리카노(hot)", "아메리카노(ice)","카페라떼"] # 커피명 리스트
coffeecost=[2000,2500,4000] # 커피명 리스트에 해당되는 가격 리스트 
# coffee[0], coffeecost[0] -> 아메리카노 hot 을 지칭 하게된다. 
buymoney = [] # 구매 진행중인 커피 가격을 담는 리스트 
buycoffee=[] # 구매 진행중인 커피명을 담는 리스트 

flag = 0 # flag=1 금액부족으로 주문 진행중.
while True:
    # 금액 부족으로 주문진행이 없을경우 flag = 0 
    if flag ==0 :
        print('-'*100)
        print("[자판기 프로그램]")
        print("1. 금액충전")
        print("2. 아메리카노(hot) : 2000원")
        print("3. 아메리카노(ice) : 2500원")
        print("4. 카페라떼        : 4000원")
        print('-'*100)
    # 금액 부족으로 주문진행 시 flag = 1     
    elif flag == 1:
        print('-'*100)
        print("[자판기 프로그램]")
        print("1. 금액충전")
        print("2. 주문 진행")
        print('-'*100)
        
    choice = int(input("원하는 번호를 선택해주세요(종료:9) >>   "))
        
    # 금액 충전을 선택 했을 경우 
    if choice == 1:
        print("현재 잔액은 {}입니다".format(Mymoney[0]))
        money = int(input("충전할 금액을 입력하세요 >> "))
        # 입력 받은 금액을 카드에 더해준다. 
        Mymoney[0] = Mymoney[0]+money
        print("충전 후 잔액은 {}입니다".format(Mymoney[0]))
        
    # 커피 메뉴를 시켰을 경우     
    elif choice == 2 or choice == 3 or choice == 4:
        # # 금액 부족으로 주문진행이 없을경우  
        # if flag == 0:
        #     num = int(input("1.결재 2.계속주문 3.주문취소 >> "))
            
        # 금액 부족으로 주문진행중  
        if flag == 1:
            # 현재 진행중인 주문내역을 보여준다. 
            print("현재 주문하신 커피는 : {} 입니다. ".format(buycoffee))
        print('-'*100)
        num = int(input("1.결재 2.계속주문 3.주문취소 >> "))
        print('-'*100)
        # 결재 
        if num == 1:
            # choice 2인경우 아메리카노 가격은 coffeecost[0] 이기 때문에 
            # coffeecost[choice-2]를 해주면 해당되는 가격을 알 수 있다. 
            # 커피 가격을 buymoney리스트에 추가해준다. 
            if flag == 0:
                buymoney.append(coffeecost[choice-2])
                buycoffee.append(coffee[choice-2])
            
            # 잔액부족으로 진행중인 주문이 있을 경우에 [2.주문진행] 으로 들어왔기때문에
            # choice =2 선택이 아닌 주문진행이므로 추가 사항이 없다. 
            # elif flag == 1: buymoney.append(0)            
            
            # 구매하려는 총 커피의 가격이 카드에 충전된 가격을 넘지 않을 경우 주문할 수 있다 
            if Mymoney[0]>=sum(buymoney):  
                for co in buycoffee:
                    print(co,end=' ')
                print(" 주문완료")
                # 충전된 카드에 구매한 커피가격을 전부 더해서 뺀다. 
                Mymoney[0] = Mymoney[0]-sum(buymoney) 
                print("현재 잔액은 {}입니다".format(Mymoney[0]))
                # 구매후 구매하려한 리스트들을 비워준다. 
                buymoney=[]
                buycoffee=[]
                flag = 0
            else:
                print("금액이 부족합니다. ")
                print("현재 잔액은 {}입니다".format(Mymoney[0]-sum(buymoney)))
                print('-'*100)
                print("1.금액 충전  2.주문 취소")
                print('-'*100)
                selec = int(input ("원하는 메뉴를 선택해주세요 >> "))
                
                # 금액이 부족한 경우, 금액 충전으로 이동
                if selec == 1:
                    flag = 1
                    continue
                
                # 금액이 부족한 경우, 주문 취소로 이동 
                else:
                    # 주문이 취소될 경우에, 사려고 한 리스트 두개를 비워준다. 
                    buymoney=[]
                    buycoffee=[]
                    print("주문이 취소되었습니다. ")
                    flag=0
                    continue
        # 계속주문 
        if num == 2:
            # 구매가 계속 진행이 될 경우에 
            # 구매 진행중인 커피가격과 커피명 리스트에
            # 선택한 값을 넣는다. 
            buymoney.append(coffeecost[choice-2])
            buycoffee.append(coffee[choice-2])
            flag = 0 
            print("주문내역 : ", buycoffee)
        # 주문취소
        if num == 3:
            # 주문을 취소할 경우, 구매가 진행중인 리스트 두개를 비워준다. 
            buymoney=[]
            buycoffee=[]
            flag = 0 
            print("주문이 취소되었습니다. ")
           

    elif choice == 9:
        print("프로그램을 종료합니다. ")
        break 
