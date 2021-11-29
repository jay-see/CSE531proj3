from concurrent import futures
import logging
import grpc
import bankworld_pb2
import bankworld_pb2_grpc
import json
from Customer import Customer
from multiprocessing import Process
import time
import threading
import sys

finalmsg = ""
    
# instantiate Customer object, create stub, and execute Events
def Cust(custid, custevents, numbranches):
    global finalmsg
    
    cust = Customer(custid, custevents, input_type)
    out = cust.createStub(numbranches)

    finalmsg = cust.executeEvents()
    # print to string
    with open("output.json", "a") as thefile:
        thefile.write("\n" + finalmsg)
 
# Opening JSON file
f = open('input.json',)
data = json.load(f)

# get argument: "mw" is monotonic writes, "rw" or anything else is read your writes
input_type = sys.argv[1]

p = list()

# main function
if __name__ == '__main__':
    logging.basicConfig()
    count = 0

    # add opening bracket
    with open("output.json", "a") as thefile:
        thefile.write("[")
        
    # count branches
    for z in data:
        if (z['type'] == 'bank') | (z['type'] == 'branch'):
            count += 1
    
    # send appropriate events to all customers
    for i in data:
        if (i['type'] == 'customer') | (i['type'] == 'client'):
            Cust(i['id'], str(i['events']),count,)

    with open("output.json", "a") as thefile:
# add closing bracket
        thefile.write("]")

# fix JSON format
    reading_file = open("output.json", "r")
    new_file_content = ""
    for line in reading_file:
        new_file_content += line.replace(",]", "\n]")
    reading_file.close()

    writing_file = open("output.json", "w")
    writing_file.write(new_file_content)
    writing_file.close()

f.close()
