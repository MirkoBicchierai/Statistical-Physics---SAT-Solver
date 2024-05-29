from Generation_CNF import generate_cnf
from SAT import is_satisfiable
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

debug = False
H = False


def probability_test(n_var, num_c, n_test, heuristic):
    x = []
    y = []
    time = []
    for m in num_c:
        ratio = m / n_var
        x.append(ratio)
        sum = 0
        t = 0
        for i in range(n_test):
            clauses = generate_cnf(n_var, m)
            start = timer()
            result = is_satisfiable(clauses, n_var, heuristic, debug)
            end = timer()
            t = t + (end - start)
            if result is not None:
                sum = sum + 1
        print("Analyzed N:", n_var, "Ratio:", ratio, "Time:", t / n_test)
        time.append(t / n_test)
        y.append((sum / n_test) * 100)
    return x, y, time


def satisfiability_plot(n_var, num_c, n_test, heuristic):
    x = []
    time = []
    results = []
    for m in num_c:
        ratio = m / n_var
        print(ratio)
        for i in range(n_test):
            clauses = generate_cnf(n_var, m)
            start = timer()
            result = is_satisfiable(clauses, n_var, heuristic, debug)
            end = timer()

            x.append(ratio)
            time.append(end - start)
            if result is not None:
                results.append(1)
            else:
                results.append(0)

    return x, time, results


if __name__ == "__main__":
    n_vars = [10, 20, 30, 40, 50]
    n_test = 300
    color = ['#440154', '#3b528b', '#21918c', '#5dc963', '#fde725']
    j = 0
    x_saved = []
    times_saved = []
    for var in n_vars:
        num_c = np.arange(var, (var * 9) + 1, int(var / 10))
        x, y, times = probability_test(var, num_c, n_test, H)
        times_saved.append(times)
        x_saved.append(x)
        plt.scatter(x, y, color=color[j], s=30, alpha=0.45, label="N = " + str(var))
        j = j + 1

    plt.title('Percent satisfiable')
    plt.xlabel('Ratio Test M/N')
    plt.ylabel('Percent satisfiable')
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 100)
    plt.xlim(1, 9)
    plt.xticks(range(1, 10, 1))
    if H:
        plt.savefig('output/plt_prob.png')
        plt.savefig('output/plt_prob.pdf')
    else:
        plt.savefig('output/plt_prob.png')
        plt.savefig('output/plt_prob.pdf')

    plt.close()

    j = 0
    for i in range(len(times_saved)):
        plt.scatter(x_saved[i], times_saved[i], color=color[j], s=30, alpha=0.45, label="N = " + str(n_vars[i]))
        j = j + 1

    plt.title('Mean times execution')
    plt.xlabel('Ratio Test M/N')
    plt.ylabel('Mean times execution')
    plt.grid(True)
    plt.legend()
    plt.xlim(1, 9)
    plt.xticks(range(1, 10, 1))
    if H:
        plt.savefig('output/plt_times.png')
        plt.savefig('output/plt_times.pdf')
    else:
        plt.savefig('output/plt_times.png')
        plt.savefig('output/plt_times.pdf')

    plt.close()

    x, y, c = satisfiability_plot(30, np.arange(30, (30 * 9) + 1, int(30 / 10)), 100, H)

    for i in range(len(x)):
        if c[i] == 1:
            plt.scatter(x[i], y[i], color="Blue", s=18, alpha=0.50)
        else:
            plt.scatter(x[i], y[i], color="Red", s=18, alpha=0.45)

    plt.xlabel('Ratio Test M/N')
    plt.ylabel('Mean times execution')
    plt.grid(True)
    plt.xlim(1, 9)
    plt.xticks(range(1, 10, 1))

    if H:
        plt.savefig('output/plt_sat_H.png')
        plt.savefig('output/plt_sat_H.pdf')
    else:
        plt.savefig('output/plt_sat.png')
        plt.savefig('output/plt_sat.pdf')