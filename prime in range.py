start = int(input("Enter 1st Number: "))
end = int(input("Enter 2nd Number: "))
for num in range(start, end+1):
    if num>1:
        for i in range(2, num):
            if num%i == 0:
                print(num,"not prime")
                break
        else:
            print(num,"is prime")