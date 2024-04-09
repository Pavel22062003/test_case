def find_primes(start, end):
    result = []
    for i in range(start, end + 1):
        check = 1
        for d in range(2, int(i ** 0.5) + 1):
            if i % d == 0:
                check = 0
        if check == 1:
            result.append(i)
    return result


start_number = int(input('введите начальное число'))
end_number = int(input('введите конечное число'))
print(find_primes(start_number, end_number))
