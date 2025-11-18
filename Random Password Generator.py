# imorting random and string module
import random 
import string 

# defining password length and character values
pass_len=12
charvalues=string.ascii_letters + string.digits + string.punctuation  

# generating random password
password="" 
for i in range(pass_len):
    password+=random.choice(charvalues) 

print("Your Randomly Generated Password is:", password)