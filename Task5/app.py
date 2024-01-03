from flask import Flask,request,jsonify

new=Flask(__name__)

#API which gets data from the user and returns the respected output using GET and POST 
# method for the bank withdrawal and deposit
@new.route('/bank',methods=['POST','GET'])
def bank():
    try:
        if request.method=='POST':
            a = request.get_json("data")
            net_amount=a['net_amount']
            mode=a['mode']
            amount=a['amount']  
                  
            if mode=='d' or mode=='D' or mode=='DEPOSIT' or mode=='Deposit' or mode=='deposit':
                net_amount=net_amount+amount
                return f'{net_amount}'
            elif mode=='w' or mode=='W' or mode=='WITHDRAW' or mode=='withdraw' or mode=='Withdraw':
                net_amount=net_amount-amount
                return f'{net_amount}'
            else:
                return jsonify(f'Invalid input for deposit/withdraw')
        else:
            return jsonify(f'The Invalid input')
    except Exception as exp:
        return jsonify(f'The error in input : {str(exp)}')
    
#Main function
if __name__ == '__main__':
    new.run(debug=True)