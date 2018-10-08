"""
    Write a program that lets the user enter a string and displays the letter that appears
    most frequently in the string. Ignore spaces, punctuation, and uppercase vs lowercase.
"""
alphabet = tuple(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z'])

"""
    Ask's user to write a sentence. Calls count_letters and finds the letter which occurred the most in the sentence.
"""


def main():
    sentence = input("Please enter a sentence: ").lower()
    letter_list = count_letters(sentence)
    maximum = max(letter_list)
    letter_index = letter_list.index(maximum)
    print("The letter " + alphabet[letter_index].upper() + " occurred a total of " + str(maximum) + " times.")


"""
    Counts each letter in a sentence, returns a list for the total number of occurrences per letter.
"""


def count_letters(sentence):
    letters_occur = [0] * len(alphabet)
    for letter in sentence:
        if letter in alphabet:
            index = alphabet.index(letter)
            letters_occur[index] += 1
    return letters_occur


main()
