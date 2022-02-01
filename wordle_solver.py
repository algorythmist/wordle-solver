import random


def random_word(dictionary):
    return dictionary[random.randrange(0, len(dictionary))]


def score_guess(secret_word: str, guess: str) -> list:
    score = [-1 for _ in range(0, len(guess))]
    for i in range(0, len(guess)):
        if secret_word[i] == guess[i]:
            score[i] = 1
        elif guess[i] in secret_word:
            score[i] = 0
    return score


def filter_word(word: str, score: list, guess: str) -> bool:
    for i in range(0, len(score)):
        if score[i] == -1 and guess[i] in word:
            return False
        if score[i] == 0 and (not (guess[i] in word) or guess[i] == word[i]):
            return False
        if score[i] == 1 and not (guess[i] == word[i]):
            return False
    return True


def filter_dictionary(dictionary: list, score: list, guess: str) -> bool:
    return [w for w in dictionary if filter_word(w, score, guess)]


def is_solved(score: list) -> bool:
    return sum(score) == len(score)


def solve(secret_word, five_letter_words):
    words_remaining = five_letter_words
    for i in range(6):
        guess = random_word(words_remaining)
        print('guess: ' + guess)

        score = score_guess(secret_word, guess)
        print(f'Score = {score}')
        if is_solved(score):
            print("FOUND IT!")
            break
        words_remaining = filter_dictionary(words_remaining, score, guess)
    return guess, i


def read_dictionary(filename='words_alpha.txt', word_length=5):
    file = open(filename, 'r')
    words = file.readlines()
    specific_words = [w.strip().upper() for w in words if len(w.strip()) == word_length]
    print(len(specific_words))
    return specific_words


if __name__ == '__main__':
    five_letter_words = read_dictionary()
    secret_word = random_word(five_letter_words)
    print("secret word: " + secret_word)
    guess, iterations = solve(secret_word, five_letter_words)
    print(f'Found the solution {guess} in {iterations} iterations')



