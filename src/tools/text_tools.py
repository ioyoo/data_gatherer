def find_in_text(word, text):
    list = text.lower().strip().split()
    return word.lower() in list  # in [w.lower() for w in list]
