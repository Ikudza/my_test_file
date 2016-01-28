import urllib, socket, string
alph = string.ascii_lowercase

def recurse(url, alph, count):
    count -= 1
    for i in alph:
        page_url = url + '{}/'.format(i)
        code = urllib.urlopen(page_url).getcode()
        #print "{0} - {1}".format(page_url, code)
        if (code in [200, 301]):
                print "YES: {0} - {1}".format(page_url, code)
        if count > 0:
            recurse(url+i, alph, count)
            


if __name__ == '__main__':
    page_url = 'http://ftp.mediapark.pro:82/'
    print 'start'
    count = 6
    for i in alph:
        page_url = 'http://ftp.mediapark.pro:82/' + i
        recurse(page_url, alph, count)
    print 'end'
