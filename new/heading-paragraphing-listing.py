#!/usr/bin/python3
import os

path = "/mnt/c/Users/Max/max-self-improve"
os.chdir(path)
new_html = ''

def read_html_to_remove_last_blank_lines(file_path):
  new_html_list = []
  with open(file_path, 'r') as f:
    for line in f:
      new_html_list.append(line)
    f.close()
  while new_html_list[-1] == '\n':
    new_html_list.pop(-1)
  new_html_list[-1] = new_html_list[-1].strip('\n')
  with open(file_path, 'w') as f:
    f.write(''.join(new_html_list))
    f.close()

def read_html_file(file_path):
  global new_html
  start_ul = False
  with open(file_path, 'r') as f:
    for line in f:
      if line[:3] == '## ':
        new_html = new_html + '<h2>' + line[3:-1] + '</h2>\n'
      elif line[:4] == '### ':
        new_html = new_html + '<h3>' + line[4:-1] + '</h3>\n'
      elif line[:2] == '- ' or line[:2] == '+ ' or line[:2] == '* ':
        if not start_ul:
          start_ul = True
          new_html = new_html + '<ul>\n'
        new_html = new_html + '<li>' + line[2:-1] + '</li>\n'
      elif line == '\n':
        if start_ul:
          start_ul = False
          new_html = new_html + '</ul>\n'
        new_html = new_html + '\n'
      elif line[0] == '#':
        new_html = new_html + line[:-1] + '<br/>\n'
      else:
        new_html = new_html + '<p>' + line[:-1] + '</p>\n'
    f.close()

def write_html_file(file_path):
  global new_html
  with open(file_path, 'w') as f:
    f.write(new_html)
    f.close()
  new_html = ''

def main():
  for root, dirs, files in os.walk("."):
    for name in files:
      if name.endswith("Me.html"):
        file_path = os.path.join(root, name)
        read_html_to_remove_last_blank_lines(file_path)
        read_html_file(file_path)
        write_html_file(file_path)

if __name__ == '__main__':
  main()
