nums = [12, 13, 15, 16, 17]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")