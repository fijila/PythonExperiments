def outer(func):

    def inner():

        print("Accessing :",

                  func.__name__)

        return func()



    return inner



def greet():

    return 'Hello!'



greet = outer(greet) # decorating 'greet'



print(greet() ) # calling new 'greet'

