#!/usr/bin/python3
# ./md2html.py
import os

path = "/mnt/c/Users/Max/max-self-improve"
os.chdir(path)

def main():
  for root, dirs, files in os.walk("."):
    for name in files:
      if name.endswith(".md"):
        os.rename(os.path.join(root, name), os.path.join(root, name[:-3] + ".html"))

if __name__ == '__main__':
    main()