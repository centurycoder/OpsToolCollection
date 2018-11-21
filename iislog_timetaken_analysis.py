import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    starttime = ""
    endtime = ""
    if (len(sys.argv) == 4):
        starttime = sys.argv[2]
        endtime = sys.argv[3]
    scatter = {}

    file=open(filename,'rt')
    for line in file:
        (day,time,host,timetaken) = line.strip('\r\n').split(" ")
        if ((starttime !="") and (time < starttime or time >= endtime)):
            continue
        else:
            print day,time,host,int(timetaken)
            seconds = int(timetaken) / 1000
            if seconds in scatter:
                scatter[seconds] += 1
            else:
                scatter[seconds] = 1
    print scatter
    file.close()
