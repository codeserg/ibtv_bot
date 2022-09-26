from datetime import datetime
from sanic import Sanic
from sanic import response
from ib_insync import *

ib=None
app= Sanic(__name__)


@app.route('/')
async def root(request):
    return response.text ('ok')

@app.route('/webhook', methods= ['POST'])
def webhook(request):
            
    if request.method == 'POST':
        #checkIfReconnect()
        data = str(request.body)
        
        command= data[2:5]
        ordercommand = ""
        print (data, command)
        
        if command == 'sel':
            ordercommand ='SELL'
        if command == 'buy':
            ordercommand ='BUY'
        
        if ordercommand != "":

            order = MarketOrder(ordercommand,1,account = ib.wrapper.accounts[0] )
            curr_dt = datetime.now()
            order.orderId = int(round(curr_dt.timestamp()))

            contract =Future (symbol='ES', lastTradeDateOrContractMonth='20221216', exchange='GLOBEX', localSymbol='ESZ2', multiplier='50', currency='USD')
            

            trade = ib.placeOrder(contract,order)
            print(trade.log)
                        

    return response.text ('')

async def checkIfReconnect():
    global ib
    if not ib.isConnected() or not ib.client.isConnected():
        ib.disconnect
        ib = IB()
        ib.connect('127.0.0.1',7497)    
    

if __name__ == '__main__':
    ib = IB()
    ib.connect('127.0.0.1',7497)
    app.run(port=5001)