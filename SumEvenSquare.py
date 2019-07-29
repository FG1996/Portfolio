def sum_even_square(numbers):
    #function sums the square of all even numbers passed into function.
    sum_square=0
    for num in numbers:
        if num%2==0:
            sum_square+=num**2
    return sum_square