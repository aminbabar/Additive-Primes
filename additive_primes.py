"""
 *****************************************************************************
   FILE:  additive_primes.py

   AUTHOR: Amin Babar

   ASSIGNMENT: Project 7: Additive Primes

   DATE: 10/20/17

   DESCRIPTION: The additive prime function results in a true and false
   response, depending on whether or not a number is additive prime, while the
   additive prime list funciton results in a list of additive prime numbers
   between 1 and the number n.
 *****************************************************************************
"""


def add_digits(number):
    """ This function sums up the digits for a given number"""
    # converts a number to a string and makes a list of the digits involved in
    # the number

    number = str(number)
    digits = list(number)
    sum_digits = 0

    # adds all the numbers in the list
    for n in range(len(digits)):
        sum_digits += int(digits[n])
    return sum_digits


def prime_test(number):
    """ This function tests whether a number is prime or not """

    # Tests for the divisibility of the number between 1 and the number itslef.
    # If exactly 2 divisors found, it returns true, but if more than 2 divisors
    # found, it results in False.
    n = 0
    for i in range(1, number + 1):
        if number % i == 0:
            n += 1
    if n > 2:
        return False
    elif n == 2:
        return True


def additive_prime(number):
    """ This function tests whether a number is an additive prime"""

    # Two base cases for this function. The first base case involves single
    # digit prime numbers, and the second base case involves the test for a
    # prime number
    # CITE: Professor Helmuth helped with the recursion part
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    elif not prime_test(number):
        return False

    # Adds the digits in a number, and then recursively calls on the additive
    # prime funtion
    else:
        addition = add_digits(number)
        return additive_prime(addition)


def additive_primes_list(n):
    """ Gives a list of all additive primes between 1 and a user input n"""
    additive_list = []

    # Considers all the numbers between 1 and n for the additive_prime
    # function, and adds the numbers that are additive primes to the
    # additive_list
    for i in range(1, n):
        if additive_prime(i):
            additive_list.append(i)
    return additive_list


def main():

    print(additive_primes_list(100))


if __name__ == "__main__":
    main()
