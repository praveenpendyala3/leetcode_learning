import math

cust_data = {}   #Create an empty customer lookup database in memory
f = open("inputs.csv", "r+")
for line in f:
    line = line.strip() # Remove all unnecessary whitespaces and newline characters at beginning and end of line. 
    
    if line == "" or line ==",,": # Continue to next line if current line is empty
        continue

    # Get important data as strings and integer numbers
    cust_id,date,amount = line.split(",")[0], line.split(",")[1], int(line.split(",")[2])

    # Create new customer entry for a new customer
    if cust_id not in cust_data:
        cust_data[cust_id]={}
    if date not in cust_data[cust_id]:
        cust_data[cust_id][date] = [0,0] # Credits, Debits

    # Calculate and update daily credits and debits
    if amount>=0:
        cust_data[cust_id][date][0]+=amount # Add Credits
    else:
        cust_data[cust_id][date][1]+=amount # Add debits
f.close()

# Create an empty monthly report information to be displayed later
cust_monthly = {}
for customer in cust_data:
    cust_monthly[customer]={}
    dates = sorted(cust_data[customer].keys())
    balance = 0
    for date in dates:
        month = date.split("/")[0] + "/" + date.split("/")[2] #Get month information

        if month not in cust_monthly[customer]: # New month
            balance = 0
            cust_monthly[customer][month] = [math.inf,-math.inf,0] # Min balance, Max balance, Total balance
        
        credit = cust_data[customer][date][0]
        debit = cust_data[customer][date][1]

        balance = balance + credit + debit #
        if balance <  cust_monthly[customer][month][0]:
            cust_monthly[customer][month][0] = balance
        if balance > cust_monthly[customer][month][1]:
            cust_monthly[customer][month][1] = balance
        cust_monthly[customer][month][2] = balance

# Output the monthly database 
ostring = ""
for customer in cust_monthly:
    for month in cust_monthly[customer]:
        ostring += ",".join([customer, month, str(cust_monthly[customer][month][0]), str(cust_monthly[customer][month][1]), str(cust_monthly[customer][month][2])]) + "\n"
with open("outputs.csv","w+") as f:
    f.write(ostring[:-1])    
