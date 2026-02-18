class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for index1 in range(len(startTime)):
            for index2 in range(startTime[index1],endTime[index1]+1):
                if index2==queryTime:
                    count+=1
        return count
        