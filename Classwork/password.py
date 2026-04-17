#user enter`s a password 
#the application says ver week
#he enter`s again and it says weak passwor
#he keeps trying until it says strong password, Good!


password = (input(" Enter your password: "))


password_length = len (password)

if (password_length < 8):
   
   print("This is a  very weak password" )

elif(password_length == 8):
   
   print("This password is weak")

elif password_length >= 8 and password_length == 16:
   print("This password is strong")

elif(password_length > 16):
   print("This password is very strong")

    

 

