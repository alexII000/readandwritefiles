import csv


def main():

    with open("sales.csv", "r") as in_file:
        reader = csv.reader(in_file)
        next(reader)

        customer_totals = {}

        for row in reader:
            customer_id = row[0]
            subtotal = float(row[3])
            taxamt = float(row[4])
            freight = float(row[5])

            customer_total = subtotal + taxamt + freight

            if customer_id in customer_totals:
                customer_totals[customer_id] += customer_total
            else:
                customer_totals[customer_id] = customer_total

    with open("salesreport.csv", "w") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Customer | " "Total"])

        for customer_id, total in customer_totals.items():
            writer.writerow(
                ["{:>8}".format(customer_id) + "  " + "{:>10.2f}".format(total)]
            )


if __name__ == "__main__":
    main()
