data = 'aaaaabbbcccccccdddddddd'
encoded = ''

count = 1
for i in range(1, len(data)):
    if data[i] == data[i-1]:
        count += 1
    else:
        encoded += data[i-1] + str(count)
        count = 1


    if i == len(data) -1:
        encoded += data[i] + str(count)


print(encoded)