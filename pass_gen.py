import random
import string
import os


def user_option2():

    question_2 = input("""\t\t\t  1)Letters exclusive
                          2)Letters and numbers
                          3)Letters and punctuation
                          4)Numbers and punctuation
                          5)Letter, numbers and punctuation 
                        > """)
    os.system('cls')
    return question_2


        
def user_option():

    global question_1
    question_1 = input("\t\t\t  Length of password: ")
    if question_1.isnumeric():
        question_1= int(question_1)
        if question_1 >= 8:
          question_1=int(question_1)
          os.system('cls')
         
        else:
            os.system('cls')
            print("\t\t\t  Password is recommended to be 8 or more characters")
            user_option()
       
    else:
        os.system('cls')
        print("Please enter an integer!")
        user_option()



def password_gen(option, length):
   global password
   question_2 = user_option2()
   if question_2.isnumeric():
       question_2=int(question_2)
       if question_2 >0 and question_2 < 6:
          if question_2 == 1:
               gen1 = string.ascii_letters
               random1 = random.choices(gen1, k= question_1)
               password = "".join(random1)
               print(f"\t\t\t  Your password is: {password}")
          elif question_2 == 2:
               gen2 = string.hexdigits
               random2 = random.choices(gen2, k= question_1)
               password = "".join(random2)
               print(f"\t\t\t  Your password is: {password}")
          elif question_2 == 3:
               punc = string.punctuation
               stri = string.ascii_letters
               random_punc = random.choices(punc, k = question_1//2)
               random_stri = random.choices(stri, k = question_1//2)
               join_pns = random_punc + random_stri
               random3 = random.choices(join_pns, k= question_1)
               password ="".join(random3)
               print(f"\t\t\t  Your password is: {password}")
          elif question_2 == 4:
               punc = string.punctuation
               num = string.digits
               random_punc = random.choices(punc, k = question_1//2)
               random_num = random.choices(num, k = question_1//2)
               join_pnn = random_punc + random_num
               random4 = random.choices(join_pnn, k= question_1)
               password ="".join(random4)
               print(f"\t\t\t  Your password is: {password}")
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
               print(f"\t\t\t  Your password is: {password}")
       else:
           print("\t\t\t  Please enter the appropriate integer!\n")

           password_gen()
   else:
        print("\t\t\t  Please enter an integer!\n")

        password_gen()
  

        
       





