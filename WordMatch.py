def match_words(words):
    ctr = 0
    first = []
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr += 1
            first.append(word)
    print("List of words with 1st and last character same \n", first)
    return ctr
count = match_words(['elle', 'joy' , 'milk', 'anya', '1331' , '13'])
print("Number of words having 1st and last character same:",count)