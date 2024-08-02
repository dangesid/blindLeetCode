# input:  ["a","a","b","b","c","c","c"]
# ouptut : ["a","2","b","2","c","3"]


from collections  import Counter

chars =["a","a","a","b","b","a","a"]


dict = dict(Counter(chars))
print(dict)
lst = []
for k,v in dict.items():
    lst.append(k)
    lst.append(v)
print(lst)
str_lst = [str(i) for i in lst]
print(str_lst)
