__all__ = [
  'central_derivative',
  'backward_derivative',
  'forward_derivative',
  'richard_extrapolation',
  'second_derivative'
]

def central_derivative(f, x, delta):
    return (f(x + delta) - f(x - delta)) / (2 * delta)


def backward_derivative(f, x, delta):
    return (f(x) - f(x - delta)) / delta


def forward_derivative(f, x, delta):
    return (f(x + delta) - f(x)) / delta


def richard_extrapolation(f, x, delta, p, derivation_function=forward_derivative):
    d1 = derivation_function(f, x, delta)
    q = 2
    d2 = derivation_function(f, x, delta / q)

    return d1 + (d1 - d2) / (q**p - 1)


def second_derivative(f, x, delta, derivation_function=forward_derivative):
    return derivation_function(lambda y: derivation_function(f, y, delta), x, delta)
