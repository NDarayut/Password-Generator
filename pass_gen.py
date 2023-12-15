import random
import string
import os

def user_option2():
    global question_2
    question_2 = int(input("""1)Letters exclusive
2)Letters and numbers
3)Letters and punctuation
4)Numbers and punctuation
5)Letter, numbers and punctuation 
> """))
        
def user_option():
    global question_1
    question_1 = input("Length of password: ")
    if question_1 >= "8" and question_1.isnumeric():
        question_1=int(question_1)
        os.system('cls')
        user_option2()
       
    else:
        print("Password length should be 8 characters or more")
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
        print(f"Your password is: {password}")
   elif question_2 == 3:
        punc = string.punctuation
        stri = string.ascii_letters
        random_punc = random.choices(punc, k = question_1//2)
        random_stri = random.choices(stri, k = question_1//2)
        join_pns = random_punc + random_stri
        random3 = random.choices(join_pns, k= question_1)
        password ="".join(random3)
        print(f"Your password is: {password}")
   elif question_2 == 4:
        punc = string.punctuation
        num = string.digits
        random_punc = random.choices(punc, k = question_1//2)
        random_num = random.choices(num, k = question_1//2)
        join_pnn = random_punc + random_num
        random4 = random.choices(join_pnn, k= question_1)
        password ="".join(random4)
        print(f"Your password is: {password}")
   elif question_2 == 5:
        punc = string.punctuation
        num = string.digits
        stri = string.ascii_letters
        random_punc = random.choices(punc, k = question_1//2)
        random_num = random.choices(num, k = question_1//2)
        random_stri = random.choices(stri, k = question_1//3)
        join_pnn = random_punc + random_num + random_stri
        random5 = random.choices(join_pnn, k= question_1)
        password ="".join(random5)
        print(f"Your password is: {password}")
   else:
        print("Please enter the appropriate integer!")
       





