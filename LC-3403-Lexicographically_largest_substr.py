# i/p= "dbca"
# o/p= "dbc"

def lexicographic(self, word:str, numFriends:int )-> str:
    n = len(word)
    max_possible = n - (numFriends-1)
    res = ""
    # if there is only 1 friend, he gets the full word
    if numFriends==1:
        return word

    for i in range(n):
        can_take = min(max_possible, n-i)
        substr = word[i:i+can_take]
        res = max(res, substr)

    return res