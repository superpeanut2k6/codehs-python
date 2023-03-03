def count_occurrences(word, character):
    count = 0
    for char in word:
        if (char == character):
            count+=1
    return count  
print (count_occurrences("banana", "a"))
