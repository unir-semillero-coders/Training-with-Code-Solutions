"""
Introduction
The first century spans from the year 1 up to and including 
the year 100, the second century - from the year 101 up to and 
including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
"""

""" Yo
import numpy as np

n= np.arange(500)

def centuryFromYear(ano):
    for i in range(len(n)):
        if (i < ano <= i*100):
            return f"El año: {ano} pertenece al Siglo: {i}"
        elif (i*100 < ano <=(i+1)*100):
            return f"El año: {ano} pertenece al Siglo: {i+1}"


print(centuryFromYear(1))
print(centuryFromYear(5200))
print(centuryFromYear(1900))
"""

""" Avanta
def century(year):
    return (year + 99) // 100
"""