import urllib

def getAllOHs():
    f = urllib.urlopen("http://www.seas.upenn.edu/~bhusnur4/cit590_spring2015/staff.html")
##    f = urllib.urlopen("http://chenyikeupenn.wix.com/portfolio")

    line = f.readline()
    print 'lines',line,'\n'
    OHs = []
    allMyLines = []
    i=0
    # as long as there is lines in the file
    while line:
        allMyLines.append(line)
        i += 1
        # if 'Office Hours' not found, we return -1
        if line.find('Office Hours') >=0:
            OHs.append(line)
        line = f.readline()
    f.close()
    return OHs

def main():
    tas = getAllOHs()
    print tas

if __name__ == '__main__':
    main()
