def solution(inputString):
    phrase = inputString.lower()
    phrase = phrase.replace(' ', '')
    inv_phrase = phrase[::-1]
    if phrase == inv_phrase:
        return True
    
    return False


def run():
    inputString = "aabaa"
    print(inputString)
    print(solution(inputString))

if __name__ == '__main__':
    run()