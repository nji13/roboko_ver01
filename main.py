# import os
import collections

x = 'lesson_package/talk'
y = '__pycache__'

z = ['/abc', '/def', 'ghi']

p = [test.replace('/', '') for test in z]

num = [1, 2, 3, 4, 5]

h = collections.defaultdict(str)

for key in z:
    h[key] += '2'

print(h)

# print(os.path.join(*p))

# for name, count in h.items():
#     print(name, count)


# def t():
#     for i in range(10):
#         yield i


# for i in t():
#     print(i)
