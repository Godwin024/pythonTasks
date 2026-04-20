
print(f"{"Multiplication Table" :32} ")

for number in range (10):
    if number != 10:
         print(number, end='  ')
    else:
        print(f"{" ": >6 }", end="")
    
    for count in range(1, 10,):
        if number  != 0:
            print(f"{number * count:>2}", end=" ")
        else:
            print(f"{count:>2}", end=" ")
            if number == 0 and count == 9:
                 print("\n ---", end=" ")
         
        
         #multiply = number * count
    
         #print(multiply, end=" ")

    print()

