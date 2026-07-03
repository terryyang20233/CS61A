
# function as an input: abstract stream first, implement later
# 复用，模块化
def improve(update, close, guess):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return  1 + 1/guess

def close_golden(guess):
    return approx(guess*guess, guess+1, 1e-15)

def approx(x,y,tolerance):
    return abs(x-y)<tolerance

# print(improve(golden_update, close_golden, 1))


# nested functions: Inherit variables, carry additional information
# 增加输入变量，灵活
def average(x,y):
    return (x+y)/2


def sqrt(a):
    def sqrt_update(x):
        return average(x, a / x)

    def sqrt_close(x):
        return approx(x*x,a, 1e-5)

    return improve(sqrt_update, sqrt_close,1)

# print(sqrt(17))


# function as an output, keep the inner function uncalled
# 分期付款，延迟参数传递
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update

def find_zero(f, df):
    def near_zero(x):
        return approx(f(x), 0)

    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)