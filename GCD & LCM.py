import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = math.gcd(a, b)
lcm = (a * b) // gcd
print("GCD is:", gcd)
print("LCM is:", lcm)



