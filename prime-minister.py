import math

def is_divisible_by(number, by):
    return number % by == 0

def is_prime(number):
    if number <= 1:
        return False
    # Only check up to the square root of the number for efficiency
    for i in range(2, int(math.sqrt(number)) + 1):
        if is_divisible_by(number, i):
            return False
    return True

def primes_in_range(start, end):
    for number in range(start, end + 1):  # Make the end value inclusive
        if is_prime(number):
            print(f"The number {number} is prime")

def main():
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    primes_in_range(start, end)

if __name__ == "__main__":
    main()
