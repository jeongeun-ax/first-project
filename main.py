# 가위 바위 보 게임 미니 프로젝트 

import random
try_count = 0
my_score = 0
computer_score = 0
game_list = ("가위", "바위", "보")


print("=" * 30)
print("가위 / 바위 / 보 게임")
print("=" * 30)
print("1. 가위 / 2. 바위 / 3. 보")



while True: 
    number = random.randint(1, 3)
    user_input = input("번호를 선택하세요. : ")

    if user_input == "q":
        print(f"게임 종료합니다.")
        break

    if not user_input.isdecimal():
        print("숫자(1~3)만 입력해주세요.")
        continue

    user_number = int(user_input) 

    if user_number <= 0 or user_number > 3:
        print("1 ~ 3 사이값을 입력하세요.")
        continue

    print()
    print("[게임 결과]")
    print()
    print(f"나: {user_number}.{game_list[user_number-1]} vs 컴퓨터: {number}.{game_list[number-1]}")

    
    try_count += 1

    if user_number == number:
        print("=> 비김")
    elif user_number == 1 and number == 2:
        print("=> 패배")
        computer_score += 1
    elif user_number == 1 and number == 3:
        print("=> 승리")
        my_score += 1
    elif user_number == 2 and number == 1:
        print("=> 승리")
        my_score += 1
    elif user_number == 2 and number == 3:
        print("=> 패배")
        computer_score += 1
    elif user_number == 3 and number == 1:
        print("=> 패배")
        computer_score += 1
    elif user_number ==3 and number == 2:
        print("=> 승리")
        my_score += 1


    print()
    print(f"현재 스코어 나 {my_score} : 컴퓨터 {computer_score}")
    print("-" * 30)

    if my_score >= 2:
        print("=" * 30)
        print("승리했습니다!")
        print("=" * 30)
        user_input = input("다시 도전 (yes/no) : ")
    elif computer_score >= 2:
        print("=" * 30)
        print("L을 가져가")
        print("=" * 30)
        user_input = input("다시 도전 (yes/no) : ")
    

    if user_input == "y":
        my_score = 0 
        computer_score = 0
        try_count = 0
    elif user_input == "n":
        print(f"게임 종료합니다.")
        break

