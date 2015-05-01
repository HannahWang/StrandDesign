class RNA:
    
    basecoplement = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    
    def __init__(self, s):
        self.seq = s

    def transcribe(self):
        return self.seq.replace('U', 'T')

    def reverse(self):
        letters = list(self.seq)
	letters.reverse() 
	return ''.join(letters)

    def complement(self): 
        letters = list(self.seq) 
	letters = [self.basecomplement[base] for base in letters]
	return ''.join(letters)
    
    def reversecomplement(self):
        letters = list(self.seq)
	letters.reverse()
	letters = [self.basecomplement[base] for base in letters] 
	return ''.join(letters)

    def gc(self):
        s = self.seq
	gc = s.count('G') + s.count('C') 
	return gc * 100.0 / len(s) 

    def codons(self): 
        s = self.seq 
        end = len(s) - (len(s) % 3) - 1 
        codons = [s[i:i+3] for i in range(0, end, 3)] 
	return codons 
