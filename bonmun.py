import turtle as tt
import string
import random
import os

tt.penup()
tt.hideturtle()
tt.speed(0)

#자동 줄바꿈 함수
def wrap_text(text, max_length):
    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += word + ' '
        else:
            lines.append(current_line.strip())
            current_line = word + ' '
    if current_line:
        lines.append(current_line.strip())

    return '\n'.join(lines)

qwerqwer = '학습할 본문을 선택해주세요.\n\n< 선택 가능 본문 목록 >'
qwerqwer += '\n((9B)) The Power Of Writing'
tt.write(qwerqwer, font=("Arial", 16, 'bold'), align="center")
tt.goto(0, -50)
while True:
    selection = input(">>")
    if selection in ['9B']: break
    tt.write('존재하지 않습니다.', font=("한컴 윤고딕 720", 12), align='center')

#작업 디렉토리 현 주소로 설정
nowdir = os.path.abspath(os.path.dirname(__file__))
os.chdir(nowdir)
print("Now Loading in second... {}".format(nowdir))

#파일 읽어들이기
selection += '.txt'
file = open(selection, encoding='UTF8')
content = file.read()
content = content.split('\n')
file.close()

file = open('exception.txt', encoding='UTF8')
exxp = file.read()
exxp = exxp.split('\n')
file.close()

print("Every loading completed!")
print("*"*30)

tt.goto(0, 0)
tt.clear()
tt.write('난이도를 선택해주세요.\n(1-3 or Z(전부 빈칸), default=2)', font=("한컴 윤고딕 760", 16, "bold"), align='center')
difficulty = input('>>')
if difficulty not in ['1', '2', '3', 'Z']: difficulty = 2
elif difficulty == 'Z': difficulty = 4
else: difficulty = int(difficulty)
difficulty = [1] + [0] * (4 - difficulty)

#자동 빈칸 함수
def binkan(text):
    words = text.split()
    replaced, result = [], []
    while True:
        for word in words:
            if random.choice(difficulty) and word not in exxp:
                p_word = word.strip(string.punctuation)
                word = word.replace(p_word, '[-]')
                replaced.append(p_word)
            else: p_word = word
            result.append(word)
        if len(replaced): break
    return ' '.join(result), replaced

#유저 인터페이스
def write_gosu():
    tt.clear()
    tt.goto(0, 50)#참고: 여기서 사용된 i는 아래 for문의 임시변수로, 다른 코드에서 임시변수 i를 사용할 수 없습니다.
    tt.write(wrap_text(content[2*i+1], 25), font=("한컴 윤고딕 760", 16, "bold"), align='center')
    tt.goto(0, -150)
    tt.write(wrap_text(processed, 40), font=('한컴 윤고딕 760', 16, 'bold'), align='center')

for i in range(len(content)//2):
    print("{}/{}번째 문장".format(i+1, len(content)//2))
    processed, real_binkan = binkan(content[2*i])
    hint = 0; opened_hint=[]
    hint_word = ('[-] ' * len(real_binkan[0]))[:-1]
    will_opened_hint = list(range(len(real_binkan[0])))
    write_gosu()
    dap = input('>>')
    while True:
        if hint < len(real_binkan[0]):
            qwerqwer = random.choice(will_opened_hint)
            will_opened_hint.remove(qwerqwer)
            opened_hint.append(qwerqwer)
            for k in opened_hint:
                hint_word = list(hint_word)
                hint_word[4*k+1] = real_binkan[0][k]
                hint_word = ''.join(hint_word)

        tt.color('red')
        hint += 1
        if dap.lower() == real_binkan[0].lower():
            processed = processed.replace('[-]', real_binkan[0], 1)
            del real_binkan[0]
            tt.color('green')
            if len(real_binkan) == 0: break
            hint = 0; opened_hint = []
            hint_word = ('[-] ' * len(real_binkan[0]))[:-1]
            will_opened_hint = list(range(len(real_binkan[0])))
        write_gosu()

        if hint > 0:
            tt.goto(0, 220)
            tt.write('힌트: ' + str(hint_word), font=("한컴 윤고딕 720", 12), align='center')
        dap = input('>>')