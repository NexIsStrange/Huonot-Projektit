i = 0

for times in range(100000):
    i += 1
    
    if i % 2 == 0:
        with open("code.py","a") as f:
            f.write(f"if num == {i}: #(this checks if the number {i} is even\n  print('Number Is Even!') #(this prints that the number {i} is even\n")
    else:
        with open("code.py","a") as f:
            f.write(f"if num == {i}: #(this checks if the number {i} is odd\n  print('Number Is Odd!') #(this prints that the number {i} is odd\n")