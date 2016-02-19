#!/usr/bin/env python
import time
import urllib2 as u

def time_stamps():
    ''' write timestamps of targeted files to TimesFile.txt  '''
    timesfile = file('TimesFile.txt','w')
    timesfile.write(str(time.ctime(time.time())))
    timesfile.write('\n')
    timesfile.write('\n')
    timesfile.write('http://www.wipp.energy.gov/Special/Station%20A.pdf' + '\n') 
    timesfile.write(str(u.urlopen('http://www.wipp.energy.gov/Special/Station%20A.pdf').info()['last-modified']) + '\n') 
    timesfile.write('\n')
    timesfile.write('http://www.wipp.energy.gov/Special/Station%20B.pdf' + '\n') 
    timesfile.write(str(u.urlopen('http://www.wipp.energy.gov/Special/Station%20B.pdf').info()['last-modified']) + '\n') 
    timesfile.write('\n')
    timesfile.write('http://wipp.energy.gov/wipprecovery/recovery.html' + '\n') 
    timesfile.write(str(u.urlopen('http://wipp.energy.gov/wipprecovery/recovery.html').info()['last-modified']) + '\n')
    timesfile.write('\n')
    timesfile.write('http://wipp.energy.gov/wipprecovery/photo_video.html' + '\n')
    timesfile.write(str(u.urlopen('http://wipp.energy.gov/wipprecovery/photo_video.html').info()['last-modified']) + '\n')
    timesfile.write('\n')
    timesfile.close()

def grab_pages():
    ''' scrape targeted pages and place in files '''
    file1 = file('StationA.pdf', 'w')
    page1 = u.urlopen('http://www.wipp.energy.gov/Special/Station%20A.pdf')
    file1.write(page1.read())
    file1.close()

    file2 = file('StationB.pdf', 'w')
    page2 = u.urlopen('http://www.wipp.energy.gov/Special/Station%20B.pdf')
    file2.write(page2.read())
    file2.close()

    file3 = file('Main.txt', 'w')
    page3 = u.urlopen('http://wipp.energy.gov/wipprecovery/recovery.html')
    file3.write(page3.read())
    file3.close()

    file4 = file('Photos.txt', 'w')
    page4 = u.urlopen('http://wipp.energy.gov/wipprecovery/photo_video.html')
    file4.write(page4.read())
    file4.close()

if __name__ == '__main__':
   time_stamps()
   grab_pages()
