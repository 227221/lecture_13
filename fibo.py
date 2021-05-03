def recursive_ntb_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_ntb_fibo(n - 1) + recursive_ntb_fibo(n - 2)


def main():
    fibo_number = int(input("Zadejte cislo: "))
    fibo_sequence = []
    for number in range(fibo_number + 1):
        fibo_sequence.append(recursive_ntb_fibo(number))
    print(fibo_sequence)


if __name__ == '__main__':
    main()
