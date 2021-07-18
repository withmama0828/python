import matplotlib.pyplot as plt
from functools import wraps
from random import uniform


#random.uniform(x, y)方法将随机生成一个实数，它在 [x,y] 范围内
def random(min, max, length):
    x = [uniform(min, max) for ii in range(length)]
    y = [uniform(min, max) for ii in range(length)]

    def decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            func(x, y)
        return wrap
    return decorator


@random(0, 5, 200)
def draw(x, y):
    plt.figure(figsize=(10, 10), dpi=60)
    plt.scatter(x, y, alpha=1.0)
    plt.show()


draw()