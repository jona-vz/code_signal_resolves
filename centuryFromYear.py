def solution(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
        
    return century

def run():
    year = 1905
    print(year)
    print(solution(year))

if __name__ == '__main__':
    run()