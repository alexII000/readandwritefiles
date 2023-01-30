# Import
import csv


def main():
    with open("Customers.csv", "r") as in_file:
        reader = csv.reader(in_file)
        next(reader)

        with open("customer_country.csv", "w", newline="") as out_file:
            fieldnames = ["Name", "Country"]
            writer = csv.writer(out_file)
            writer.writerow(fieldnames)
            for row in reader:
                cust_firstn = row[1]
                cust_lastn = row[2]
                cust_country = row[4]
                cust_name = row[1] + " " + row[2]
                customer_full = [cust_name, cust_country]
                writer.writerow(customer_full)


if __name__ == "__main__":
    main()
