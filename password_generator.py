import random
import string

alpha_small_list = list(string.ascii_lowercase)
alpha_cap_list = list(string.ascii_uppercase)
num_list = [*range(0,10)]
special_char_list = ['_', '$', '&', '!']
alphanum_list = num_list + alpha_cap_list + alpha_small_list + special_char_list
print (alphanum_list)
while True:
    print ("".join(map(str,random.choices(alphanum_list, k = random.randint(8,14)))))
    response = input("Another password? (y/n): ")
    if response[0].lower() == "y":
        continue
    else:
        break