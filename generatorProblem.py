# https://www.youtube.com/watch?v=C3Z9lJXI6Qw problem solution

def sentenceGen(inputString: str):
    for word in inputString.split():
        yield word

for word in sentenceGen('how its going mom'):
    print(word)

mySentence = sentenceGen('this is test for generator')

print(next(mySentence))
print(next(mySentence))
print(next(mySentence))
print(next(mySentence))
print(next(mySentence))
print(next(mySentence))