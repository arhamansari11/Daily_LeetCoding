class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically so parent folders come before their subfolders
        folder.sort()
        # Initialize result list
        result = []
        for f in folder:
            # Get the last added folder path and add a trailing slash
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)

        return result
