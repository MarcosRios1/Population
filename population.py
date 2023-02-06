n = 0
born = 0
passed = 0
ending = 0

def findpop():
    global n, born, passed, ending
    years = 0

    n = starting()
    ending = ending()
    
    while n < ending:
        born = n//3
        passed = n//4
        n -= passed
        n += born
        print(n)
        years += 1
        
    print(f'Years: {years}')
    print(n)

def starting():
    n_size = int(input('Starting population: '))
    if n_size < 9:
        print('Starting pop cannot be lower than 9')
        starting()
    else:
        print(f'Starting size: {n_size}')
        return n_size

def ending():
    global n
    end = int(input('Ending population: '))
    if end <= n:
        print('Must be higher than starting pop')
        ending()
    else:
        print(f'Ending size: {end}')
        return end

findpop()


