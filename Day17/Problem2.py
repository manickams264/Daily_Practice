class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        string_length = len(s)
        for ascii_code in range(ord('A'), ord('Z') + 1):
            target_char = chr(ascii_code)
            left_pointer = 0
            right_pointer = 0
            replacements_used = 0
            while right_pointer < string_length:
                if s[right_pointer] == target_char:
                    right_pointer += 1
                elif replacements_used < k:
                    right_pointer += 1
                    replacements_used += 1
                elif s[left_pointer] == target_char:
                    left_pointer += 1
                else:
                    left_pointer += 1
                    replacements_used -= 1
                max_length = max(max_length, right_pointer - left_pointer)
        return max_length
