import grpc
import bankworld_pb2
import bankworld_pb2_grpc
import time
import json

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stubList = list()

    # TODO: students are expected to create the Customer stub
    def createStub(self, numbranches):
        print (numbranches)
        for i in range(numbranches):
            channelnumber = 50050+i+1
            channel = grpc.insecure_channel('localhost:'+str(channelnumber))
            self.stubList.append(bankworld_pb2_grpc.BranchStub(channel))
            print ("Done creating CLIENT stub " + str(channelnumber))
        return ("Done creating CLIENT stub " + str(channelnumber))

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
            print (singleevent)
            response = self.stubList[branchid-1].MsgDelivery(bankworld_pb2.BranchRequest(msg=singleevent))
        msg += response.branch_msg + "\n },"
        return (msg)
