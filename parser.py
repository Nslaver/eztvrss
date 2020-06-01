import feedparser
import time
import subprocess as sp
import pprint as pp

count = 0
names = ["kill"]
erase = '\x1b[1A\x1b[2K'
tick = 0.2
eztv = "https://eztv.io/ezrss.xml"
waint = 30
matches = ["snow", "rick", "bill"]
pro = ["/", "-", "\\", "|" ]

while True:
  fancy = 1
  tmp = sp.call('clear',shell=True)
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
  while cycle < 60:
    fancy = (fancy + 1) % 4
    print(erase*1 + "Wait {}".format(pro[fancy]))
    cycle = cycle + tick
    time.sleep(tick)
    pass
