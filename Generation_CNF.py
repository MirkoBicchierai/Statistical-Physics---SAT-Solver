import random


def generate_cnf(nv, nc):
    cnf = []
    for _ in range(nc):
        clause_size = 3  # 3 SAT come dal paper
        clause = set()
        literals = []
        while len(clause) < clause_size:

            while True:
                literal = random.randint(1, nv)
                if not (literal in literals):
                    literals.append(literal)
                    break

            if random.choice([True, False]):
                literal = -literal
            clause.add(literal)
        cnf.append(list(clause))
    return cnf
