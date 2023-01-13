def solution(a):
    even = sum([n for i, n in enumerate(a) if i % 2 == 0]) #par
    print(even)
    odd = sum([n for i, n in enumerate(a) if i % 2 != 0]) #impar
    print(odd)
    res = [even, odd]
    return res




def run():
    a = [50, 60, 60, 45, 70]

    print(a)
    print(solution(a))


if __name__ == '__main__':
    run()