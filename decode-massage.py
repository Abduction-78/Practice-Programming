#Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven

massage = 'Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven'

word = massage.split(' ')

dictionary = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5', 'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9', 'Zero': '0', 'Dash': '-'}

output = []

for w in word:
    if w in dictionary:
        output.append(dictionary[w])
    else:
        output.append(w[0])

final = ''.join(output)
print(final)


#other-way

for w in word:
    print(dictionary.get(w, w[0]), end='')

print()