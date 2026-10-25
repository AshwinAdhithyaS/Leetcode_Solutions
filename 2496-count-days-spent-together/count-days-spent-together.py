class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months=[0,31,59,90,120,151,181,212,243,273,304,334]
        def days_find(dat):
            mon,day=int(dat[:2]),int(dat[3:])
            return months[mon-1]+day
        st=max(days_find(arriveAlice),days_find(arriveBob))
        en=min(days_find(leaveAlice),days_find(leaveBob))
        return max(0,en-st+1)