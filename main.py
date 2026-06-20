def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(numbers):
    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


def sort_primes_descending(prime_numbers):
    return sorted(prime_numbers, reverse=True)


def main():
    numbers = [10, 7, 3, 4, 11, 15, 17, 20]

    prime_numbers = get_prime_numbers(numbers)
    sorted_primes = sort_primes_descending(prime_numbers)

    print("Sorted Prime Numbers:", sorted_primes)


if __name__ == "__main__":
    main()