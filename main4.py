start_no = int(input("What is your required starting number"))
end_no = int(input("What is your required ending number"))

for i in range(start_no , end_no +1):
    if i%5 == 0:
        break
    print(i)