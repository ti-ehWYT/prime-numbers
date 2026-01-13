start = int(input("Enter the start number:"))
stop = int(input("Enter the stop number:"))

"""
define a functions called primes_in_ranges 
to returns all prime numbers between start and stop
"""
def primes_in_range(start,stop):
    # create "primes" as a list to store the prime numbers
    primes = []

    # A loop to check if the number in range is prime or not
    for num in range(start, stop + 1): # stop + 1 because python range default wont include the number at "stop"
        if num < 2:
            continue # skip if number less than 2 as they are not prime, if greater than 2, the loop continues

        for i in range(2, int(num ** 0.5) + 1): # i is created by square root of number ( = factors) , + 1 as python default exclude last number in range
            if num % i == 0: # see if number divisible by i 
                break # divisible / remainder = 0 -> not prime and will start next number
        
        else:
            primes.append(num) # loop completed without break consider prime and add into list

    return primes
print(primes_in_range(start,stop))
        