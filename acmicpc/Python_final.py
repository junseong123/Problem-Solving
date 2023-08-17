def caculation(func):
    def wrapper(*args, **kwargs):
        print("계산을 시작하겠습니다!")
        return func(*args, **kwargs)
        print("계산을 끝내겠습니다!")
    return wrapper

@caculation 
def add(a, b):
    return a + b

@caculation
def minus(a, b):
    return a - b

@caculation
def multiply(a, b):
    return a * b

@caculation
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        

result_add = add(3, 5)
print(result_add)

result_minus = minus(3, 5)
print(result_minus)

result_multiply = multiply(3, 5)
print(result_multiply)

result_divide = divide(3, 5)
print(result_divide)