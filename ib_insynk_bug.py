# ib-insync 0.9.71
# Python 3.10.4
# Demo account Trader Workstation Build 10.18.1e, Sep 20, 2022 4:11:21 PM
# Windows10 1809

# Found Bug: only first order appears at TWS
# if ib.sleep(0) added - all orders appears
# print shows correct OrdedID assigned to each trade

from ib_insync import *

ib = IB()
ib.connect('127.0.0.1',7497)
contract = Stock (symbol='SPY', exchange='SMART',  currency='USD')

for n in range(3):
    order = MarketOrder('BUY',1,account = ib.wrapper.accounts[0] )
    trade = ib.placeOrder(contract,order)
    print('---',trade)
    #ib.sleep(0) 
