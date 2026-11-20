class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char = list(s)
        n = len(s)
        for i in range(0, len(s), 2 * k):
            if n < k:
                char[i:] = char[i:][::-1]
            elif n < 2 * k and n >= k:             
                char[i:i+k] = char[i:i+k][::-1]
            else:
                char[i:i+k] = char[i:i+k][::-1]
            n -= 2 * k                           
        return ''.join(char)
