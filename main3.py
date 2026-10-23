start_no = int(input("What is your required starting number"))
end_no = int(input("What is your required ending number"))

for i in range(start_no , end_no+1):
    if i%2 == 0 or i%3 == 0:
        continue
    print(i)