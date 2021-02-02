text = (("Hi", "Steve!"), ("What's", "up?"))

list_of_words = []
for sentence in text:
    print(sentence)
    for word in sentence:
        list_of_words.append(word)


print(list_of_words)

# or

text = (("Hi", "Steve!"), ("What's", "up?"))

print([word for sentence in text for word in sentence])

# [x for y in collection for x in y]

# Same as

"""
for y in collection:     #      for B in C:
    for x in y:          #          for D in E: (in this case: for A in B)
        # receive x      #              # receive A
"""

