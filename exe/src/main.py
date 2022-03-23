#https://github.com/leehyowon14

import random
import os

list_file = open("./config/Voca.txt", "r", encoding='UTF8')
Voca_list = eval(list_file.read())

worng_answer = []

def isin(t,a):
    t_len = int(len(t))
    if t_len == 0:
        return False
    for i in range(0, t_len):
        if t[i] == a:
            return True
    return False

def Test(word):
    print("예문: "+word[1]+"\n단어: "+word[2])
    if input("\n정답을 입력하여 주세요 : ") == word[0]:
        print("\n정답입니다.")
    else:
        print(
            """
            오답입니다.
            정답: 
            """+word[0]
        )
        worng_answer.append(word)

if len(Voca_list) == 0:
    print("입력한 단어가 없습니다.")
    os.system("pause")

if input("시험순서를 랜덤으로 설정하시겠다면 y를 입력하여 주세요. : ") == "y":
    random_num_list = []
    while len(random_num_list) < len(Voca_list):
        random_num = random.randrange(0, len(Voca_list))
        if isin(random_num_list, random_num) == False:
            random_num_list.append(random_num)

    for num in random_num_list:
        Test(Voca_list[num])
else:
    for voca in Voca_list:
        Test(voca)

print("\n\n 정답 갯수 : "+str(len(Voca_list)-len(worng_answer))+"\n 오답 갯수 : "+str(len(worng_answer)))
os.system("pause")