class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        histogram = {}

        for word in strs:

            sorted_word = "".join(sorted(word))
            

            if sorted_word not in histogram:
                histogram[sorted_word] = []
            histogram[sorted_word].append(word)

        return list(histogram.values())