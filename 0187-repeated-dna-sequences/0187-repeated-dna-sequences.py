class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seen_sequences = {}
        
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            seen_sequences[substring] = seen_sequences.get(substring, 0) + 1
        
        return [k for k, v in seen_sequences.items() if v > 1]