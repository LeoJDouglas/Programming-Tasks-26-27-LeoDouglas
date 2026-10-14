"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    file = open("meantemp_daily_totals.txt", "r")

    highest = -9999.0
    lowest = 9999.0
    av = []

    for line in file:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        # Skip header line: "Date Value"
        try:
            value = float(parts[-1])
        except ValueError:
            continue

        # Track highest/lowest
        if value > highest:
            highest = value
        if value < lowest:
            lowest = value

        av.append(value)

    if len(av) == 0:
        print("ERROR: No numeric values found.")
        return

    average = sum(av) / len(av)

    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)
    pass


if __name__ == "__main__":
    main()
