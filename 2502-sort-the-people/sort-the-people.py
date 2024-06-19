class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name = list(zip(names , heights ))

        for i in range(len(name)):
            for j in range(0 , len(name) -i -1 ):
                if name[j][1] < name[j+1][1]:
                    name[j] , name[j+1] = name[j+1] , name[j]
        
        arr = []
        for i in range(len(name)):
            arr.append(name[i][0])

        return arr