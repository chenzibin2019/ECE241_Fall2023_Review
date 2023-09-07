counter = 1

while counter <= 10:
    print(counter)
    counter += 1
    if counter % 2 == 0:
        continue
    if counter > 5:
        break
