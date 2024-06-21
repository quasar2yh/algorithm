import time
# ValueError: Exceeds the limit (4300) for integer string conversion
import sys
sys.set_int_max_str_digits(0)
# RecursionError: maximum recursion depth exceeded
sys.setrecursionlimit(5000000)


def recursive_fibonacci(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)


def iter_fibonacci(num):
    fibo1, fibo2 = 1, 1
    if num < 3:
        fibo = 1
        return fibo
    while num >= 3:
        fibo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo
        num -= 1
    return fibo


start = time.time()
fibo_num = 40
answer = recursive_fibonacci(fibo_num)
print(f'{fibo_num}번째 피보나치 수는 {answer} 입니다.')  # 40번째 피보나치 수는 102334155 입니다
print(f'소요시간 : {(time.time() - start):.2f}')  # 소요시간 : 13.63


start = time.time()
fibo_num = 40
answer = iter_fibonacci(fibo_num)
print(f'{fibo_num}번째 피보나치 수는 {answer} 입니다.')  # 40번째 피보나치 수는 102334155 입니다
print(f'소요시간 : {(time.time() - start):.2f}')  # 소요시간 : 0.00




# print(recursive_fibonacci(10))

# 피보나치 수열 [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377...]


# def fibonacci(fibonacci_number):
#     if fibonacci_number == 0:
#         print("0으로 끝!")
#         return 0
#     elif fibonacci_number == 1:
#         print("1로 끝!")
#         return 1
#     else:
#         print(f'factorial_number: {fibonacci_number}')
#         result = fibonacci(fibonacci_number - 1) + fibonacci(fibonacci_number - 2)
#         print("result:", result)
#         return result
