def solution(a):
    b = sorted([num for num in a if num!= -1])
    res = []
    j=0
    for i in range(len(a)):
        if a[i] == -1:
            res.append(-1)
        else:
            res.append(b[j])
            j+=1

    return res



def run():
    n = [-1, 150, 190, 170, -1, -1, 160, 180]

    print(n)
    print(solution(n))


if __name__ == '__main__':
    run()