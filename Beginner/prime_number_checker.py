# prime number checker function
# prime number is a number that can be divided by itself and 1 and no other number

# my first attempt
# def prime_checker(number):
#     count = 0
#     for num in range(100):
#         if num / number == 1 or num / number == number:
#             count += 1
#     if count == 1:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

def prime_checker(number):
    # toggle to False if code detects if not a prime number
    is_prime = True
    # check if prime number, starting from 2 since a prime number is a number that can only be divided by itself and 1 cleanly
    # that's why not increasing by 1 at the end too
    for i in range(2, number):
        # print("i", i)
        # print("modulus", number % i)
        if number % i == 0:
            is_prime = False
    #     print("ip in for", is_prime)
    # print("ip out for", is_prime)
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())
prime_checker(number=n)
