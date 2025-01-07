class Solution:
    def displayContacts(self, n, contact, s):
        # Result will store list of lists for each prefix search
        result = []
        
        # For each prefix length from 1 to length of search string
        for i in range(1, len(s) + 1):
            prefix = s[:i]  # Get current prefix
            temp = []  # Store matches for current prefix
            
            # Search through all contacts
            for name in contact:
                # If contact starts with current prefix
                if name.startswith(prefix):
                    temp.append(name)
            
            # If no matches found, append "0"
            if not temp:
                result.append(["0"])
            else:
                # Sort matches in lexicographical order and remove duplicates
                temp = sorted(list(set(temp)))
                result.append(temp)
        
        return result