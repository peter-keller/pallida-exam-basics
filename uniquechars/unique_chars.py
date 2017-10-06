# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases


def unique_characters(word):
    letter_list = list(word)
    new_list = []
    for i in range(len(letter_list)):
        for letter in word:
            if letter[i] not in new_list:
                new_list.append(letter[i])
                return new_list


print(unique_characters("anagram"))