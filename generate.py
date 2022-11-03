math = [1,2,3,4,4,4,4,5]
cnt = [0, len(math)]
cnt[1] -= 1
result = []

for generate in math:
    result.append(math[cnt[0]] * 10 ** cnt[1])
    cnt[0] += 1
    cnt[1] -= 1

print(sum(result))