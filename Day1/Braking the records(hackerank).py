string = input("Enter a string: ")
unique = []
count = 0
max_length = 0
for item in string:
    if item not in unique:
        unique.append(item)
        count += 1
    else:
        max_length = max(max_length, count)
        unique = []
        count = 1
print(max_length)


