# PayPal-Analytics-Script
Analyze your PayPal history using this script

This script has been tested using Python 2.7

It takes a PayPal transaction csv file as first argument, and then outputs
the amounts sent by every sender, in different currencies. It also shows
the total that was withdrawn to your bank account.

This script was written to help all freelancers, businesses, sellers etc who use PayPal. 
If you find it useful, consider hiring me or donating at my gmail/PayPal address prg4hire@gmail.com
My bitcoin address is 1JVM63khCnZbi36i3w2pbXWgKJ1VaRLP9o

#Usage

python analyzePayPal.py PayPalTransactionsFile.csv

To get/create the PayPalTransactionsFile.csv, log in to your PayPal account.
Then follow Activity -> Statements -> Activity Export
Select the time period desired, and in File Type, select Comma Delimited - All Activity
Click Download. The file downloaded is the input file to this script, to be given as first command line argument 

