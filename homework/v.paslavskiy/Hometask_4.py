def find_most_frequent(string):
    """
    This function is looking for most frequent words in piece of text
    :param string: here you should insert some text
    :return: most frequent words
    """
    characters = '.,:;\'"/?><!@#$$%^&*()_+-='
    wordcount = {}
    words = set()

    for word in string.lower().split():
        for a in characters:
            if a in word:
                word = word.replace(a, "")
            else:
                continue
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for c in wordcount.values():
        if c > 1:
            for i in wordcount:
                if wordcount[i] == c:
                    words.add(i)
    print(words)


find_most_frequent('Mom! Mom! Are you sleeping?!!! Why are you sleeping? I want to play with you')
