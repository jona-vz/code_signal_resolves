def solution(n):
    '''
    n=1 -->  1 = 0 + 1 = 1**2 + 0 = 1**2 + 0**2
    n=2 -->  5 = 4 + 1 = 2**2 + 1
    n=3 --> 13 = 9 + 4 = 3**2 + 4
    '''
    return n**2 + (n-1)**2

        


def run():
    n = 3
    print(n)
    print(solution(n))

if __name__ == '__main__':
    run()