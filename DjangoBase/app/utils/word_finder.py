L = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
M = ['lslikrsjalbc', 'bupceepcikye','labhgcegthaw','ghvuqkvylwvp','qjjjzgodkahg','fmdvdqrzleky',
     'qsheccfcrdgxb','niprfeudenhl','sojkgrefdfsf','fsefnrbtuksj']

class WordFinder:
    def __init__(self, L):
        self.L = L

    def longest_word(self, word):
        # crear un diccionario con la frecuencia de cada letra de la palabra
        word_freq = {}
        for letter in word:
            if letter in word_freq:
                word_freq[letter] += 1
            else:
                word_freq[letter] = 1
        
        # recorrer la lista de palabras y encontrar la más larga que se pueda formar con las letras de word
        longest = ''
        for w in self.L:
            # crear un diccionario con la frecuencia de cada letra de la palabra w
            w_freq = {}
            for letter in w:
                if letter in w_freq:
                    w_freq[letter] += 1
                else:
                    w_freq[letter] = 1
            
            # verificar si se puede formar la palabra w con las letras de word
            can_form_word = True
            for letter in w_freq:
                if letter not in word_freq or w_freq[letter] > word_freq[letter]:
                    can_form_word = False
                    break
            
            # actualizar la palabra más larga si es necesario
            if can_form_word and len(w) > len(longest):
                longest = w
        
        return longest
    
finder = WordFinder(M)
longest = finder.longest_word('asbupkyeqw')
print(longest)