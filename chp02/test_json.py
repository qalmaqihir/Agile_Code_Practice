import sys, os, re
import json
import codecs

arr_of_objects=[
    {'name':'Jawad Haider','title':'CEO'},
{'name':'Sajjad Khan','title':'CIO'},
{'name':'Haider Khan','title':'CTO'}
]

path='./temp/test.jsonl'

#
#Write our objects to jsonl
#

f= codecs.open(path,'w','utf-8')
for row in arr_of_objects:
    #ensure_ascii=False is essentail or errors/corruption will occur
    json_record=json.dumps(row, ensure_ascii=False)
    f.write(json_record+'\n')
f.close()

print('Wrote JSON Line files in ', path)

#
# Read this jsonl file back into objects
arr_of_object=[]
f=codecs.open(path,'r','utf-8')
for line in f:
    record=json.loads(line.rstrip('\n|\r'))
    arr_of_objects.append(record)

print(arr_of_object)
print("Readd JSON Line File from ", path)