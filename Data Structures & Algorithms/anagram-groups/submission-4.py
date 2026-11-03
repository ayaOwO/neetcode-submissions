class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        
        for word in strs:
            freq = [0] *26
            for char in word:
                freq[ord(char)%26] += 1
            mem[str(freq)].append(word)

        return list(mem.values())
                
        