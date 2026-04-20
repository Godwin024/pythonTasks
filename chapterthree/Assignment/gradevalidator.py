passes = 0
validate_score = 10


for student in range (validate_score):
    
    while (True):

     result = int(input("Enter result (1 = pass 2 = fail): "))

     if result == 1 or result ==2:
        break

     else: 
         print("Wrong input, please enter 1 or 2 to proceed.")
     
if result  == 1:
    passes += 1

failures = validate_score -passes 

print("passed: ", passes)
print("failures: ", failures )

if passes > 8:
  print("Bonus to instructor")

