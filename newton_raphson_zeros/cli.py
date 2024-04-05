"""CLI interface for newton_raphson_zeros project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import sympy as sp


def newton_raphson_algorithm(func, func_prime, x0, tol=1e-6, max_iter=100):
    # print table header: n, xn, f(xn), f'(xn) and xn - f(xn)/f'(xn)
    print("n\t\txn\t\t\t\tf(xn)\t\t\t\tf'(xn)\t\t\t\txn - f(xn)/f'(xn)")
    x = x0
    for i in range(max_iter):
        print(f"{i}\t\t{x}\t\t{func.subs('x', x)}\t\t{func_prime.subs('x', x)}\t\t{x - func.subs('x', x) / func_prime.subs('x', x)}")
        x = x - func.subs('x', x) / func_prime.subs('x', x)
        if abs(func.subs('x', x)) < tol:
            return x, i
    return None

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m newton_raphson_zeros` and `$ newton_raphson_zeros `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    # Define the symbol
    x = sp.symbols('x')

    # Get user input for f(x)
    func_str = input("Enter f(x): ")

    # Get user input for f'(x)
    func_prime_str = input("Enter f'(x): ")

    # Get user input for initial guess of the root
    x0 = float(input("Enter the initial guess of the root: "))

    # Convert string to SymPy expression
    func = sp.sympify(func_str)
    func_prime = sp.sympify(func_prime_str)

    # Define the Newton-Raphson method and find the root and number of iterations
    root, num_iter = newton_raphson_algorithm(func, func_prime, x0)
    
    # Print the initial guess, root and number of iterations
    print(f"Initial guess: {x0}")
    print(f"Root: {root}")
    print(f"Number of iterations: {num_iter}")
