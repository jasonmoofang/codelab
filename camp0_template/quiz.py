quiz = {
        "What is the name of Hiccup's Night Fury dragon?":
            "Toothless",
        "Which country won the Thomas Cup in 2014?":
            "Japan",
        "Who is the soulmate of Barbie?":
            "Ken",
        "How many countries are there in South East Asia (in numbers)?":
            "11",
        "What is the Theme Song of Frozen?":
            "Let it go"
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

print "The quiz is over! Your final score is:"
print total_score
