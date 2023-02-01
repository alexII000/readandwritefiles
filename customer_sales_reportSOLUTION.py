import csv

salesfile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

sales = csv.reader(salesfile, delimiter=",")
outfile.write(
    "CustomerID, Total\n",
)

next(sales)

cust_total = 0
custID = 250

for rec in sales:
    if custID != rec[0]:
        outfile.write(custID + "," + format(cust_total, ".2f") + "\n")
        cust_total = 0
        custID = rec[0]

    subtotal = float(rec[3])
    tax = float(rec[4])
    freight = float(rec[5])
    total = subtotal + tax + freight
    cust_total += total

outfile.close()
