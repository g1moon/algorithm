def insurance_calculator():
    quit_ = False
    while quit_ == False :
        print('\n')
        while True:
            try:
                A = int(input('현재 나이가 어떻게 되나요? '))
                if (type(A) != 'int') and (A <= 0):
                    print('ERROR: 잘못된 숫자입니다!')
                    continue
                break
            except:
                print('ERROR: 잘못된 숫자입니다!')
                continue

        while True:
            try:
                G = input("당신은 '여자'입니까 '남자'입니까? ")
                if (G !='남자') and (G !='여자'):
                    print("ERROR: '여자'또는 '남자'를 입력하세요! ")
                    continue
                break
            except:
                print("ERROR: '여자'또는 '남자'를 입력하세요! ")
                continue
        
        while True:
            try:
                M = int(input('매년 보험금으로 얼마를 지불할 예정입니까? '))
                if (type(M) != 'int') and (M <= 0):
                    print('ERROR: 잘못된 숫자입니다! ')
                    continue
                break
            except:
                print('ERROR: 잘못된 숫자입니다! ')
                continue

        while True:
            R = input('현재 이자율은 얼마입니까? ')
            try:
                R = float(R)
                break
            except:
                print('ERROR: 잘못된 숫자입니다! ')
                continue

        if G == '남자':
            E = 70
        elif G =='여자':
            E = 80 


        L=0    
        for i in range(1,E-A+1):
            L += (M) * ((1 + R)**i)

        print(f'이 고객에 대한 최대 보상 범위는 {"{:,}".format(round(L))}원 입니다.')
        C = input("\n계속하시려면 아무 키나 입력하세요(종료하려면 'quit'입력) => ")
    
        if C == 'quit':
            quit_ = True
        else:
            quit_ = False

        if quit_:
            print('Bye~~~~!!!')

insurance_calculator()
