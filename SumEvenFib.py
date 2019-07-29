def sum_even_fib():

    #given the repetitive nature of even fibonacci sequence, where every thing element is even, the problem can be
    #simplified to F(n)=4*F(n-3)+f(n-6).

    fn_6 = 0
    fn_3 = 2
    sum_f = 2
    for i in list(range(98)):
        temp = 4*fn_3+fn_6
        fn_6 = fn_3
        fn_3 = temp
        sum_f += fn_3
    return sum_f


print(sum_even_fib())

