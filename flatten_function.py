def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            empty_list.append(i)


x= [[1, 2], [3, 4], [5, 6, 7]]
empty_list = [] 
flatten(x)
print(empty_list)
