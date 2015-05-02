import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: nucleotide string
    key = record[1]
    key = key[:-10]
    #value = record[0]
    mr.emit_intermediate(key, 0)
    #words = value.split()
    #for w in words:
      #mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    # key: nucleotide string
    # value: 0
    #total = 0
    #for v in list_of_values:
      #total += v
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
