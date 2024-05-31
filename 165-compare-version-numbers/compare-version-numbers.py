class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both version strings by '.'
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        # Get the length of the longer version string
        max_length = max(len(v1_parts), len(v2_parts))
        
        # Compare each revision number
        for i in range(max_length):
            # Get the revision number for v1 and v2 at index i, default to 0 if index is out of range
            v1_part = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2_part = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            # Compare the revision numbers
            if v1_part < v2_part:
                return -1
            elif v1_part > v2_part:
                return 1
        
        # If all revisions are equal
        return 0
