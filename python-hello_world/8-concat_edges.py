#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.index("ob"):str.index("ing")+ 4] + str[str.index("with"):str.index("very")] + str[:7]
print(str)
