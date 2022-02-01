#-----------------#
#  수하물 비용 계산  #
#-----------------#

weight = float(input("짐의 무게는 얼마인가?"))
num = float(input("짐의 개수는 몇 개인가?"))
fee = 0

if weight > 20 :
    print("20kg 이상은 20,000원 추가입니다.")
    fee = fee + 20000
else:
    print("짐 무개에 대한 수수료는 없습니다.")

if num > 2 :
    print("2개 이상은 30,000원 추가입니다.")
    fee = fee + 30000
else:
    print("짐 개수에 대한 수수료는 없습니다.")
print("총 가격은",fee, "입니다.")

#----------------#
#  졸업 시물레이션  #
#----------------#

score = int(input("몇 학점을 이수했습니까?"))

if score >= 140 :
    print("졸업 가능합니다.")
else:
    print("졸업 불가합니다.")

#------------------#
#  3의 배수 구별하기  #
#------------------#

num = int(input("3의 배수인지 알고싶은 수를 입력하시오"))
if num % 3 == 0
    print("3의 배수가 맞습니다.")
else:
    print("3의 배수가 아닙니다.")

#----------------#
#  물건값 계산하기  #
#----------------#

total = int(input("구입 금액은 얼마입니까?"))

if total >= 100000 :
    price = total * 0.95
    print("지불금액은",price,"입니다.")
else:
    print("지불금액은",total,"입니다.")

#------------------#
#  문자열의 중간문자  #
#------------------#

word = str(input("중간문자를 알고싶은 단어는 무엇인가?"))
length = len(word)

if length % 2 == 0 :
    ans1 = word[length//2]
    ans2 = word[length // 2 + 1]
    print("중앙글자는 다음과 같습니다.",ans1,ans2)
else:
    ans3 = word[length//2]
    print("중앙글자는 다음과 같습니다.", ans3)

#------------#
#  임금계산기  #
#------------#

wt=int(input("근무시간을 입력하시오"))
mon = int(input("시급을 입력하시오"))

if wt >40 :
    salary=40*mon + (wt-40)*1.5
    print("총임금은 다음과 같다.",salary)
else:
    salary = wt * mon * 1.5
    print("총임금은 다음과 같다.",salary)

#---------------#
# 성과급 계산하기  #
#---------------#

rank=int(input("실적을 입력하시오(단위: 만원)"))
if rank > 1200
    bonus = (rank - 1200) * 0.1
    print("보너스는",bonus,"입니다.")
else:
    print("보너스는 없습니다.")

# --------------#
#  나이 구별하기  #
#---------------#

age = int(input("나이를 입력하시오"))

if age <= 12 :
    print("어린이입니다.")
elif age >=13 and age <=30 :
    print("청소년입니다.")
elif age >= 31 and age <= 50:
    print("장년입니다.")
elif age >= 51
    print("노년입니다.")

#-----------------------#
#  음수, 양수, 0 구별하기  #
#-----------------------#

num = int(input("부호를 알고싶은 수를 입력하시오"))

if num >= 0 :
    if num == 0 :
        print(0)
    else:
        print("양수")
else:
    print("음수")

#------------#
#  로그인하기  #
#------------#

idList=["Kim","Lim"]
pwList=[72,68]
hisId=str(input("아이디를 입력하시오"))
hisPw=int(input("비밀번호를 입력하시오"))

hisPw

if hisId == idList[0] :
    if hisPw == pwList[0]:
        print("환영합니다 회원님 :)")
    else:
        print("잘못된 비밀번호입니다.")
elif hisId == idList[1] :
    if hisPw == pwList[1]:
        print("환영합니다 회원님 :)")
    else:
        print("잘못된 비밀번호입니다.")

#----------------#
#  숫자에서 한글로  #
#----------------#

num = list(input("숫자를 입력하시오"))
hun = num[0]
ten= num[1]
one = num[2]

if hun == 1 :
    print("일")
elif hun == 2 :
    print("이")
elif hun == 3 :
    print("삼")
elif hun == 4 :
    print("사")
elif hun == 5 :
    print("오")
elif hun == 6 :
    print("육")
elif hun == 7 :
    print("칠")
elif hun == 8 :
    print("팔")
elif hun == 9 :
    print("구")
elif hun == 10 :
    print("십")

if ten == 1 :
    print("일")
elif ten == 2 :
    print("이")
elif ten == 3 :
    print("삼")
elif ten == 4 :
    print("사")
elif ten == 5 :
    print("오")
elif ten == 6 :
    print("육")
elif ten == 7 :
    print("칠")
elif ten == 8 :
    print("팔")
elif ten == 9 :
    print("구")
elif ten == 10 :
    print("십")

if one == 1 :
    print("일")
elif one == 2 :
    print("이")
elif one == 3 :
    print("삼")
elif one == 4 :
    print("사")
elif one == 5 :
    print("오")
elif one == 6 :
    print("육")
elif one == 7 :
    print("칠")
elif one == 8 :
    print("팔")
elif one == 9 :
    print("구")
elif one == 10 :
    print("십")
print(hun,"백",ten,"십",one,"입니다.")

#-------------------------#
#  달의 일수 출력 (수정 전)  #
#-------------------------#
mon = list(input("몇 월의 일수가 궁금하신가요?(3월, 4월과 같이 입력해주십시오)"))
year = int(input("해당년도를 입력해주십시오"))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) : # 윤년인 경우
    if mon[0]==2: # 윤년인 경우 중 2월인 경우
        print("달의 일수는", 29, "입니다.")
    else: # 윤년인 경우 중 2월이 아닌 경우
        if mon == 4 and 6 and 10 : # 윤년이 경우 중 2월이 아닌 경우 중 4,6,10월인 경우
            print("달의 일수는", 30, "입니다.")
        else: # 윤년인 경우 중 2월이 아닌 경우 중 4,6,10월이 아닌 경우
            print("달의 일수는", 31, "입니다.")
else: # 윤년이 아닌 경우
    if mon[0] == 2: # 윤년이 아닌 경우 중 2월인 경우
        print("달의 일수는", 28, "입니다.")
    else: # 윤년이 아닌 경우 중 2월이 아닌 경우 중 4,6,10월 인 경우
        if mon == 4 and 6 and 10:
            print("달의 일수는", 30, "입니다.")
        else: # 윤년이 아닌 경우 중 2월이 아닌 경우 중 4,6,10월도 아닌 경우
            print("달의 일수는", 31, "입니다.")
#-------------------------#
#  달의 일수 출력 (수정 후)  #
#-------------------------#

year = int(input("해당년도를 입력해주십시오"))
mon = int(input("몇 월이 궁금하누"))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) : # 윤년인 경우
    if mon == 2 :
        print("28일임")
    elif mon == 4 and 6 and 10 :
        print("30일임")
    else :
        print("31일임")
else :
    if mon == 2 :
        print("29일임")
    elif mon == 4 and 6 and 10 :
        print("30일임")
    else :
        print("31일임")
#-------------------------#
#  현재 시간과 계절 출력하기  #
#-------------------------#

import time
now = time.localtime()
print("현재 시간은", time.asctime())

if now.tm_mon < 3 :
    print("겨울이네요.")
elif now.tm_mon < 5 :
    print("봄이네요.")
elif now.tm_mon < 9 :
    print("여름이었다ㅋ.")
elif now.tm_mon < 11 :
    print("가을이네요.")
elif now.tm_mon < 13 :
    print("겨울네요.")

#---------------------------#
# 원기둥의 표면적과 부피 구하기  #
#---------------------------#

radius = float(input("반지름을 입력하시오"))
height = float(input("높이를 입력하시오"))

surface = radius**2 * 3.14 * 2 + (height * 2 * radius * 3.14)

volume = height * 2 * radius * 3.14

print("표면적은",surface,"부피는",volume,"입니다.")

#-----------------#
#  숫자 맞추기 게임  #
#-----------------#

answer = 56
while answer == 56 :
    print("숫자 게임에 오신 것을 환영합니다.")
    guess = int(input("숫자를 맞춰보시오"))
    if guess == answer :
        print("정답입니다.")
    elif guess > answer :
            print("너무 큽니다.")
    else :
        print("너무 작습니다.")
