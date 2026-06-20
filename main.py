def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(numbers):
    print("Prime Numbers:", end=" ")

    for number in numbers:
        if is_prime(number):
            print(number, end=" ")

    print()


def main():
    numbers = [10, 7, 3, 4, 11, 15, 17, 20]
    get_prime_numbers(numbers)


if __name__ == "__main__":
    main()