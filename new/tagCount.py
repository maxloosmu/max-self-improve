#!/usr/bin/python3
# ./tagCount.py
import os

path = "/mnt/c/Users/Max/max-self-improve"
write_path = path + "/tagCount.txt"

os.chdir(path)

mylist = []     # list of all occurences of tags
myset = set()   # set of one occurence of tags
mydict = {}
newdict1 = {}
newdict2 = {}

def read_html_file(file_path):
  with open(file_path, 'r') as f:
    for line in f:
      first_split = line.split()
      if len(first_split) > 0:
        first_in_line = line.split()[0]
        first_in_line_parts = len(first_in_line.split("#"))
        if first_in_line_parts > 1:
          tag = first_in_line.split("#")[1]
          if len(first_in_line.split("#")) == 2:
            mylist.append(tag)
            myset.add(tag)
    f.close()

# for file in os.listdir():
for root, dirs, files in os.walk("."):
  for name in files:
    if name.endswith(".html"):
      # file_path = f"{path}/{file}"
      file_path = os.path.join(root, name)
      read_html_file(file_path)

for val in myset:
  # create count dictionary for individual tags
  mydict[val] = mylist.count(val)
  # sort in alphabetical order based on tags, which are item[0]
  newdict1 = dict(sorted(mydict.items(), key=lambda item: item[0]))
  # sort based on count, which are item[1], from largest to smallest
  newdict2 = dict(sorted(newdict1.items(), key=lambda item: item[1], reverse=True))

# print(newdict2)
with open(write_path, 'w') as f:
  f.close()
with open(write_path, 'a') as f:
  for key in newdict2:
    f.write(f"{key}: {newdict2[key]}\n")
  f.close()
