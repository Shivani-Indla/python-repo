# def sample_func():
#     print("This is a sample function")
# # calling this function as bellow
# sample_func()

#Use cases

def add(a, b, c=3):
    """
        this function is adding a,b,c. "we can get this info in help(add)"
    """
    res = a + b + c
    return res
#calling the function
result = add(a=1, b=2)
print(result)
help(add)
