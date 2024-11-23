import csv
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file_name, out_name = sys.argv[1], sys.argv[2]
    if file_name[-4:] == '.csv':
        try:
            read_write(file_name,out_name)
        except FileNotFoundError:
            sys.exit(f"Could not read {file_name}")
    else:
        sys.exit("Not a CSV file")


def read_write(file_name,out_name):
    students = []
    with open(file_name,'r') as f, open(out_name,'w') as o:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(o)
    for row in reader:
        last,first = row["name"].strip().split(', ')
        students.append({"first": first, "last": last, "home": row["home"]})
for student in sorted(students, key=lambda student: student["first"]):
        writer.writeheader()
        writer.writerow({'first_name': {first}, 'last_name':{last}, 'house': {row['house']}})

if __name__ == "__main__":
    main()
