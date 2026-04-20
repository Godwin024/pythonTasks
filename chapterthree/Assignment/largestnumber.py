
largest = 0
second_largest = 0


for count in range(10):
    number = int(input(f"Enter your number {count + 1}: "))
    
    
    if number > largest:
        second_largest = largest 
        largest = number         
    else:
        if number > second_largest:
            second_largest = number

print(f"The largest is: {largest}")
print(f"The second largest is: {second_largest}")

