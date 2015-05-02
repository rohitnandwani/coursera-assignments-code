import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: individual word
    # value: document identifiers
    key = record[1]
    value = record[0]
    words = key.split()
    for w in words:
      #if w in value:
      mr.emit_intermediate(w, value)

def reducer(word, list_of_docid):
    # key: word
    # value: list of document identifiers
    docid_list = []
    for v in list_of_docid:
      if v not in docid_list:
        docid_list.append(v)
    mr.emit((word, docid_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
