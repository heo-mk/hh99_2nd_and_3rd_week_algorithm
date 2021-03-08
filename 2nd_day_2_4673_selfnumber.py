# def generator : 생성자 함수
def generator():
    every_numbers = set(range(1, 10001))
    generated_numbers = set()
    self_numbers = set()

    for i in range(1, 10001):       # i = 476
        for j in str(i):            # str(i) = '476', 문자열은 for 문에서 인덱스로 하나씩 분리가 된다.
            i += int(j)             # i = 476 + 4 + 7 + 6
        generated_numbers.add(i)
        self_numbers = sorted(every_numbers - generated_numbers)

    return self_numbers

result = generator()

for k in result:
    print(k)
