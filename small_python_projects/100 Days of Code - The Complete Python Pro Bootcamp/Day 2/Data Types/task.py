x = range (1000)
y = 0
for i in x:
    if i % 3 == 0 or i % 5 == 0:
        y = y + i

print(y)