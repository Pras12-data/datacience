#print("prob1")


#def H():
# return (prob1.count(H))/len(prob1)

#def T():
# return ((prob1.count(T))/len(prob1)






import statistics
l = [5,2,4,3,1,1]
l.sort()
print(l)
def mean():
    mean=sum(l)/len(l)
    print(mean)
mean()
def median():
    median=statistics.median(l)
    print(median)
median()
def mode():
    mode=statistics.mode(l)
    print(mode)
mode()




def probability(sample_space,event):
	n_of_event=0
	for i in sample_space:
		if i==event:
			n_of_event+=1
	prob=n_of_event/len(sample_space)
	return prob
s=["head", "tail"]
e="head"
print(probability(s,e))	



l = {1,2,3,4,5}
l2={1,2,6}


def Union():
    Union=l.union(l2)
    print(Union)
Union()
def intersection():
    intersection=(l.intersection(l2))
    print(intersection)
intersection()
def difference():
    difference=l.difference(l2)
    print(difference)
difference()
