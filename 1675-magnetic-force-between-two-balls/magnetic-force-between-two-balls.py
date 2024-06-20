class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low , high = 1 , position[-1] - position[0]
        while low <= high:
            mid = (low + high) // 2
            last_position = position[0]
            count = 1 
            for i in range(1 , len(position)):
                if position[i] - last_position >= mid:
                    count += 1
                    last_position= position[i]
                if count >= m:
                    break
            
            if count >= m:
                low = mid + 1
            else:
                high = mid -1
        
        return high

