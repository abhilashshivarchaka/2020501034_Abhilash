# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:
# took help from friend

def topScorer(data):
    # Your code goes here...
    if(len(data)==0):
        return None
    l=data.splitlines()
    # print(l)
    d={}
    for i in l:
        name=i.split(",")[0]
        scores=i.split(",")[1:]
        d[name]=0
        for j in range(len(scores)):
            d[name]+=int(scores[j])
    # print(d)
    n=[]
    s=[]
    for k,v in d.items():
        n.append(k)
        s.append(v)
    # print(n,s)
    ind=[]
    ma=max(s)
    for i in range(len(s)):
        if(s[i]>=ma):
            ind.append(i)
    # print(ind)
    out=""
    for i in ind:
        out+=n[i]+","
    return out[:-1]


data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
