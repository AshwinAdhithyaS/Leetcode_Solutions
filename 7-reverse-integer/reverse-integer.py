class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        if x>=1:
            xs=str(x)
            xs=xs[::-1]
            if 0 <= int(xs) <= ((2**31)-1):
                if xs[0]=='0':
                    while xs[0]=='0':
                        xs=xs[1:]
                    return int(xs)
                else:
                    return int(xs)
            else:
                return 0
        else:
            xs=str(x)
            xs=xs[1:]
            xs=xs[::-1]
            if 0 <= int(xs) <= (2**31):
                if xs[0]=='0':
                    while xs[0]=='0':
                        xs=xs[1:]
                    return int(xs)-(int(xs)*2)
                else:
                    return int(xs)-(int(xs)*2)
            else:
                return 0