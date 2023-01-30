import csv


def main():
    with open("EmployeePay.csv", "r") as in_file:
        reader = csv.reader(in_file, skipinitialspace=True)

        for row in reader:
            print(row[0], row[1], row[2], row[3], row[4])


if __name__ == "__main__":
    main()
