haystack="aadbsadutsad"
needle="sad"

print(haystack.find(needle))

#haystack="leetcode"
#needle="leeto"

#print(haystack.find(needle))

for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)]==needle:
        print(i)
        break
