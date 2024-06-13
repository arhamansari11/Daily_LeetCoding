class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            moves += abs(students[i] - seats[i])

        return moves