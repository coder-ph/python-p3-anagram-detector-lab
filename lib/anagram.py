# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, mylist):
        sorted_list = []
        for myword in mylist:
            if sorted(myword) == sorted(self.word):
                sorted_list.append(myword)
        return sorted_list
            
           
        
        
        
    @property
    def word(self):
        return self._word   

    @word.setter
    def word(self, word):
        self._word = (word )
        

        
