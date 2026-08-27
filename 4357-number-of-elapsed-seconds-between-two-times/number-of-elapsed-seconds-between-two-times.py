class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        st=0
        et=0
        a=len(startTime)-1
        while 0<=a:
            if a==7:
                st+=int(startTime[a])
                et+=int(endTime[a])
            elif a==6:
                st+=int(startTime[a])*10
                et+=int(endTime[a])*10
            elif a==4:
                st+=int(startTime[a])*60
                et+=int(endTime[a])*60
            elif a==3:
                st+=int(startTime[a])*600
                et+=int(endTime[a])*600
            elif a==1:
                st+=int(startTime[a])*(60*60)
                et+=int(endTime[a])*(60*60)
            elif a==0:
                st+=int(startTime[a])*(60*60*10)
                et+=int(endTime[a])*(60*60*10)
            a-=1
        return et-st

        