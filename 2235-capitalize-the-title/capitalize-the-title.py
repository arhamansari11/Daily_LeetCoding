class Solution:
    def capitalizeTitle(self, title: str) -> str:
        string = ""
        x = title.split()

        for i in x:
            if len(i) > 2:
                string = string + i.title() + " "
            else:
                string = string + i.lower() + " "

        return string.rstrip()