def map_new(doc):
    for word in doc:
        yield word, 1


def shuffle(mapped_values):
    dictionary = {}
    for word, count in mapped_values:
        if (word in dictionary):
            dictionary[word].append(count)
        else:
            dictionary[word] = [count]
    return dictionary


def reduce(word, values):
    yield word, sum(values)


lst = ['one', 'two', 'one', 'three', 'four']
shuffled_values = shuffle(list(map_new(lst)))
for word in shuffled_values:
    print(tuple(reduce(word, shuffled_values.get(word))))
