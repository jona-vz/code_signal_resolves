def solution(inputArray):
    lens = []
    res = []
    for i in range(len(inputArray)):
        lens.append(len(inputArray[i]))
    
    lmax = max(lens)
    for i in range(len(inputArray)):
        if len(inputArray[i])==lmax:
            res.append(inputArray[i])
            
    return res


def run():
    a = ['csocd', 'docmom', 'asd', 'polks', 'laks']

    print(a)
    print(solution(a))


if __name__ == '__main__':
    run()