Technology-stack
---------------- 
Python, Beautiful Soup

Problem Statement
-----------------
- This was a simple assignment to create a script that can scrape the price for a fixed number of stocks (referred to as symbols by the client).
- The price would be the latest price at the time the script was executed.
- The symbols were stored in a text file (symbols.txt) and can be altered without modifying the actual script
- This input text file should reside at the same location as that of the script file.
- The output file contains the Timestamp, Symbol, Price

Example:
- Input Sumbol: QCGRIX
- Output File: 2020-05-05 00:58:27.266049,QCGRIX,230.01
- URL: "https://finance.yahoo.com/quote/QCGRIX"