class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        answer = [0]*n
        for i in range(n):
            if boxes[i] == "1":
                for j in range(n):
                    answer[j] += abs(j - i)
        return answer