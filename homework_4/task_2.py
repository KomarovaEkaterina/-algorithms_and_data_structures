import cProfile
import timeit


def sieve(n):
    assert n <= 5761455
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func:
        if n <= key:
            size = pi_func[key]
            break
    a = [0] * size
    for i in range(size):
        a[i] = i

    a[1] = 0
    m = 2
    while m < size:
        if a[m] != 0:
            j = m * 2
            while j < size:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return b[n - 1]


def prime(x):
    count_simples = 1
    simple = 2
    num = 2

    while count_simples < x:
        flag = 0
        for i in range(1, num - 1):
            if num % i == 0:
                flag += 1
        if flag == 1:
            count_simples += 1
            simple = num
        num += 1
    return simple


def sieve_1(x):
    def eratosfen(n):
        a = [0] * n
        for i in range(n):
            a[i] = i

        a[1] = 0
        m = 2
        while m < n:
            if a[m] != 0:
                j = m * 2
                while j < n:
                    a[j] = 0
                    j = j + m
            m += 1

        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])

        return b

    simple_nums = []
    i = 2
    while len(simple_nums) < x:
        simple_nums = eratosfen(i)
        i += 1
    return simple_nums[-1]


print(sieve(10))
print(sieve_1(10))
print(prime(10))

print('** sieve **')
print(timeit.timeit('sieve(10)', number=10, globals=globals()))    # 0.0003065469999999973
print(timeit.timeit('sieve(100)', number=10, globals=globals()))   # 0.0038443989999999983
print(timeit.timeit('sieve(1000)', number=10, globals=globals()))  # 0.066706233

print('** sieve first version **')
print(timeit.timeit('sieve_1(10)', number=10, globals=globals()))    # 0.0033326520000000054
print(timeit.timeit('sieve_1(100)', number=10, globals=globals()))   # 0.455544339
print(timeit.timeit('sieve_1(1000)', number=10, globals=globals()))  # 112.892149706

print('** prime **')
print(timeit.timeit('prime(10)', number=10, globals=globals()))    # 0.00030490100000690745
print(timeit.timeit('prime(100)', number=10, globals=globals()))   # 0.06427985199999853
print(timeit.timeit('prime(1000)', number=10, globals=globals()))  # 18.200243754000013

cProfile.run('sieve(100)')
'''
172 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2.py:5(sieve)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
cProfile.run('sieve_1(100)')
'''
         31154 function calls in 0.056 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.056    0.056 <string>:1(<module>)
        1    0.001    0.001    0.056    0.056 task_2.py:59(sieve_1)
      541    0.052    0.000    0.054    0.000 task_2.py:60(eratosfen)
        1    0.000    0.000    0.056    0.056 {built-in method builtins.exec}
      542    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    30067    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
cProfile.run('prime(100)')
'''
         4 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.007    0.007    0.007    0.007 task_2.py:42(prime)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


'''
Решето Эратосфена определенно самый быстрый вариант, если правильно его применить. 
При выполнении этого задания у меня случился ступор именно с задачей про решето. 
Единственное, что смог родить мой мозг, это функция под названием sieve_1 (намеренно оставленная здесь)
Я изначально понимала, что это полнейши й бред и будет оооочень медленно, поэтому не сдала задание. 
После просмотра вебинара с разбором дз я (шейм он ми) взяла один из ваших вариантов решения с решетом, сравнила его 
со своей функцией и тем, что мой гениальный мозг предумал изначально. Я была права) Это был полнейший бред. 
'''
