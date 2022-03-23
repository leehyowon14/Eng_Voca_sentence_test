#https://github.com/leehyowon14

import random

from config import Voca

worng_answer = []

def isin(t,a):
    t_len = int(len(t))
    if t_len == 0:
        return False
    for i in range(0, t_len):
        if t[i] == a:
            return True
    return False

def Test(list):
    print("예문: "+list[1]+"\n단어: "+list[2])
    if input("\n정답을 입력하여 주세요 : ") == list[0]:
        print("\n정답입니다.")
    else:
        print(
            """
            오답입니다.
            정답: 
            """+list[0]
        )
        worng_answer.append(list)


if input("시험순서를 랜덤으로 설정하시겠다면 y를 입력하여 주세요. : ") == "y":
    random_num_list = []
    while len(random_num_list) < len(Voca.list):
        random_num = random.randrange(1, len(Voca.list) + 1)
        if isin(random_num_list, random_num) == False:
            random_num_list.append(random_num)

    for num in random_num_list:
        Test(Voca.list[num])
else:
    for list in Voca.list:
        Test(list)

print("\n\n 정답 갯수 : "+str(len(Voca.list)-len(worng_answer))+"\n 오답 갯수 : "+str(len(worng_answer)))