def count_ocurrences(path, word):
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count


path = "src/jobs.csv"
word = "Python"

print(count_ocurrences(path, word))
