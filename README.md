# PayPal-Analytics-Script
Analyze your PayPal history using this script

This script has been tested using Python 2.7

It takes a PayPal transaction csv file as first argument, and then outputs
the amounts sent by every sender, in different currencies. It also shows
the total that was withdrawn to your bank account.

To run this script, you need Python on your computer. The easiest way to install Python is Anaconda installer; its miniconda installer is only 30 MB.

#Usage

python paypalAnalyze.py PayPalTransactionsFile.csv

To get/create the PayPalTransactionsFile.csv, log in to your PayPal account.
Then follow Activity -> Statements -> Activity Export
Select the time period desired, and in File Type, select Comma Delimited - All Activity
Click Download. The file downloaded is the input file to this script, to be given as first command line argument 

#Hire or Donate

This script was written to help all freelancers, businesses, sellers etc who use PayPal. 
If you find it useful, consider hiring me or donating at my PayPal address prg4hire@gmail.com
My bitcoin address is 18LNpmGtgFA2NGnQr4w7miNKfRB29ny5ot



data is lists of binaries.

opcode, symbol for compiled language, stack changes

# values opcodes

opcode | literal | action | comment
--- | --- | --- | --- 
0 | int |  -- X  | the next 32 bits = 4 bytes are put on the stack as a single binary.
2 | binary |  N -- L  | the next N * 8 bits are put on the stack as a single binary.


# other opcodes

opcode | literal | action | comment
--- | --- | --- | --- 
10 | print | ( Y -- X ) | prints the top element on stack
11 | crash |    |code stops execution here. Whatever is on top of the stack is the final state.



