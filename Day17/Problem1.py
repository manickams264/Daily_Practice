from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)   
        left_pointer = 0                 
        for right_pointer in range(len(fruits)):
            fruit_count[fruits[right_pointer]] += 1
            if len(fruit_count) > 2:
                fruit_count[fruits[left_pointer]] -= 1
                if fruit_count[fruits[left_pointer]] == 0:
                    del fruit_count[fruits[left_pointer]]
                left_pointer += 1
        return right_pointer - left_pointer + 1
