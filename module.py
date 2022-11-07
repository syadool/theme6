result = []


def generate_body(math):
    cnt = [0, len(math)]
    cnt[1] -= 1
    result_draft = []

    for generate in math:
        result_draft.append(math[cnt[0]] * 10 ** cnt[1])
        cnt[0] += 1
        cnt[1] -= 1
    result.append(sum(result_draft))


def generate(math):
    math.sort()
    generate_body(math)


def reverse(math):
    math.sort(reverse=True)
    generate_body(math)


def calculate(result):
    result.sort(reverse=True)
    calculate_base = 0
    calculate_base = result[0] - result[1]
    result.clear()
    result.append(calculate_base)


def parse(result, math):
    math.clear()
    parse_base = []
    cnt = len(result[0])
