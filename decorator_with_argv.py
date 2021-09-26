
# Defining Decorator with argv
def string_lower(func):
    def wrapper(mystring):
        mystring = mystring.lower()
        
        return func(mystring)
    return wrapper
def make_list(func):
    def wrapper(mystring):
        mystring = list(mystring)
        return func(mystring)
    return wrapper



@string_lower
@make_list
def myprint(mystring):
    return mystring
mystring = "GANESH"
a = myprint(mystring)
print(a)
