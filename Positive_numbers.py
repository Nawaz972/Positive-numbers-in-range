# Positive numbers in the given range
start = int(input("Enter the starting number of range: "))                       # Reading first number in the range
end = int(input("Enter the ending number of range: "))                          # Reading last number in the range
for n in range(start, end + 1):                     
    if n >= 0:
        print(n, end = " ")                 # Printing the positive numbers