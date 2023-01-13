def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray)-1):
        prod = inputArray[i]*inputArray[i+1]
        if prod > max:
            max = prod
    
    return max
        


def run():
    inputArray = [3, 6, -2, -5, 7, 3]
    print(inputArray)
    print(solution(inputArray))

if __name__ == '__main__':
    run()