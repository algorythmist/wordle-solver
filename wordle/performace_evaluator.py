from heuristics import OneStepLookaheadSolver
from wordle_solver import evaluate_solver


def solver_accuracy():
    trials = 100
    success_rate, average_score, stdev = evaluate_solver('wordle_dict.txt', trials,
                                                  lambda scorer: OneStepLookaheadSolver(scorer))
    print(f'\nSuccess rate = {success_rate:.2}')
    print(f'Average Score = {average_score}')
    print(f'Standard deviation = {stdev}')


def solver_accuracy_large_dict():
    trials = 500
    success_rate, average_score, stdev = evaluate_solver('full_dict.txt', trials,
                                                  lambda scorer: OneStepLookaheadSolver(scorer,
                                                                                        threshold=300,
                                                                                        max_sample_size=1000))
    print(f'\nSuccess rate = {success_rate:.2}')
    print(f'Average Score = {average_score}')
    print(f'Standard deviation = {stdev}')


if __name__ == '__main__':
    # solver_accuracy()
    # Success rate = 0.99
    # Average Score = 3.524193548387097
    # Standard deviation = 0.7455644070901363

    solver_accuracy_large_dict()
    # Success rate = 0.93
    # Average Score = 4.41036717062635
    # Standard deviation = 0.9524666596558226

    # Success rate = 0.93
    # Average Score = 4.398286937901499
    # Standard deviation = 0.8754547665571433
