import grpc
import bankworld_pb2
import bankworld_pb2_grpc
import time
import json

class Customer:
    def __init__(self, id, events, input_type):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stubList = list()
        # input type
        self.input_type = input_type

    # TODO: students are expected to create the Customer stub
    def createStub(self, numbranches):
        for i in range(numbranches):
            channelnumber = 50050+i+1
            channel = grpc.insecure_channel('localhost:'+str(channelnumber))
            self.stubList.append(bankworld_pb2_grpc.BranchStub(channel))
        return ("Done creating CLIENT stub " + str(channelnumber))

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        version = 0
        msg = ""
        if self.input_type != "mw":
            msg = " {\n \"id\": " + str(self.id) + ", \"balance\": ["
        previousbranch = 0
        newevents = self.events.replace("\'", "\"")
        eventslist = json.loads(newevents)

        # send each event to the proper destination branch
        for x in eventslist:
            if x['interface'] == 'query':
                x['ReadSet'] = str(previousbranch) + ":" + str(version)
                x['WriteSet'] = ""
            else:
                version += 1
                x['ReadSet'] = ""
                x['WriteSet'] = str(previousbranch) + ":" + str(version)
            singleevent = str(x)
            branchid = x['dest']
            previousbranch = branchid
            response = self.stubList[branchid-1].MsgDelivery(bankworld_pb2.BranchRequest(msg=singleevent))
            if (x['interface'] == 'query'):
                if self.input_type == "mw":
                    msg += " {\n \"id\": " + str(self.id) + ", \"balance\": " + response.branch_msg + "\n },\n"
                else:
                    msg += response.branch_msg + ", "
        if self.input_type != "mw":
            msg = msg[:-2] + "]\n },"
        return (msg)


