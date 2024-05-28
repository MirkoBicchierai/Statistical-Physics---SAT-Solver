from Generation_CNF import generate_cnf
from SAT import is_satisfiable

if __name__ == "__main__":

    # Example CNF: (x1 or ~x2 or x3) and (~x1 or x2 or x3) and (~x3 or ~x2 or ~x1)
    # clauses = [
    #     [1, -2, 3],
    #     [-1, 2, 3],
    #     [-3, -2, -1],
    # ]
    # num_vars = 3  # Number of variables: x1, x2, x3

    n = 5
    m = 50
    clauses = generate_cnf(n, m)
    print("------------------------------------------------------------------------")
    print("Generated clauses", clauses)
    print("------------------------------------------------------------------------")
    result = is_satisfiable(clauses, n)
    print("------------------------------------------------------------------------")

    if result is not None:
        print("Satisfiable with assignment:", result)
    else:
        print("Not satisfiable")
