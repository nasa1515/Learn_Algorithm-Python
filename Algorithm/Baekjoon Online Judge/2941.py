
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for x in a:
    word = word.replace(x, "0")
print(len(word))