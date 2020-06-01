import feedparser
import time
import subprocess as sp
import pprint as pp
import getopt
import re
import sys

def main(argv):
  inputFile = ""
  count = 0
  erase = '\x1b[1A\x1b[2K'
  tick = 0.2
  eztv = "https://eztv.io/ezrss.xml"
  wait = 300
  pro = ["/", "-", "\\", "|" ]
  opts, args = getopt.getopt(argv, "i:", ["ifile="])

  for opt, arg in opts:
    if opt in ("-i", "--ifile"):
      inputFile = arg

  matches = re.split('\s+', inputFile)

  while True:
    fancy = 1
    sp.call('clear',shell=True)
    print("Loading {}".format(eztv))
    print("Looking for:{} cy: {} \n".format(matches,count))
    feed = feedparser.parse(eztv)

    count = count + 1
    cycle = 1.0
    for item in feed["items"]:
      if any(x in item.title.lower() for x in matches):
        print(item.title)
        print(item.links[1].href)
        pass
      else:
        pass
    pass

    print("\n")
    while cycle < wait:
      fancy = (fancy + 1) % 4
      print(erase*1 + "Wait {}".format(pro[fancy]))
      cycle = cycle + tick
      time.sleep(tick)
      pass

if __name__ == "__main__":
    main(sys.argv[1:])
