import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    key = record[0]
    value = record[1]
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key, [value, +1])
    mr.emit_intermediate(value, [key, -1])

def reducer(key, list_of_values):
    # key: person name
    # value: list of occurrence counts
    for i in list_of_values:
      if i[1] == -1:
        unsym = 1
        for j in list_of_values:
          if i[0] == j[0] and j[1] == +1:
            unsym = 0
        if unsym == 1:
          mr.emit((key, i[0]))
          mr.emit((i[0], key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
