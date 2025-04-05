def num_words(text):
    # returns number of words in the string
    words = text.split()
    return len(words)


def letter_count(text):
    # returns the number of times each character appears (case-insensitive)
    l_words = text.lower()
    char_dict = {}

    for char in l_words:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_d(d):
    # return sorted list of dictionaries
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
