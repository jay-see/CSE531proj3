from concurrent import futures
import logging
import time
import grpc
import bankworld_pb2
import bankworld_pb2_grpc
import json
from multiprocessing import Process

class Branch(bankworld_pb2_grpc.BranchServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # balance version number
        self.version = 0
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()


    # create the stubs to all other branches
    def createStubsss(self, branches):
        for i in range(branches):
            if (i+1) != self.id :
                channelnumber = 50050+i+1
                channel = grpc.insecure_channel('localhost:'+str(channelnumber))
                self.stubList.append(bankworld_pb2_grpc.BranchStub(channel))
            else :
                self.stubList.append(None)
        return ("Done creating BRANCH stubsss!!")

    # get the balance from the previous branch that client connected to, and update this branch's balance with it
    def Get_Balance(self, newversion, context):
        if (int(newversion.msg) >= int(self.version)):
            getmsg = str(self.balance)
        else :
            getmsg = "fail"
        return bankworld_pb2.BalanceReply(get_msg=getmsg)


    # return balance
    def Query(self, readset):
        [prevbranch,currentversion] = readset.split(':')
        if (int(prevbranch) != self.id) & (int(prevbranch) != 0) :
            response = self.stubList[int(prevbranch)-1].Get_Balance(bankworld_pb2.BalanceRequest(msg=str(currentversion)))
            self.balance = int(response.get_msg)
        if (int(self.version) > int(currentversion)):
            pass
        return self.balance

    # add deposit amount to this branch balance, but don't propagate it to any other branch until another branch calls the Get_Balance funtion
    def Deposit(self, amount, writeset):
        [prevbranch, currentversion] = writeset.split(':')
        if (int(prevbranch) != self.id) & (int(prevbranch) != 0) :
            response = self.stubList[int(prevbranch)-1].Get_Balance(bankworld_pb2.BalanceRequest(msg=str(currentversion)))
            if response.get_msg != "fail":
                self.balance = int(response.get_msg)
        new_bal = self.balance + amount
        if new_bal >= 0:
            self.balance = new_bal
            self.version = currentversion
            return "success"
        else:
            self.version = currentversion
            return "fail"

    # subtract withdrawal amount from this branch balance, but don't propagate it to any other branch until another branch calls the Get_Balance funtion
    def Withdraw(self, amount, writeset):
        [prevbranch, currentversion] = writeset.split(':')
        if (int(prevbranch) != self.id) & (int(prevbranch) != 0) :
            response = self.stubList[int(prevbranch)-1].Get_Balance(bankworld_pb2.BalanceRequest(msg=str(currentversion)))
            if response.get_msg != "fail":
                self.balance = int(response.get_msg)
        new_bal = self.balance - amount
        if new_bal >= 0:
            self.balance = new_bal
            self.version = currentversion
            return "success"
        else:
            self.version = currentversion
            return "fail"

    # parse the message received from customer and call appropriate branch routines
    def MsgDelivery(self, request, context):
        branchmsg = ""
        request.msg = request.msg.replace("\'", "\"")

        i = json.loads(request.msg)
        if i['interface'] == 'deposit':
            result = Branch.Deposit(self, i['money'], i['WriteSet'])

        elif i['interface'] == 'withdraw':
            result = Branch.Withdraw(self,i['money'], i['WriteSet'])

        elif i['interface'] == 'query':            
            bal = Branch.Query(self, i['ReadSet'])
            branchmsg = str(bal)

        return bankworld_pb2.BranchReply(branch_msg=branchmsg)

p = list()
count = 0

# instantiate all Branch objects, create branch stubs over ports 50051 to 50050+id
def Serve(id, balance, branches):
    channelnumber = 50050+id
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10,))
    bankbranch = Branch(id, balance, branches)
    bankworld_pb2_grpc.add_BranchServicer_to_server(bankbranch, server)

    server.add_insecure_port('[::]:'+str(channelnumber))
    server.start()

    out = bankbranch.createStubsss(branches)
    server.wait_for_termination()
    
# Call Serve() for each branch
def run():
    
    for y in data:
        if (y['type'] == 'bank') | (y['type'] == 'branch'):
            proc = Process(target=Serve, args=(y['id'], y['balance'], count,))
            proc.start()
            p.append(proc)
    for proc in p:
        proc.join()

            
# main function
if __name__ == '__main__':
    logging.basicConfig()

    
    # Opening JSON file
    f = open('input.json',)
    data = json.load(f)

# get number of banks N from input.json    
    for x in data:
        if (x['type'] == 'bank') | (x['type'] == 'branch'):
            count += 1

# call run() to create branches
    run()

