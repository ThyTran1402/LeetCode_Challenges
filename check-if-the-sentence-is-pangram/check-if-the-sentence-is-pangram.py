class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = len(sentence)
        sentence.lower()
        pangram = set()
        for ch in sentence:
            if ch not in pangram:
                pangram.add(ch)
        return len(pangram) == 26
                
                