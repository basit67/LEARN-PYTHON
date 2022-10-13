#list  -  have brackets []


movies = ["harry","hangover","wallflower","she hulk"]
print(movies[1]) #return second item
print(movies[0]) #returrn first item
print(movies[1:4]) #it does not include last item 
print(movies[1:])#it show all item after 1 but not 1 
print(movies[:2])
print(movies[-1])

#for lenth of list how many name in list
print(len(movies))

#to add item in list
#added to end of list
movies.append("jaws")
print(movies)

#to remove item in list
#it remove last item in list
movies.pop()
print(movies)
#it remove seleted item on list in "()"
movies.pop(0)
print(movies)