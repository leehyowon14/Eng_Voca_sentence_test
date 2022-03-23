import os

voca = open("./config/Voca.txt", "wt", encoding='UTF8')
amount = int(input('단어의 갯수를 적어주세요. : '))

voca.write('list = [')
print("작성 순서: 단어, 영어 예문, 예문 의미")
print("예문을 적을 때에는 단어는 적지 마시고 '_' 여러개로 대체해주세요.")
for i in range(1, amount+1):
    word = input('단어를 적어주세요: ')
    sent = input('예문을 적어주세요: ')
    mean = input('예문의 뜻을 적어주세요: ')
    voca.write('["{}", "{}", "{}"],'.format(word, sent, mean))
voca.write(']')
voca.close()
print('Voca.py 세팅 완료')
os.system("pause")