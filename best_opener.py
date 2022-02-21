import multiprocessing as mp
from dictionary import read_dictionary
from wordle_solver import evaluate_solver, BruteForceSolver

def evaluate_opener(opener: str):
    success_rate, average_score = evaluate_solver('wordle_dict.txt', 500,
                                                  lambda scorer: BruteForceSolver(scorer=scorer,
                                                                                  opener=opener))
    return opener, average_score, success_rate


def find_best_openers():
    """
    Read the entire dictionary and simulate every opening.
    Retain only the words that score below 4 and store them
    """
    openers = read_dictionary()

    with mp.get_context("spawn").Pool(16) as pool:
        results = pool.map(evaluate_opener, [opener for opener in openers])

    results = [result for result in results if result[1] < 3.9 and result[2] > 0.98]
    results = sorted(results, key=lambda x: x[1])
    results = [f'{result[0]},{result[1]},{result[2]}\n' for result in results]

    with open("best_openers.txt", "w") as f:
        f.writelines(results)


if __name__ == '__main__':

    find_best_openers()
