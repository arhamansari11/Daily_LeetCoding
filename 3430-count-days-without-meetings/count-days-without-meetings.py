class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count=0
        prev_end=0 
        for start,end in meetings:
            if start>prev_end+1:
                count+=start-prev_end-1
            prev_end=max(prev_end,end)  
        count+=days-prev_end  
        return count