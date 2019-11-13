from collections import defaultdict

colours=(('yasoob','yellow'),('ali','blue'),('arham','green'),('ali','black'),('yasoob','red'),('ahmed','silver'),)
print(type(colours))
favourite_colours=defaultdict(list)
for name,colour in colours:
    favourite_colours[name].append(colour)
print(favourite_colours)
