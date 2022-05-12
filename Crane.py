# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:23:51 2022

@author: User
"""
# Import pandas library

from PythonUlt import *
# initialize Dataset this dataset will be the database that the plc will communicate with

##DunctionList##
#Create Dataset
  


def main():
    ##Create the dataset Random generated Values
    createData()
    ##Load the dataset
    mainDataset()
    ##print the dataset
    mainDataset()
    ##print the Blocks that there are workers on
    maintnaceBlocks()
    id_search("3")
    ##openGrid still needs some debugging for the NameError
    #openGrid()
    #gridOpener()
    ##Path finding calculates the path from start to finish O=start X=finish
    #PathFinding()
    ##Create the a QR_code that has the ticket information
    create_order_ticket(19)
    ##Read the QR_code and receive the order ID
    read_ticket=read_order_ticket()
    ##printTicketInfo
    print(read_ticket)
    ##Return the position of a any order based on unique id
    pos_from_uniqueID(read_ticket)
    
main()
