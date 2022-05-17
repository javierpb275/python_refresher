def hello():
    print("Hello!")

hello()

# *args **kwargs

def super_func(*args, **kwargs):
    print(args)  # (1, 2, 3, 4, 5)
    print(*args)  # 1 2 3 4 5
    total = 0
    print(kwargs)  # {'num1': 6, 'num2': 7}
    for item in kwargs.values():
        total += item
    return sum(args) + total  # 28


# args: 1, 2... 5; kwargs: 6, 7
total = super_func(1, 2, 3, 4, 5, num1=6, num2=7)

print(total)  # 28


# Rule: params, *args, default parameters, **kwargs
def super_func_2(name, *args, i='hi', **kwargs):
    pass


super_func_2('pepe', 1, 2, 3, 4, 5, num1=6, num2=7)


def add(x, y):
    return x + y


print(add(1, 2))

print('-------------------------------------')

lambda_func = lambda x, y: x + y
print(lambda_func(2, 2))

print((lambda x, y: x + y)(5, 5))

sequence_lambda = [1, 2, 3]

doubled_lambda = [(lambda x: x * 2)(x) for x in sequence_lambda]
doubled_2_lambda = map(lambda x: x * 2, sequence_lambda)

print(doubled_lambda)
print(list(doubled_2_lambda))

print('------------------------------------')


def double(x):
    return x * 2


sequence = [1, 2, 3]
doubled = [double(x) for x in sequence]
doubled_2 = map(double, sequence)
print(doubled)
print(list(doubled_2))