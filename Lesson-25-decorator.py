def greet(fun) :
    def wrapper(name) :
        print('Hello')
        fun(name)
        print('Good Job')
        
    return wrapper
@greet

def name(name) :
    print(name)
name('Khunn Satt Ko Ko')