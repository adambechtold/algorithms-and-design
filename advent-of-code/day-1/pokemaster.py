import re
import sys

#Dictionary for part 2 to replace instances of words that describe digits with digits, retaining the first letter for the infamous "oneight" type cases.
replacement = {"one": "o1e", "two": "t2o", "three":"t3e", "four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}

#Open and return the file passed as parameter to program
def readInput():
    if len(sys.argv)==1:
        print("Missing parameter, use the program like this: python3 day1.py [inputfile]")
        exit()
    try:
        f = open(sys.argv[1])
    except FileNotFoundError:
        print("File not found, check your filename and path and try again.")
        exit()
    return f

#Strip all non digit characters from the string
def cleanup(line):
    return re.sub("\D", '', line)

#Acutally solve both parts of the challenge
def solve(f):
    results = [0,0]
    for line in f.readlines():
        li1 = cleanup(line)
        li2 = line
        for key in replacement.keys():
            li2 = re.sub(key, replacement[key], li2)
        li2 = cleanup(li2)
        results[0]+=int(li1[0]+li1[-1])
        results[1]+=int(li2[0]+li2[-1])
    return results

#Print results of part1
res = solve(readInput())
print("Part1: ", res[0])
print("Part2: ", res[1])