# ksl-screening-challenge

## Overview

This project is a Python-based command-line utility that processes a list of integers provided by the user.

The program:
1. Accepts a list of integers as input.
2. Identifies and filters prime numbers from the list.
3. Sorts the prime numbers in descending order.
4. Displays the sorted prime numbers along with the total number of elements processed.

## Features
* Modular and reusable code structure
* Prime number detection using an optimized algorithm
* Descending order sorting
* Command-line user input
* Total element count reporting

## Requirements

* Python 3.x

## Project Structure

```text
ksl-screening-challenge/
│
├── main.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-github-username>/ksl-screening-challenge.git
```

2. Navigate to the project directory:

```bash
cd ksl-screening-challenge
```

3. Run the program:

```bash
python main.py
```

## Example

### Input

```text
Enter integers separated by spaces: 10 7 3 4 11 15 17 20
```

### Output

```text
Total Elements Processed: 8
Sorted Prime Numbers: [17, 11, 7, 3]
```

## Implementation Details

The application is organized into the following functions:

* `is_prime(number)` – Determines whether a number is prime.
* `get_prime_numbers(numbers)` – Extracts prime numbers from the input list.
* `sort_primes_descending(prime_numbers)` – Sorts prime numbers in descending order.
* `process_numbers(numbers)` – Coordinates processing and counting.
* `main()` – Handles user input and displays output.
