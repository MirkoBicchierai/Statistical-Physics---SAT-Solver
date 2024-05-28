from Generation_CNF import generate_cnf
from SAT import is_satisfiable
import numpy as np
import math

debug = False


def probability_test(n_var, num_c):
    for m in num_c:
        ratio = m / n_var
        print(ratio)
        clauses = generate_cnf(n_var, m)
        result = is_satisfiable(clauses, n_var, debug)
        if result is not None:
            print("Satisfiable with assignment:", result)
        else:
            print("Not satisfiable")


if __name__ == "__main__":
    n_vars = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    for var in n_vars:
        num_c = np.arange(var, var * 8 + 1, 1)
        print(num_c)
        probability_test(var, num_c)
