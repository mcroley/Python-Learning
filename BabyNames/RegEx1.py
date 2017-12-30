# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re


def extract_names(filename, regExStr):
  """
  this gives information on the mouse over of the function
  Given a file name, returns a list starting with the year string
 
  """
  
  names = []

  # Open and read the file.
  f = open(filename, 'r') # open is a built in Python function for reading files
  text = f.read()  
  #year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text) # re is a regular expression Python function imported
  year_match = re.search(r'Popular', text)
  if not year_match:      
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)  #if no year is found then we need to do an exit. Otherwise we'll get a full stack trace. Also, this is like an if/else
  year = year_match.group(1)
  names.append(year)
  print(names)
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  #args = sys.argv[1:]

  #if not args:
  #  # print 'usage: [--summaryfile] file [file ...]'
  #  sys.exit(1)

  ## Notice the summary flag and remove it from args if it is present.
  #summary = False
  #if args[0] == '--summaryfile':
  #  summary = True
  #  del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  extract_names('1990file.html', 'Year')
  
if __name__ == '__main__':
  main()

