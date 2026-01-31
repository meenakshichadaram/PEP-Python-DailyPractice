file_name = "high_score.txt"
high_score = 0
score = 0

def load_high_score():
    global high_score
    try:
        file = open(file_name,"r")
        high_score = int(file.read())
    except:
        pass

def save_high_score():
    file = open(file_name,"w")               
    file.write(str(high_score))           
    file.close()

#play quiz 
def play_quiz():
    global score
    questions = ["what is output of print(2+3)?","which datatype stores true/false?","which keyword is used to fetch global variable in the function?"]
    answers = ["5","boolean","global"]
    for i in range(len(questions)):
        print("\nQ.",questions[i])
        user_answer = input("Your answer: ")
        if user_answer == answers[i]:
            score = score + 1
            print("Correct answer!")
        else:
            print("Wrong answer!")

def main():
    global high_score
    load_high_score()
    player_name = input("Enter your name: ")
    play_quiz()
    print("\nQuiz over!")
    print(player_name,"Your score is:",score)
    if score > high_score:
        high_score = score
        save_high_score()
    else:
        print("High score is:",high_score)

main()