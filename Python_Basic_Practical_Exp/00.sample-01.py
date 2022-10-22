# 숫자 맞추기 게임
import random

random_number = random.randint(1, 100)

# print(random_number)

game_count = 1  # 실패할 때마다 1씩 증가하게 된다.

while True:
    try:

        my_number = int(input("1~100 사이의 숫자를 입력하세요")) # int를 해주지 않게 되면, 문자형으로 인식을 하게 된다.

        if my_number > random_number:
            print("Down!!")
        elif my_number < random_number:
            print("Up!!")
        else:
            print(f"축하합니다. {game_count}번 만에 맞추셨습니다.") # f"{}"을 하게 되면 game_count에 대한 내용이 나오게 된다.
            break

        game_count = game_count + 1

    except:
        print("숫자로 입력해주세요")