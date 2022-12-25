text="My Name is {1} and i Love {0}"                    #provided index
name="Prakhar"
hobby="writing code"
print(text.format(name,hobby))          #{} will be replaced by respective arguments passed inside format...remmber by default order is going to be as provided, but if we provide index in curly braces, we can change it.

#Same thing can be achieved via using f-Strings
print(f"My Name is {name} and i Love {hobby}")       #this seems more cool right!

print(f"My Name is {{name}} and i Love {{hobby}}")      #if you need ypur variables to be retianed, use double curly braces

print(f"My Name is {{{name}}} and i Love {{{hobby}}}")    #Remember this too

print(type(f"{2 * 30}"))   #this will be string too, this is something cool!