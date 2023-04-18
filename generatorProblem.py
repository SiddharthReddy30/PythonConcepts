# https://www.youtube.com/watch?v=C3Z9lJXI6Qw problem solution

def sentenceGen(inputString: str):
    words :list[str] = inputString.split()
    index = 0
    while index < len(words):
        yield words[index]
        index +=1
        
for word in sentenceGen('how its going mom'):
    print(word)