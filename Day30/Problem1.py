from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preference_count = [0, 0]
        for student in students:
            preference_count[student] += 1
        for sandwich in sandwiches:
            if preference_count[sandwich] == 0:
                break
            preference_count[sandwich] -= 1
        return preference_count[0] + preference_count[1]
