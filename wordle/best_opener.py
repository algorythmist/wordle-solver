import multiprocessing as mp

from wordle.dictionary import read_dictionary
from wordle.performace_evaluator import evaluate_solver
from wordle.wordle_solver import NaiveSolver


def find_best_openers():
    """
    Read the entire dictionary and simulate every opening.
    Retain only the words that score below 4 and store them
    """

    def evaluate_opener(opener: str):
        success_rate, average_score = \
            evaluate_solver(dictionary_filename='wordle_dict.txt',
                            trials=1000,
                            solver_factory=lambda scorer: NaiveSolver(opener=opener))
        return opener, average_score, success_rate

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
