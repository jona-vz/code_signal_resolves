def solution(statues):
    num_max = max(statues)
    num_min = min(statues)
    counter = 0
    for i in range (num_min, num_max+1):
        if ( i not in statues):
            counter += 1
    
    print(counter)
    return counter


def run():
    a = [6, 2, 3, 8]
    print(a)
    solution(a)


if __name__ == '__main__':
    run()