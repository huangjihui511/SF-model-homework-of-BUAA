from queue import PriorityQueue

class CompareAble:
    def __init__(self,priority,jobname):
        self.priority = priority
        self.jobname = jobname

    def __cmp__(self, other):
        if self.priority < other.priority:
            return -1
        elif self.priority == other.priority:
            return 0
        else:
            return 1

    def __lt__(self, other):
        return self.priority < other.priority

class Vertex():
    def __init__(self,g,location,target,father):
        x = 5
        self.g = g
        self.f = abs(target[0] - location[0]) + abs(target[1] - location[1])
        self.h = g * x + self.f 
        self.father = father
        self.location = location


class Tactics():
    def __init__(self,hinders,gate,size):
        self.hinders = [(round(hinders[h].location[0]),round(hinders[h].location[1]))for h in hinders]
        self.target = (round(gate[0]),round(gate[1]))
        self.size  = size

    def think(self,src,r):
        target = self.target
        hinders = self.hinders
        src = (round(src[0]),round(src[1]))
        opened_table = PriorityQueue()
        closed_table = set()
        opened_table.put(CompareAble(0,Vertex(0,src,target,None)))
        notstop = True 
        while not opened_table.empty() and notstop:
            father = opened_table.get()
            end_Vertex = None
            rawDirection = father.jobname.location
            directions = [(rawDirection[0] + 1,rawDirection[1]),(rawDirection[0] + 1,rawDirection[1] + 1),(rawDirection[0],rawDirection[1] + 1),(rawDirection[0] - 1,rawDirection[1] + 1),(rawDirection[0] + 1,rawDirection[1] - 1),(rawDirection[0] + 1,rawDirection[1] - 1),(rawDirection[0],rawDirection[1] - 1),(rawDirection[0] - 1,rawDirection[1] - 1)]
            for direction in directions:
                if direction == target:
                    end_Vertex = father.jobname
                    notstop = False
                    break
                x , y = direction[0],direction[1]
                if x >= 0  and y >=0  and x <= self.size[0]  and y <= self.size[1] :
                    if direction not in closed_table:
                        tmp_queue = []
                        isin = False
                        newPriority = None
                        if direction in hinders:
                            newPriority = 1000000
                        else:
                            newPriority = father.jobname.g + 1
                        while not opened_table.empty():
                            tmp = opened_table.get()
                            if tmp.jobname.location == direction:
                                isin = True
                                if tmp.priority > newPriority:
                                    v = Vertex(newPriority,direction,target,father.jobname)
                                    tmp = CompareAble(v.h,v)
                            tmp_queue.append(tmp)
                        for tmp in tmp_queue:
                            opened_table.put(tmp)
                        if not isin:
                            v = Vertex(newPriority,direction,target,father.jobname)
                            opened_table.put(CompareAble(v.h,v))
            closed_table.add(rawDirection)
        if end_Vertex.father == None:
            return end_Vertex.location
        while end_Vertex.father.father != None:
            end_Vertex = end_Vertex.father
            print(end_Vertex.location)
        return end_Vertex.location


                        


