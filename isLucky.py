def solution(n):
    n = list(str(n))
    hlen = len(n)//2
    sum1 = sum2 = 0
    for i in range(hlen):
        sum1 += int(n[i])
        sum2 += int(n[i+hlen])

    if sum1 == sum2:
        return True
    
    return False


def run():
    n = 1230

    print(n)
    print(solution(n))


if __name__ == '__main__':
    run()