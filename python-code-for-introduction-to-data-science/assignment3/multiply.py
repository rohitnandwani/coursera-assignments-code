import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = ""
    if record[0] == "a":
      for i in range(5):
       key = str(record[1]) + "." + str(i)
       mr.emit_intermediate(key, ["a", record[2], record[3]])
    if record[0] == "b":
      for i in range(5):
        key = str(i) + "." + str(record[2])
        mr.emit_intermediate(key, ["b", record[1], record[3]])


def reducer(key, list_of_values):
    aindex = {}
    bindex = {}
    a = []
    b = []

    for v in list_of_values:
      if v[0] == "a":
        index = v[1]
        aindex[index] = v[2]
      if v[0] == "b":
        index = v[1]
        bindex[index] = v[2]

    for i in range(5):
      if i in aindex:
        a.append(aindex[i])
      if i not in aindex:
        a.append(0)
    
    for i in range(5):
      if i in bindex:
        b.append(bindex[i])
      if i not in bindex:
        b.append(0)

    c = 0
    for i in range(0, len(a)):
      c = c + a[i]*b[i]
    key_list = key.split(".")

    mr.emit((int(key_list[0]), int(key_list[1]), c))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
