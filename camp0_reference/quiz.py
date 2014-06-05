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
passing_mark = 8

def ask_question(question, right_answer):
    global total_score
    print question
    input_answer = raw_input("Enter answer:")
    if input_answer == right_answer:
        total_score = total_score + 2
        print "That was correct!"
    else:
        print "That was wrong :( The answer was: " + right_answer

def ask_question_tweak_scoring(question, right_answer):
    global total_score
    print question
    input_answer = raw_input("Enter answer:")
    if input_answer == right_answer:
        total_score = total_score + 4
        print "That was correct!"
    else:
        total_score = total_score - 1
        print "That was wrong :( The answer was: " + right_answer

def ask_question_until_correct(question, right_answer):
    global total_score
    print question
    input_answer = raw_input("Enter answer:")
    while input_answer != right_answer:
        print "That was wrong :( Try again?"
        input_answer = raw_input("Enter answer:")
    total_score = total_score + 2
    print "That was correct!"


print "Welcome to the quiz!"
to_continue = "yes"
while to_continue == "yes":
    for q, a in quiz.iteritems():
        ask_question(q,a)
    print "The quiz is over! Your final score is: " + str(total_score)
    if total_score >= passing_mark:
        print "You passed!"
    else:
        print "You failed :("
    to_continue = raw_input("Would you like to go again? (yes/no):")