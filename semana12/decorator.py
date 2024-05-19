from functools import wraps


def my_decorator(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la funcion")
        result = funct(*args, **kwargs)
        print(result.upper())
        print("Despues de llamar a la funcion")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Funcion para saludar a alguien"""
    return (f"Hola, {name}!")

greet("Gustavo")

print(greet.__name__)
print(greet.__doc__)