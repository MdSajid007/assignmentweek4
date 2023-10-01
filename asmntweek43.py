def num_divide3(num):
    count = 0

    for i in range(1, num + 1):
        if i % 3 == 0:
            count = count + 1

    return count

while True:
    given_input= input("Enter a positive integer: ")
    
    if given_input == 'done':
        print("Bye !!")
        break


    try:
        num = int(given_input)
        
        if num < 1:
            print("please enter a positive number")
        else:
            result = num_divide3(num)
            print("numbers divisible by 3 among numbers from 1 to", num, ":", result)

    except ValueError:
        print("Please enter a positive number")
