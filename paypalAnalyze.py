#!/usr/bin/python 

# This script has been tested using Python 2.7

# It takes a PayPal transaction csv file as first argument, and then outputs
# the amounts sent by every sender, in different currencies. It also shows
# the total that was withdrawn to your bank account.

# This script was written to help all freelancers, businesses, sellers etc who use PayPal. 
# If you find it useful, consider hiring me or donating at my gmail/PayPal address prg4hire@gmail.com
# My bitcoin address is 1JVM63khCnZbi36i3w2pbXWgKJ1VaRLP9o

import csv, sys
def usage():
    print "Usage:\n\nanalyzePayPal.py PayPalTransactionsFile.csv\n"
    print ""
    print "To get/create the PayPalTransactionsFile.csv, log in to your PayPal account."
    print "Then follow Activity -> Statements -> Activity Export"
    print "Select period, and in File Type, select Comma Delimited - All Activity"
    print "Click Download. The file downloaded is the input file to this script, to be given as first command line argument"   

if len(sys.argv) <= 1:
    usage()
    exit()

try:
    csvlines = csv.reader(open(sys.argv[1], "r"))
except:
    print "Could not open file", sys.argv[1]
    usage()
    exit()

totalWithdrawn = 0
currencies = dict(dict())    # main key is currency. Then client name is the key, and the amount sent by them is stored as value
for date,time, timezone, name, typ, status, currency, amount, receiptid,empty, balance in csvlines:
    amount = amount.replace(",", "") # change numbers from 1,123 to 1123

    if "Payment Received" in typ or "eCheque Received" in typ:
        if "Update" in typ:    # some transactiions are updattes, such as update that echeque cleared. We ignore these.
            continue 
        if currency in currencies:
            if name in currencies[currency]:
                currencies[currency][name] = currencies[currency][name] + float(amount)
            else:
                currencies[currency][name] = float(amount)
        else:
            currencies[currency] = dict()
            currencies[currency][name] = float(amount)
        
    # as of 25 dec 2015: Two types of comments. 1. "Withdrawn to: XYZ Bank ..." 2. "Withdraw funds to Bank Account"
    if typ.find( "ithdraw") != -1:
        totalWithdrawn = totalWithdrawn + float(amount[1:])

print "\nClient names and total amounts sent by them:\n"
for c in sorted( currencies, key=currencies.get):
    total = 0
    print "%s" % ( c)
    for n in sorted( currencies[c], key=currencies[c].get):
        total = total + currencies[c][n]
        print "%30s: %s" % (n, currencies[c][n])
    print "                ----------------------"
    print "%23s %s: %s" %( c, " total", total)
         
print "\nTotal Withdrawn in local currency = ", totalWithdrawn
