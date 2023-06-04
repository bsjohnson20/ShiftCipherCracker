

# reader to check if a word is in english_words.txt file
def read_file(word):
    with open('english_words.txt') as f:
        for row in f:
            # compare the word with the word in the file
            if row.strip() == word:
                return True
    return False

# function to go through every word in an input string and use the read_file function to check if it is a word
def check_words(input_string):
    # split the string into a list of words
    words = input_string.split()
    # create an empty list to store the words that are not in the file
    # also create an empty list to store the words that are in the file
    not_words = []
    valid_words = []
    # go through every word in the list
    for word in words:
        # if the word is not in the file, add it to the not_words list
        if not read_file(word.lower()):
            not_words.append(word.lower())
        # else add it to the valid words list:
        else:
            valid_words.append(word.lower())
    # return the list of words that are not in the file
    return not_words, valid_words


# shift cipher function
# takes a string and a shift number and shifts it forward by that amount
def shift_cipher(input_string, shift=1):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_string = ''
    for i in input_string.lower():
        if not i.isnumeric() and not i.isspace():
            pos = letters.index(i)
            # if pos is greater than 26 // it by 26.
            # print(f"Pos: {pos}"
            #      f"Pos%26: {pos%26}")
            new_string += letters[((pos+shift)%26)]

        else:
            new_string += i
    print(f"New string {new_string}")
    return new_string






# main function to get user input, call the check_words function, and print the results
def main():
    # get user input
    input_string = input("Enter a string: ")

    shift = 0
    iterations = 0
    valid_words = 'a'
    print("running")
    print((len(valid_words)/len(input_string.split(' '))*100) < 50)
    while ((len(''.join(valid_words))/len(input_string))) < 0.5 and iterations < 30:

        new_string = shift_cipher(input_string, shift)
        shift += 1; iterations += 1
        # call the check_words function
        not_words, valid_words = check_words(new_string)
        print(not_words, valid_words)
        percent = len(valid_words)/len(input_string)
        if percent > 0.5:
            print(f"Found something with greater than 50% accuracy:\n\n{new_string}")
        else:
            print(f"Iteration: {iterations}, current shift: {shift}")
            print(f"not words: {not_words},\n valid words: {valid_words}")
            print(f"\nPercent equals: {len(''.join(valid_words))/len(input_string)*100}\n")
            print(f"len valid words {len(''.join(valid_words))}\nlen total string {len(input_string)}")
            print("\n\n")



main()

# call the main function
#print(shift_cipher("ZNK IGZ PASVKJ UBKX ZNK XGHHOZ",-32))

