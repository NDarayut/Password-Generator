def user_option():
    global question_2, question_1
    question_1 = int(input("Length of password: "))
    if question_1 >= 8:
        question_2 = int(input("""1)Letters exclusive
2)Letters and numbers
3)Letters and punctuation
4)Numbers and punctuation
5)Letter, numbers and punctuation 
> """))
       
    else:
        print("Password length should be 8 characters or more")
        user_option()

user_option()
