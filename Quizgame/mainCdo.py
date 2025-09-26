import json
import random


score = 0

with open("questions.json","r") as f:
    questions = json.load(f)["science_questions"]
    
    
quuiz_questions = questions

print("*******Welcome to Science Quiz**********")

for i,q in enumerate(quuiz_questions,start=1):
    print(f"Q{i}.{q["question"]}")
    for j,opt in enumerate(q['options'],start=1):
        print(f"{j}.{opt}")
        
    answer = input("Your answer (1/2/3/4): ").strip()
    
    if answer.isdigit() and 1 <= int(answer) <= len(q['options']):
        if q['options'][int(answer)-1] == q['answer']:
            score += 1
            print("Correct answer!\n")
        else:
            print(f"Wrong! correcr answer:{q['answer']}\n")
else:
    print("invalid input! skiiping to next question")
    
    
print("Quiz finished")
print(f"Your score is {score/len(quuiz_questions)}")
    
    
    
    
        