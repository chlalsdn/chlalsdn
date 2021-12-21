'''
print (5)
print (-10)
print (3.14)
print (5 + 3)
print (2 * 8)
print (3 *(3 + 1))

print ('풍선')
print ("나비")
print ("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print ("ㅋ"*9)

print (5 > 10)
print (5 < 10)
print (True)
print (False)
print (not True)
print (not (5 > 10))

animal = "고양이"
name = '해피'
age = 3
hobby ='낮잠'
isAdult =age >=3

print ('우리집' + animal + "의 이름은" + name + '에요~')
hobby = '공놀이'
print (name + '는 ' + str(age) + '살이며, ' + hobby + '를 아주 좋아해요.')
print (name + '는 ', str(age),'살이며,', hobby,'를 아주 좋아해요.')
print (name + '는 어른일까요?' + str(isAdult))

#'#'은 한 문장을 주석처리합니다

이렇게 하면 
여려 문장이 
주석처리가 됩니다

A = '사당행' 
B = '신도림행'
C = '왕십리행'
 
print (A + ' 열차가 ' + '들어오고 있습니다!')
print (B + ' 열차가 ' + '들어오고 있습니다!')
print (C + ' 열차가 ' + '들어오고 있습니다!')

print (1+1)
print (3-72)
print (5*134)
print (9/3)

print (2**3) #2의 3승
print (5%3) #나눴을때 남는것 구하기
print (10%3) #나머지 구하기
print (5//3) #정수로 몫 구하기
print (10/3) #길게 몫 구하기

print (5 > 3)
print (4 >= 7)
print (10 < 3)
print (5 <= 5)

print (3 == 3) # == 는 같다는 뜻
print (4 == 2)
print (3 + 4 == 5)

print (1 != 3) # != 는 같지 않다는 뜻
print (not(1 != 3))

print ((3 > 0) and (3 < 5)) #and 대신 &를 넣어도 상관 없음
print ((3 >0) or (3 > 5)) #or 대신 |를 사용하여도 ㄱㅊ

print (5 > 4 > 3)
print (5 > 4 > 7)

print (2 + 3 * 4)
print ((2 + 3)*4)
number = 2+3*4
print (number)
number = number + 2 #이게 '가' 라면 
print (number)
number += 2 #이것은 '가'를 간결하게 쓴것임
print (number)
number *=2
print (number)
number /=2
print (number)
number -=2
print (number)
number %=2
print (number)
number %=5
print (number)

print (abs(-5)) #절댓값
print (pow(4, 2)) #승
print (max(5, 12)) #큰 수 고르기
print (min(5, 12)) #작은 수 고르기
print (round(3.14)) #반올림
print (round(4.99)) #반올림

from math import * #math (모듈)안에 들어가있는 코드를 불러다 올 때 쓰는 것들 ('*'는 모든것이라는 뜻)
print (floor(4.99)) # 버림 (수소자 뒤 숫자까지는 다 버림)
print (ceil(3.14)) #반올림이 아닌 그냥 올림 (다 올려버림)
print (sqrt(16)) #제곱근, 즉 4

from math import ceil #이것은 모든것중에 ceil만 쓰겠다는 말

from random import *
print (random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print (random() *10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print (int (random() *10)) # 0 ~ 10 미만의 임의의 값 생성
print (int (random() *10)+1) # 0 ~ 10 이하의 임의의 값 생성
print (int (random() *10)+1) # 0 ~ 10 이하의 임의의 값 생성
print (int (random() *10)+1) # 0 ~ 10 이하의 임의의 값 생성
print (int (random() *10)+1) # 0 ~ 10 이하의 임의의 값 생성
print (int (random() *10)+1) # 0 ~ 10 이하의 임의의 값 생성

print (randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print (randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print (randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print (randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print (randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print (randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print (randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print (randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print (randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print (randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

sentence = '나는 소년입니다'
print (sentence)
sentence2 = '파이썬은 쉬워요'
print (sentence2)
# ' ' 안에서의 ''은 줄바꿈 문자이다
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print (sentence3)
'''

#슬라이싱


