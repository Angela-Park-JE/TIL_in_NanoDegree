# Who likes it?
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

### MINE

def likes(names):
    if len(names) == 0:
        print("'", 'no one likes this', "'", sep='')
    elif len(names) == 1:
        print("'", names[0], " likes this", "'", sep='')
    elif len(names) == 2:
        print("'", names[0], " and ", names[1], " like this", "'", sep='')
    elif len(names) == 3:
        print("'", names[0], ", ", names[1], " and ", names[2], "l ike this","'", sep='')
    elif len(names) >= 4:
        print("'", names[0], ", ", names[1], " and ", len(names)-2, ' others like this', "'", sep='')
        
# THis works well and the results were same with that but 'codewars' didn't accept mine.
