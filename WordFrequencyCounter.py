# Write a program that:

# Asks the user to input a sentence.

# Splits the sentence into words.

# Counts how many times each word appears.

# Displays the results in a neat format.

# 
def get_sentence():
    return input("Enter a sentence: ")
def count_word_frequencies(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
def display_word_frequencies(word_count):
    print("\nWord Frequencies:")
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")
def main():
    sentence = get_sentence()
    word_count = count_word_frequencies(sentence)
    display_word_frequencies(word_count)
if __name__ == "__main__":
    main()
