# https://www.youtube.com/watch?v=C3Z9lJXI6Qw problem solution

class Sentence:
    
    def __init__(self,inputString):
        self.values = inputString.split()
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.values):
            raise StopIteration
        current = self.values[self.index]
        self.index += 1
        return current
    
mySentence = Sentence('hello mom how its going')

for word in mySentence:
    print(word)