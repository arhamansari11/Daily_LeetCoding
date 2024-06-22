class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = len(students)
        while students and sandwiches and sandwiches[0] in students:
            if students[0] != sandwiches[0]:
                students.append(students[0])
                students.pop(0)
            else:
                students.pop(0)
                sandwiches.pop(0)
                count -= 1
        
        return count