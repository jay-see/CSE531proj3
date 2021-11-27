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
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

    # TODO: students are expected to process requests from both Client and Branch

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

    # add the deposit amount to this branch's balance
    def Propagate_Deposit(self, amount, context):
        new_bal = self.balance + int(amount.msg)

        if new_bal >= 0:
            self.balance = new_bal
            depositmsg = "success"
        else :
            depositmsg = "fail"
        return bankworld_pb2.DepositReply(deposit_msg=depositmsg)

    # subtract the withdrawal amount from this branch's balance
    def Propagate_Withdraw(self, amount, context):
        new_bal = self.balance - int(amount.msg)

        if new_bal >= 0:
            self.balance = new_bal
            withdrawmsg = "success"
        else :
            withdrawmsg = "fail"
        return bankworld_pb2.WithdrawReply(withdraw_msg=withdrawmsg)

    # return balance
    def Query(self):
#        time.sleep(3)
        return self.balance

    # add deposit amount to this branch balance and then use branch stubs to send the transaction to all other branches
    def Deposit(self, amount):
        new_bal = self.balance + amount
        if new_bal >= 0:
            self.balance = new_bal

            for i in range(len(self.stubList)) :
                if (i+1) != self.id :
                    response = self.stubList[i].Propagate_Deposit(bankworld_pb2.DepositRequest(msg=str(amount)))

            return (response.deposit_msg)
        else:
            return "fail"

    # subtract withdrawal amount from this branch balance and then use branch stubs to send the transaction to all other branches
    def Withdraw(self, amount):
        new_bal = self.balance - amount
        if new_bal >= 0:
            self.balance = new_bal

            for i in range(len(self.stubList)) :
                if (i+1) != self.id :
                    response = self.stubList[i].Propagate_Withdraw(bankworld_pb2.WithdrawRequest(msg=str(amount)))

            return (response.withdraw_msg)
        else:
            return "fail"

    # parse the message received from customer and call appropriate branch routines
    def MsgDelivery(self, request, context):
        branchmsg = ""
        request.msg = request.msg.replace("\'", "\"")

        reqmsg = json.loads(request.msg)
        for i in reqmsg:
            if i['interface'] == 'deposit':
                result = Branch.Deposit(self,i['money'])
                branchmsg = "deposited " + str(i['money']) + " balance = " + str(self.balance) + " at branch " + str(self.id)
                print ("BRANCHMESSAGE: " + branchmsg)
            elif i['interface'] == 'withdraw':
                result = Branch.Withdraw(self,i['money'])
                branchmsg = "withdrew " + str(i['money']) + " balance = " + str(self.balance) + " at branch " + str(self.id)
                print ("BRANCHMESSAGE: " + branchmsg)
            elif i['interface'] == 'query':
                bal = Branch.Query(self)
                branchmsg = "queried " + str(bal) + " at branch " + str(self.id)
                print ("BRANCHMESSAGE: " + branchmsg)
        print (branchmsg)
        return bankworld_pb2.BranchReply(branch_msg=branchmsg)


p = list()
count = 0
#index = 0

# instantiate all Branch objects, create branch stubs over ports 50051 to 50050+id
def Serve(id, balance, branches):
#    global index
    
    channelnumber = 50050+id
#    index+=1
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10,))
    bankbranch = Branch(id, balance, branches)
    print ("IIIIIIIIIDDDDDDDDDDDDDDDDDD = " + str(id))
    print ("SERVERLIST = " + str(server))
    print ("BANKBRANCH = " + str(bankbranch))
    bankworld_pb2_grpc.add_BranchServicer_to_server(bankbranch, server)

    server.add_insecure_port('[::]:'+str(channelnumber))
    server.start()

    out = bankbranch.createStubsss(branches)
    server.wait_for_termination()
    
# Call Serve() for each branch
def run():
#    branchnum = 0
    
    for y in data:
        if (y['type'] == 'bank') | (y['type'] == 'branch'):
#            branchnum += 1
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

