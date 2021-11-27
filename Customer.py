import grpc
import bankworld_pb2
import bankworld_pb2_grpc
import time
import json
#from multiprocessing import Process, Queue

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = ""
        # pointer for the stub
        self.stubList = list()
        # list of event processes
        self.p = list()
#        self.pqueue = Queue()
        self.WriteSet = list()

    # TODO: students are expected to create the Customer stub
    def createStub(self, numbranches):
#        print (numbranches)
        self.WriteSet = ["["] * numbranches
        for i in range(numbranches):
            channelnumber = 50050+i+1
            channel = grpc.insecure_channel('localhost:'+str(channelnumber))
            self.stubList.append(bankworld_pb2_grpc.BranchStub(channel))
            print ("Done creating CLIENT stub " + str(channelnumber))
        return ("Done creating CLIENT stub " + str(channelnumber))

#    def runEvent(self, id, singular, queue):
#        response = self.stubList[id-1].MsgDelivery(bankworld_pb2.BranchRequest(msg=singular))
#        time.sleep(3)
#        queue.put(response.branch_msg + "\n },")
#        self.recvMsg = response.branch_msg + "\n },"
#        print (self.recvMsg)
#        return
    
    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        print ("Executing events.." + self.events)
        msg = " {\n \"id\": " + str(self.id) + ", \"balance\": "
        
        newevents = self.events.replace("\'", "\"")
        eventslist = json.loads(newevents)

        # send each event to the proper destination branch
        for x in eventslist:
            singleevent = str(x)
            branchid = x['dest']
#            print (singleevent)
            self.WriteSet[branchid-1] += singleevent + ","

        for y in range(len(self.WriteSet)):
            if (self.WriteSet[y] != "["):
                self.WriteSet[y] = self.WriteSet[y][:-1] + "]"            
                line = self.WriteSet[y].replace("\'", "\"")
                jsonline = json.loads(line)
 #           proc = Process(target=Customer.runEvent, args=(self, branchid, singleevent,self.pqueue,))
 #           proc.start()
 #           self.p.append(proc)
 #       for proc in self.p:
 #           proc.join()
#            Customer.runEvent(self, branchid, singleevent)
                response = self.stubList[y].MsgDelivery(bankworld_pb2.BranchRequest(msg=str(jsonline)))
#            print (self.pqueue.get())
                msg += response.branch_msg + "\n },"
                print (msg)
        return (msg)

