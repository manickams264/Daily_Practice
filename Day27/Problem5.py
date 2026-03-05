class Solution:
    def findAnagrams(self, text: str, pattern: str) -> List[int]:
        result = []
        pattern_length = len(pattern)
        if len(text) < pattern_length:
            return result
        else:
            pattern = sorted(pattern)
            for start_index in range(len(text) - pattern_length + 1):
                substring = text[start_index:start_index + pattern_length]
                substring = sorted(substring)
                if substring == pattern:
                    result.append(start_index)
            return result
