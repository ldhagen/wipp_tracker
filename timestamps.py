#!/usr/bin/env python

def print_stamps():
  ''' print tracker timestamps  '''
  import time
  import urllib2 as u
  print time.ctime(time.time() - 21600)
  print 'http://www.wipp.energy.gov/Special/Station%20A.pdf' 
  print u.urlopen('http://www.wipp.energy.gov/Special/Station%20A.pdf').info()['last-modified'] 
  print 
  print 'http://www.wipp.energy.gov/Special/Station%20B.pdf' 
  print u.urlopen('http://www.wipp.energy.gov/Special/Station%20B.pdf').info()['last-modified'] 
  print
  print 'http://wipp.energy.gov/wipprecovery/recovery.html' 
  print u.urlopen('http://wipp.energy.gov/wipprecovery/recovery.html').info()['last-modified'] 
  print
  print 'http://wipp.energy.gov/wipprecovery/photo_video.html'
  print u.urlopen('http://wipp.energy.gov/wipprecovery/photo_video.html').info()['last-modified']
  print

if __name__ == '__main__':
     print_stamps()
