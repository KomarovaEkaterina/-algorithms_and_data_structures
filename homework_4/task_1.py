import cProfile
import sys
import timeit

sys.setrecursionlimit(20000)


# ====================== 1 =============================
def count_sum_1(a, b):
    if b == 0:
        return 0
    else:
        return a + count_sum_1(a / -2, b - 1)


# ====================== 2 =============================
def count_sum_2(b):
    sum_ = 1
    new_el = 1
    for _ in range(b - 1):
        new_el = new_el / -2
        sum_ += new_el
    return sum_


# ====================== 3 =============================
def count_sum_3(n):

    def fined_all_el(b):
        arr = [1]
        item = 1
        while b > 0:
            item = item / -2
            arr.append(item)
            b -= 1
        return arr

    all_el = fined_all_el(n-1)
    sum_ = 0

    for i in range(len(all_el)):
        sum_ += all_el[i]

    return sum_


print('** 1 **')
print(timeit.timeit('count_sum_1(1, 10)', number=1000, globals=globals()))  # 0.0016632389999999986
print(timeit.timeit('count_sum_1(1, 100)', number=1000, globals=globals()))  # 0.021267354999999998
print(timeit.timeit('count_sum_1(1, 1000)', number=1000, globals=globals()))  # 0.241307564
print(timeit.timeit('count_sum_1(1, 10000)', number=1000, globals=globals()))  # 2.839432576

print('** 2 **')
print(timeit.timeit('count_sum_2(10)', number=1000, globals=globals()))     # 0.0008139950000001228
print(timeit.timeit('count_sum_2(100)', number=1000, globals=globals()))     # 0.005642219000000281
print(timeit.timeit('count_sum_2(1000)', number=1000, globals=globals()))     # 0.06131200700000017
print(timeit.timeit('count_sum_2(10000)', number=1000, globals=globals()))     # 0.6435312239999997

print('** 3 **')
print(timeit.timeit('count_sum_3(10)', number=1000, globals=globals()))     # 0.0021003560000001364
print(timeit.timeit('count_sum_3(100)', number=1000, globals=globals()))     # 0.016635661999999662
print(timeit.timeit('count_sum_3(1000)', number=1000, globals=globals()))     # 0.1810263949999995
print(timeit.timeit('count_sum_3(10000)', number=1000, globals=globals()))     # 1.838122202


# Если брать N меньше, то в ответе сипрофайла будут одни нули.
cProfile.run('count_sum_1(1, 10000)')
cProfile.run('count_sum_2(10000)')
cProfile.run('count_sum_3(10000)')

'''
================= 1 =====================
         10004 function calls (4 primitive calls) in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
  10001/1    0.011    0.000    0.011    0.011 task_1.py:10(count_sum_1)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        
        
================= 2 =====================
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_1.py:18(count_sum_2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        


================= 3 =====================
         10005 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.001    0.001    0.003    0.003 task_1.py:28(count_sum_3)
        1    0.002    0.002    0.002    0.002 task_1.py:30(fined_all_el)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

'''
Вывод. 
Все написанные мною алгоритмы выглядят линейными. 
На маленьком N наиболее медленным вариантом решения является запись в массив элементов последовательности.
Но если количесвто элементов, которые собираемся складывать сделать значительно больше (200, 500, 800..), 
то проигрывать по времени начинает вариант с рекурсией. 
С учетом вышесказанного наиболее хорошим вариантом является вариант решения номер 2. 
'''