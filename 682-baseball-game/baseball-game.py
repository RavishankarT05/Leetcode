class Solution(object):
    def calPoints(self, operations):
        a=0
        q=[]
        while a<len(operations):
            if operations[a].isdigit() or operations[a][1:].isdigit():
                q.append(int(operations[a]))
            else:
                if operations[a]=="+":
                    q.append(q[-1] + q[-2])
                elif operations[a]=="D":
                    q.append(q[-1]*2)
                elif operations[a]=="C":
                    q.pop()
            a+=1
        return sum(q)
            
        