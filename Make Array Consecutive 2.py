def solution(statues):
    num_max = max(statues)
    num_min = min(statues)
    counter = 0
    for i in range (num_min, num_max+1):
        if ( i not in statues):
            counter += 1

    return counter
        


def run():
    statues = [6, 2, 3, 8]
    print(statues)
    print(solution(statues))

if __name__ == '__main__':
    run()