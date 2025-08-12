# #1
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return a[::-1]
#     return wrapper

# @decorator
# def teskari():
#     return('Salom python')

# print(teskari())


# #2
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return a.replace(" ", "")
#     return wrapper

# @decorator
# def matn():
#     return "wlecome to Tashkent"

# print(matn())


# #3
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).lower()
#     return wrapper

# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, *kwargs) + '***'
#     return wrapper

# @decorator
# @decorator2
# def matn():
#     return "WelCoME To TAshKent bro"

# print(matn())


# #4
# def decorator(*args): 
#     a =1   
#     for i in args:
#          a *= i
#     return a
# print(decorator(2, 4, 5, 6 ))   


# #5
# def decorator(func):
#     def wrapper(*args):
#         for i in args:
#             if i %2 == 0:
#                 return "toq son kiriting"
#         return func(*args)
#     return wrapper

# @decorator
# def test(*args):
#     return sum([i for i in args])

# print(test(5, 1, 2, 7))


# #6
# def max_min(sonlar):
#     return f"kattasi={max(sonlar)}, kichigi={min(sonlar)}"

# print(max_min([2, 5, 6, 4, 8]))


# #7
# def aski():
#     for i in range(65, 90+1):
#         print(chr(i), i)

# aski()


# #9
# def sonlar(a):
#     number = []
#     for i in a:
#         if i > 0  and i %2 == 0:
#             number.append(i)
#     return number
        
# print(sonlar([2, 4, 3, 6, 7, 9, 8, -2 ,-5, -8]))


#10
import time

start = time.perf_counter()
def decorator(func):
    x = []
    def wrapper(*args):
        start = time.perf_counter()
        for i in args:
            if i > 0:
                x.append(i)
        return func(*x)
    return wrapper
end = time.perf_counter()

print(end-start)
@decorator
def test(*args):
    return sum(args)
print(test(2, 3, -2, -6, 8))
