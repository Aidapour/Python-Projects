#!/usr/bin/env python3.9

#init our blockchain list
blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

"""Retrun the last valu of current blockchain"""

def add_value(transaction_ammount, last_transction= [1]):
    blockchain.append([ last_transction,transaction_ammount])
"""Append a new value as well as last block chain value to the block chain 
   Arguments:
   
   : transaction_ammount : the ammount should be added.
   : last_transction : the last block chain 
   """
   
   
   

def get_user_input ():

    """retrun the input of the user ( a new transction ammount )as a float"""

    return float (input('please add your transction amount'))

tax_amout = get_user_input ()
add_value(tax_amout)
tax_amout = get_user_input ()
add_value(last_transction= get_last_blockchain_value(),transaction_ammount =0)
tax_amout = get_user_input ()
add_value(last_transction= get_last_blockchain_value(),transaction_ammount =3.4)

print(blockchain)
