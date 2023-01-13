def solution(s1, s2):
    ls2 = list (s2) 
    counter =0
    for i in range(len(s1)):
        for j in range(len(ls2)):
            if s1[i] == ls2[j]:
                ls2.pop(j)
                counter += 1
                break

    return counter

def run():
    s1 = "aabcc" 
    #abcc   dcaa
    s2 = "adcaa"

    print(s1 + ' ' + s2)
    print(solution(s1, s2))


if __name__ == '__main__':
    run()