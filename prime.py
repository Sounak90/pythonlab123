num = int(input("Enter a Number: "))
if num<=1:
    print(num,"is not prime")
else:
    for i in range(2, num):
        if num%i == 0:
            print(num,"not prime")
            break
    else:
        print(num,"is prime")
