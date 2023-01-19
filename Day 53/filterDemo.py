def filter_function(a):
  return a>2
  
l=[1,2,4,6,4,3]
newnewl=list(filter(filter_function, l))
print(newnewl)

#Simply Understand it like that what does filter in normal life does ? It Filters the water right..basically the thing is for any element if the condition goes true, that element will go in the new filter object(like inside the container we say that we want no dirt, so for all water if there is any impurity associated it will not get in our glass) which further can be typecasted into list, so that we can use it efficiently for our purpose.
