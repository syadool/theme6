l = [1, 6, 3, 2, 5]
length = len(l)
e = []
cnt = 0
while length == 0:
    e.append(l[cnt] * 10 ** length)
    length -= 1
    cnt += 1

print(sum(e))