import random
import string


def user_option():
    global question_2, question_1
    question_1 = int(input("Length of password: "))
    if question_1 >= 8:
        question_2 = int(input("""1)Letters exclusive\n2)Letters and numbers\n3)Letters and punctuation\n4)Numbers and punctuation\n5)Letter, numbers and punctuation 
> """))
       
    else:
        print("Please choose a password length with 8 characters or more")
        user_option()
user_option()

  

def password_gen():
    if question_2 == 1:
        gen1 = string.ascii_letters
        random1 = random.choices(gen1, k= question_1)
        password = "".join(random1)
        print(f"Your password is: {password}")
    elif question_2 == 2:
        gen2 = string.hexdigits
        random2 = random.choices(gen2, k= question_1)
        password = "".join(random2)
        print(f"YOur password is: {password}")
    elif question_2 == 3:
        punc = string.punctuation
        stri = string.ascii_letters
        random_punc = random.choices(punc, k = question_1//2)
        random_stri = random.choices(stri, k = question_1//2)
        join_pns = random_punc + random_stri
        random3 = random.choices(join_pns, k= question_1)
        
        password ="".join(random3)
        print(f"Your password is: {password}")

        
password_gen()











