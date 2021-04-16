import random 
import os  
import string 
 
random.seed = (os.urandom(1024)) 
 
 
letters = ['A','B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g''h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
spec =['~','!','@','#','$','%','^','&','*','-','+','='] 
numbers =['1','2','3','4','5','6','7','8','9','0'] 

all=[letters,spec,numbers]
 

def PasswordGen(n): 
    r=str() 
    for h in range (n): 
        r+=random.choice(random.choice(all)) 
    return r 
 
 
n=int(input()) 
print('Your password is : \n',PasswordGen(n))
