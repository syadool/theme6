int = [9, 0]

while int[0] > int[1]:
    int.append(int[0] * 10 + int[1])
    int.append(int[1] * 10 + int[0])
    int.append(int[2] - int[3])
    print(int[4])
    int[0] -= 1
    int[1] += 1
