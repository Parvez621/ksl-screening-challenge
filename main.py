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


def process_numbers(numbers):
    total_elements = len(numbers)

    prime_numbers = get_prime_numbers(numbers)
    sorted_primes = sort_primes_descending(prime_numbers)

    return total_elements, sorted_primes


def main():
    user_input = input("Enter integers separated by spaces: ")

    numbers = [int(num) for num in user_input.split()]

    total_elements, sorted_primes = process_numbers(numbers)

    print("\nTotal Elements Processed:", total_elements)
    print("Sorted Prime Numbers:", sorted_primes)


if __name__ == "__main__":
    main()