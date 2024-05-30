from Generation_CNF import generate_cnf
from SAT import is_satisfiable
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer


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

    debug = False
    H = False

    if H:
        n_vars = [10, 20, 30, 40, 50]
        n_test = 300
        test_var = 50
    else:
        n_vars = [10, 20, 30, 40]
        n_test = 100
        test_var = 40

    color = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

    point_x_ratio = 50

    prob_plot = False
    satis_plot = True

    if prob_plot:
        j = 0
        x_saved = []
        times_saved = []
        for var in n_vars:
            num_c = np.arange(var, (var * 9) + 1, int(var / 10))
            x, y, times = probability_test(var, num_c, n_test, H)
            times_saved.append(times)
            x_saved.append(x)
            plt.scatter(x, y, color=color[j], s=25, alpha=0.5, label="N = " + str(var))
            j = j + 1

        if H:
            plt.title('Percent satisfiable with Heuristic')
        else:
            plt.title('Percent satisfiable without Heuristic')

        plt.xlabel('Ratio Test M/N')
        plt.ylabel('Percent satisfiable')
        plt.grid(True)
        plt.legend()
        plt.ylim(0, 100)
        plt.xlim(1, 9)
        plt.xticks(range(1, 10, 1))
        if H:
            plt.savefig('output/plt_prob_H.png')
            plt.savefig('output/plt_prob_H.pdf')
        else:
            plt.savefig('output/plt_prob.png')
            plt.savefig('output/plt_prob.pdf')

        plt.close()

        j = 0
        for i in range(len(times_saved)):
            plt.scatter(x_saved[i], times_saved[i], color=color[j], s=25, alpha=0.5, label="N = " + str(n_vars[i]))
            j = j + 1

        if H:
            plt.title('Mean execution times with Heuristic')
        else:
            plt.title('Mean execution times without Heuristic')

        plt.xlabel('Ratio Test M/N')
        plt.ylabel('Mean execution times')
        plt.grid(True)
        plt.legend()
        plt.xlim(1, 9)
        plt.xticks(range(1, 10, 1))
        if H:
            plt.savefig('output/plt_times_H.png')
            plt.savefig('output/plt_times_H.pdf')
        else:
            plt.savefig('output/plt_times.png')
            plt.savefig('output/plt_times.pdf')

        plt.close()

    if satis_plot:

        x, y, c = satisfiability_plot(test_var, np.arange(test_var, (test_var * 9) + 1, int(test_var / 10)),
                                      point_x_ratio, H)

        for i in range(len(x)):
            if c[i] == 1:
                plt.scatter(x[i], y[i], color="royalblue", s=18, alpha=0.60)
            else:
                plt.scatter(x[i], y[i], color="orangered", s=18, alpha=0.60)

        if H:
            plt.title('Execution time N = ' + str(test_var) + " with Heuristic")
        else:
            plt.title('Execution time N = ' + str(test_var) + " without Heuristic")

        plt.xlabel('Ratio Test M/N')
        plt.ylabel('Execution time')
        plt.grid(True)
        plt.xlim(1, 9)
        plt.xticks(range(1, 10, 1))

        if H:
            plt.savefig('output/plt_sat_H.png')
            plt.savefig('output/plt_sat_H.pdf')
        else:
            plt.savefig('output/plt_sat.png')
            plt.savefig('output/plt_sat.pdf')
