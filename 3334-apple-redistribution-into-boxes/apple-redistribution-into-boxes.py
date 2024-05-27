class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        box = 0
        capacity.sort(reverse=True)
        for i in capacity:
            if total_apples <= 0:
                break
            total_apples -= i
            box += 1
        return box
