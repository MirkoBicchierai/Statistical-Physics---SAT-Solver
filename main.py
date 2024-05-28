from Generation_CNF import generate_cnf
from SAT import is_satisfiable
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

debug = False


def probability_test(n_var, num_c, n_test):
    x = []
    y = []
    time = []
    for m in num_c:
        ratio = m / n_var
        x.append(ratio)
        print(ratio)
        sum = 0
        t = 0
        for i in range(n_test):
            clauses = generate_cnf(n_var, m)
            start = timer()
            result = is_satisfiable(clauses, n_var, debug)
            end = timer()
            t = t + (end - start)
            if result is not None:
                sum = sum + 1
                # print("Satisfiable with assignment:", result)
        time.append(t / n_test)
        y.append((sum / n_test) * 100)
    return x, y, time


if __name__ == "__main__":
    n_vars = [10, 20, 30]  # 10, 20 , 30, 40, 50
    n_test = 50
    color = ['#440154', '#3b528b', '#21918c', '#5dc963', '#fde725']
    j = 0
    x_saved = []
    times_saved = []
    for var in n_vars:
        num_c = np.arange(var, var * 10 + 1, 1)
        x, y, times = probability_test(var, num_c, n_test)
        times_saved.append(times)
        x_saved.append(x)
        plt.scatter(x, y, color=color[j], s=35, alpha=0.4, label="N = " + str(var))
        j = j + 1

    plt.title('Percent satisfiable')
    plt.xlabel('Ratio Test M/N')
    plt.ylabel('Percent satisfiable')
    plt.grid(True)
    plt.legend()
    plt.savefig('output/plt_prob.png')

    plt.close()

    j = 0
    for i in range(len(times_saved)):
        plt.scatter(x_saved[i], times_saved[i], color=color[j], s=35, alpha=0.4, label="N = " + str(n_vars[i]))
        j = j + 1

    plt.title('Mean times execution')
    plt.xlabel('Ratio Test M/N')
    plt.ylabel('Mean times execution')
    plt.grid(True)
    plt.legend()
    plt.savefig('output/plt_times.png')
