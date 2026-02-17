class Solution:
    def length_of_longest_substring(self, text: str) -> int:
        max_length = 0
        window = []
        for char in text:
            if char in window:
                while window.pop(0) != char:
                    pass
            window.append(char)
            max_length = max(max_length, len(window))
        return max_length
