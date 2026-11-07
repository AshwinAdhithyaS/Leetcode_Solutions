class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def ship_can(cap):
            day_coun,load=1,0
            for w in weights:
                if load+w>cap:
                    load=0
                    day_coun+=1
                load+=w
            return day_coun<=days
        
        lo,hi=max(weights),sum(weights)
        while lo<hi:
            mid=(lo+hi)//2
            if ship_can(mid):
                hi=mid
            else:
                lo=mid+1
        return lo