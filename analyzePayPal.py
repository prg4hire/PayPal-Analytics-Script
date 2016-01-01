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

def	addValue( currencies, currency, name, month, amount):
	m = int(month)
	#print "In addvalue name = ", name, " month = ", m, " amount = ", amount
	#print currencies[currency][name]

	val = 0.0
	try:
		val = float(currencies[currency][name][ m])
		#print "val = ", val
	except:
		val = 0.0
    
	val = val + float( amount)

	l = len(currencies[currency][name])
	if( l < m):
		for i in range( l, m):
			currencies[currency][name].append(0)
		currencies[currency][name].append( val)
	else:
		currencies[currency][name][m] = val
	currencies[currency][name] [0] = currencies[currency][name] [0] + float(amount)
	#print currencies[currency][name]
	return currencies

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
        month = date[3:5]
        #print month 
        if currency in currencies:
            if name in currencies[currency]:
            	currencies = addValue( currencies, currency, name, month, amount)
                #currencies[currency][name].insert( int(month) , float(amount))
            else:
            	currencies[currency][name] = list()
            	currencies = addValue( currencies, currency, name, month, amount)
        else:
            currencies[currency] = dict()
            currencies[currency][name] = list()
            currencies = addValue( currencies, currency, name, month, amount)
        
    # as of 25 dec 2015: Two types of comments. 1. "Withdrawn to: XYZ Bank ..." 2. "Withdraw funds to Bank Account"
    if typ.find( "ithdraw") != -1:
        totalWithdrawn = totalWithdrawn + float(amount[1:])

print "\nClient names and total amounts sent by them:\n"
for c in sorted( currencies, key=currencies.get):
    total = 0
    print "\nSent in %s:" % ( c) # EUR/USD

    months = list()
    currtotal = 0
    for n in sorted( currencies[c], key=currencies[c].get):
        usertotal = 0
        i = 0

        for val in currencies[c][n]:
        	#print "name = ", n , " val = ", val
	        if i > 0: #ignore first value
	        	usertotal = usertotal + val
        		l = len( months)
        		if l < i:
        			for j in range( l, i):
        				months.append(0.0)
        			months[i-1] = months[i-1] +  float(val)
        		else:
        			months[i-1] = months[i-1] + float(val)
        	i = i + 1
        print "%30s: %s" % (n, usertotal)
        currtotal = currtotal + usertotal
    print "                ----------------------"
    print "%23s %s: %s\n\n" %( c, " total", currtotal)
    
    print "Money received in", c, "for each month: "
    for mname in monthNames:
    	print "%5s" % mname, 
    print ""
    for m in months:
    	print "{:5.0f}".format(m),  

    print "\n--------------------------------------------------------------------------------"

print "\nTotal Withdrawn in local currency = ", totalWithdrawn
