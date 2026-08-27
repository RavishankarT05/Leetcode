class Solution(object):
    def scoreValidator(self, events):
        z=0
        y=0
        a=0
        while a<len(events):
            if events[a].isdigit():
                z+=int(events[a])
            elif events[a]=="W":
                y+=1
            else:
                z+=1
            if y==10:
                break
            a+=1
        return [z,y]