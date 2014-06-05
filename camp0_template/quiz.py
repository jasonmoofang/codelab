quiz = {
        "What is Python?":
            "A programming language",
        "Who is called the Father of Computer Science?":
            "Alan Turing",
        "Who is the current president of the US?":
            "Barack Obama",
        "In which country was Albert Einstein born?":
            "Germany",
        "Is the iPhone a computer?":
            "Yes"
        }

total_score = 0

def ask_question(question, right_answer):
    global total_score
    print question
    input_answer = raw_input("Enter answer:")
    if input_answer == right_answer:
        total_score = total_score + 2
        print "That was correct!"
    else:
        print "That was wrong :( The answer was: " + right_answer


print "Welcome to the quiz!"

for q, a in quiz.iteritems():
    ask_question(q,a)

print "The quiz is over! Your final score is: " + str(total_score)