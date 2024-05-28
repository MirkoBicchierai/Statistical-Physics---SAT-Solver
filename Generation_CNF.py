import random


def generate_cnf(nv, nc):
    cnf = []
    for _ in range(nc):
        clause_size = 3  # 3 SAT come dal paper
        clause = set()
        while len(clause) < clause_size:
            literal = random.randint(1, nv)
            if random.choice([True, False]):
                literal = -literal
            clause.add(literal)
        cnf.append(list(clause))
    return cnf
