class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l , r = 0 , len(people)-1
        boat = 0
        while l <= r:
            left = people[l]
            right = people[r]
            if left + right <= limit:
                l += 1
                r -= 1
                boat += 1
            else:
                r -= 1
                boat += 1

        return boat
