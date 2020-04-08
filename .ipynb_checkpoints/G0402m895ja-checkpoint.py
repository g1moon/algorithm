'''
Student name: Jian Lee<이지안>',
Student number:12184895,
Work number:G0402m
'''

# file_name = 'G0402m895ja.py'


import os 
os.path.abspath( __file__ ).split('/')[-1]
file_name = os.path.abspath( __file__ ).split('/')[-1]

#------------------
f = open(file_name, 'r')
file_text = []

for idx, i in enumerate(f):
    
    if idx ==0: 
        continue
    
    file_text.append(i)
    
    
    if idx==4:break
    
f.close()
    
    
file_text[0] = file_text[0][0:-3]
file_text[1] = file_text[1][:-2]
file_text[2] = file_text[2][:-1]

file_text = file_text[:-1]
file_name = file_name[:-3]
print(file_text)
#----------------------------

def CheckFile():
    score = 0
    
    #1 파일명이 G로 시작하는지
    if file_name[0] == 'G':
        score += 10
#         print('1번')

    #2 파일명의 날짜부분이 옳은지 
    if file_name[1:5] == '0402':
        score += 10
#         print('2번')


    #3 파일명의 끝이 영문 소문자인지
    if file_name.split('.')[0][-1].islower():
        score += 10
#         print('3번')


    #4 파일명의 학번이 3자리 숫자인지
    if file_name[-5:-2].isdigit() and len(file_name[-8:-5])==3:
        score += 10
#         print('4번')

    #5 파일명의 이름이 2개 영문 소문자인지
    if file_name[-2:].islower() and len(file_name[-5:-3])==2:
        score += 10
#         print('5번')

    #6 
    if file_text[2].split(':')[-1] == file_name[0:6]:
        score += 10
#         print('6번')

    #7 파일내에 적혀있는 student name의 첫번째 영문 이니셜이// 파일명의 이름과 일치하는지
    if file_text[0].split(':')[-1].strip()[0].lower() == file_name[-2]:
        score += 10
#         print('7번')


    #8 파일 내에 적혀있는 student number와 파일명의 학번이 일치하는지
    if file_text[1].split(':')[1][-3:] ==file_name[-5:-2]:
        score += 10
#         print('8번')

    score += 20
    print(score)


    return score

CheckFile()




    
    

    

