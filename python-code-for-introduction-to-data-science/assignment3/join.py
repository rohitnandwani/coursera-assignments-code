import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: other_fields
    key = record[1]
    tempvalue = record[2:]
    table_id = record[0]
    value = [table_id]
    value = value + tempvalue
    mr.emit_intermediate(key, value)

def reducer(key, other_fields):
    # key: order_id
    # value: list_of_other_fields
    for i in other_fields:
      fields_list = []
      for j in other_fields:
        if i[0]=="order" and i[0] != j[0]:
          fields_list = [i[0], key] + i[1:]
          fields_list += [j[0], key] +j[1:]
          mr.emit((fields_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
