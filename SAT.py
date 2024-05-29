def simplify_formula(formula, variable, value):
    new_formula = []
    for clause in formula:
        if value:  # variable is set to True
            if variable in clause:
                continue  # Clause is satisfied, remove it
            new_clause = [lit for lit in clause if lit != -variable]
        else:  # variable is set to False
            if -variable in clause:
                continue  # Clause is satisfied, remove it
            new_clause = [lit for lit in clause if lit != variable]

        if not new_clause and new_clause != clause:
            return None  # Clause becomes empty after simplification, unsatisfiable
        new_formula.append(new_clause)

    return new_formula


def backtrack(formula, variables, labeling, heuristic, debug):
    if debug:
        print(f"Backtracking with formula: {formula}, variables: {variables}, labeling: {labeling}")

    if not formula:
        return labeling  # Satisfiable
    if any(not clause for clause in formula):
        return None  # Unsatisfiable

    # HEURISTICS
    if heuristic:
        # Unit Propagation
        unit_clauses = [clause[0] for clause in formula if len(clause) == 1]
        for unit in unit_clauses:
            if debug:
                print(f"Unit propagation with unit clause: {unit}")
            if unit > 0:
                formula = simplify_formula(formula, unit, True)
                labeling[unit] = True
            else:
                formula = simplify_formula(formula, -unit, False)
                labeling[-unit] = False

            if formula is None:
                return None  # Conflict during unit propagation

            if abs(unit) in variables:
                variables.remove(abs(unit))

        if not variables:
            return labeling

    # CLASSIC SAT
    variable = variables[0]
    remaining_variables = variables[1:]

    # Try assigning True to the variable
    new_labeling = labeling.copy()
    new_labeling[variable] = True
    simplified_formula = simplify_formula(formula, variable, True)
    if debug:
        print(f"Trying variable {variable} = True, simplified formula: {simplified_formula}")
    if simplified_formula is not None:
        result = backtrack(simplified_formula, remaining_variables, new_labeling, heuristic, debug)
        if result is not None:
            return result

    # Try assigning False to the variable
    new_labeling[variable] = False
    simplified_formula = simplify_formula(formula, variable, False)
    if debug:
        print(f"Trying variable {variable} = False, simplified formula: {simplified_formula}")
    if simplified_formula is not None:
        result = backtrack(simplified_formula, remaining_variables, new_labeling, heuristic, debug)
        if result is not None:
            return result

    return None  # Unsatisfiable


def is_satisfiable(c, n, heuristic, debug):
    variables = list(range(1, n + 1))
    labeling = {}
    return backtrack(c, variables, labeling, heuristic, debug)
