# Lecture 01_Python
# Homework 01_맛집 고르기

# Declaration
import random
한식=("김밥천국","서울 불고기","돕감자탕")
중식=("남경","몽중헌","빠오즈푸")
일식=("호야스시","토끼정","사보텐")

# Methods
def Eunneun_Detaction(k_word):
    if (ord(k_word[len(k_word)-1])-44032)%28 == 0:
        return "는"
    else:
        return "은"

# Main
print("\n안녕하세요.\n")
Eunneun_Detaction("빠")
while True:
    user_input = input("한식,중식,일식 중 한가지를 골라주세요:")
    if user_input in ("한식","중식","일식"):
        tmp = random.choice(eval(user_input))
        print(user_input + "이라면, " + tmp + Eunneun_Detaction(tmp) + " 어떨까요?\n")
        break
    else:
        print("\n" + user_input + "이라구요？\n죄송합니다. 다시 입력해주세요.\n")

# Notes
# Line 22 if, in 참고 : https://www.daniweb.com/programming/software-development/threads/64456/python-logical-or
# Line 22 eval 참고 : http://stackoverflow.com/questions/15168765/python-3-get-value-of-variable-entered-from-user-input
# Line 11 은/는 출력 참고 :  http://lpesign.tistory.com/9
#                           https://nemisj.com/python-api-javascript/
