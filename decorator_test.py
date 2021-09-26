

# Defining Decorator
def string_lower(func):
    def wrapper():
        f = func()
        return f.lower()
    return wrapper
def make_list(func):
    def wrapper():
        f = func()
        return list(f)
    return wrapper


@make_list
@string_lower
def myprint():
    return "GANESH"
a = myprint()
print(a)
