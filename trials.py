"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):

    return [num for num in nums if num % 2 == 0]


def get_odd_indices(items):
    
    return [items.index(idx) for idx in items if idx % 2 != 0]


def print_as_numbered_list(items):
    
    number = 1
    for item in items:
        print(f"{number}. {item}")
        number +=1

    print([f"{number}. {item}", number +=1 for item in items])
    
def get_range(start, stop):
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
