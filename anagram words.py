from collections import defaultdict
list1 =['limp','eat','me','tea','em','plum']
print("The original list :"+str(list1))
p = defaultdict(list)
for i in list1:
    p[str(sorted(i))].append(i)
res = list (p.values())
print("The grouped Anagrams :"+str(res))



'''

The original list :['limp', 'eat', 'me', 'tea', 'em', 'plum']
The grouped Anagrams :[['limp'], ['eat', 'tea'], ['me', 'em'], ['plum']]

'''
