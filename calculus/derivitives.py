def limit_derivative(f,x,h):
    return (f(x+h) - f(x)) / h
def derivative(f,x,h=1e-5):
    return limit_derivative(f,x,h)
