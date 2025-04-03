def fizzbuzz(k):
    if k % 3 == 0 and k % 5 != 0:
        return 'Fizz'
    if k % 5 == 0 and k % 3 != 0:
        return "Buzz"
    if k % 5 == 0 and k % 3 == 0:
        return "FizzBuzz"
    if k % 5 != 0 and k % 3 != 0:
        return k
