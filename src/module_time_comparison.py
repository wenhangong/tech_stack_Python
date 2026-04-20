import timeit

# 测试 import random
setup1 = "import random"
code1 = "random.random()"
time1 = timeit.timeit(stmt=code1, setup=setup1, number=10000000)

# 测试 from random import random
setup2 = "from random import random"
code2 = "random()"
time2 = timeit.timeit(stmt=code2, setup=setup2, number=10000000)

print(f"import random 耗时: {time1:.4f} 秒")
print(f"from ... import 耗时: {time2:.4f} 秒")