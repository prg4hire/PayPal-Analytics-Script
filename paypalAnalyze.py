#!/usr/bin/python 

# This script has been tested using Python 2.7

# It takes a PayPal transaction csv file as first argument, and then outputs
# the amounts sent by every sender, in different currencies. It also shows
# the total that was withdrawn to your bank account.

# This script was written to help all freelancers, businesses, sellers etc who use PayPal. 
# If you find it useful, consider hiring me or donating at my gmail/PayPal address prg4hire@gmail.com
# My bitcoin address is 1JVM63khCnZbi36i3w2pbXWgKJ1VaRLP9o

import csv, sys

monthNames = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# refer http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python
# https://docs.python.org/2/howto/logging.html
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def usage():
    """ Prints the usage message """
    print "Usage:\n\nanalyzePayPal.py PayPalTransactionsFile.csv\n"
    print ""
    print "To get/create the PayPalTransactionsFile.csv, log in to your PayPal account."
    print "Then follow Activity -> Statements -> Activity Export"
    print "Select period, and in File Type, select Comma Delimited - All Activity"
    print "Click Download. The file downloaded is the input file to this script, to be given as first command line argument"   

def analyze(filename):
    """ This function analyzes the Paypal csv transaction file """
    
    # The basic data structure that is used to store the amounts sent. 
    # The key of the outer dict is a currency name. Then the inner dict's key is 
    # the client name. Finally, the value for each client is a list that is the 
    # sum received for each month. 0th value is the total sum received for that client.
    # 1st value is for Jan, 2nd for Feb, and so on. Total is stored at 0th position so that the values 
    # can be easily sorted. An example state is { "USD: { "John": [1000, 100, 800, 0,0,0,0,0,0,0,0,0,100]}} 
    currencies = dict()    

    totalWithdrawn = 0

    try:
        csvlines = csv.reader(open(filename, "r"))
    except:
        print "Could not open file", filename
        usage()
        exit()


    for date,time, timezone, name, typ, status, currency, amount, receiptid,empty, balance in csvlines:
        amount = amount.replace(",", "") # change numbers from 1,123 to 1123

        if "Payment Received" in typ or "eCheque Received" in typ:
            if "Update" in typ:    # some transactiions are updattes, such as update that echeque cleared. We ignore these.
                continue 
            month = date[3:5]
            if currency in currencies:
                if name not in currencies[currency]:
                    currencies[currency][name] = [0] * 13
            else:
                currencies[currency] = dict()
                currencies[currency][name] = [0] * 13
            
            currencies[currency][name][int(month)] += float( amount)
            currencies[currency][name] [0] +=  float(amount)

        # as of 25 dec 2015: Two types of comments. 1. "Withdrawn to: XYZ Bank ..." 2. "Withdraw funds to Bank Account"
        if "ithdraw" in typ:
            totalWithdrawn = totalWithdrawn + float(amount[1:])

    print "\nClient names and total amounts sent by them in a specific currency:\n"
    for c in sorted( currencies, key=currencies.get):
        total = 0
        print "\n%s was received from following clients:\n" % ( c) # EUR/USD

        months = [0]* 12
        currtotal = 0
        for n in sorted( currencies[c], key=currencies[c].get):
            usertotal = 0
            i = 0

            for val in currencies[c][n]:
                logger.debug("name = %s val = %d", n, val)
                if i > 0: #ignore first value
                    usertotal = usertotal + val
                    months[i-1] = months[i-1] + float(val)
                i = i + 1
            print "%30s: %s" % (n, usertotal)
            currtotal = currtotal + usertotal
        print "                ----------------------"
        print "%23s %s: %s\n\n" %( c, " total", currtotal)
        
        print c, "received for each month: \n"
        for mname in monthNames:
            print "%5s" % mname, 
        print ""
        for m in months:
            print "{:5.0f}".format(m),  
        print "\n--------------------------------------------------------------------------------"
    print "\nTotal Withdrawn in local currency = ", totalWithdrawn

if __name__ == "__main__":
    logger.debug('Start script')
    
    if len(sys.argv) <= 1:
        usage()
        exit()

    analyze( sys.argv[1])
