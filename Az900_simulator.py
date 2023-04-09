import random 
import bs4
import re
import os
import time

def connect_to_az900():
    filepath = os.path.join('x:', '\\xxxx', 'xxxx', 'xxxx', 'xxxx', 'az900github_html.txt') # to be replaced with your path
    fileObject = open(filepath, 'r',encoding = 'utf-8')
    txt_html = fileObject.read()
    soup = bs4.BeautifulSoup(txt_html, 'html')
    question = soup.find_all("a", {"class": "anchor"})[9:]
    answer = soup.find_all("ul", {"contains-task-list"})
    list_Q_A= []
    for i in range(485):
        list_Q_A.append([re.search(r'href=\"(.*?)\"', str(question[i])).group()[7:], [(i, r) for i, r in enumerate(re.findall(r"(/)\>(.*?)\<(/)", str(answer[i])))], re.findall(r"(checked)(.*?).(<)",str(answer[i]))])
    return list_Q_A
list_Q_A = connect_to_az900()
rnd_range = range(0,485)
num_quiz = 0
correct_answer_ = 0
while num_quiz != 50:
    time.sleep(5)
    os.system('cls')
    rnd = random.choices(rnd_range)
    print(list_Q_A[rnd[0]][0][:-1].replace("-", " "))
    correct_answer = list_Q_A[rnd[0]][2][0][1].split(">")[1].strip().upper()
    for q in list_Q_A[rnd[0]][1]:
        ans = re.findall(r"(') (.*?).(')", str(q))[0][1]
        print(f"{q[0]} => {ans}")
    user_answer = input("Choose The correct one: ").upper().strip()
    if user_answer != correct_answer:
        print(f"The correct one is {correct_answer}")
    else:
        correct_answer_ =+ 1 
    num_quiz += 1
if correct_answer_ >= 40:
    print(f"Congratulation you pass the exam! , score=> {correct_answer_}")
else:
    print(f"score=> {correct_answer_}\n.Try to learn more on https://learn.microsoft.com/en-us/certifications/exams/az-900/")

