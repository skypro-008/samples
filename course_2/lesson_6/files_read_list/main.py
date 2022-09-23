filename = "data.txt"

with open(filename, "r") as f:
    records = [line.strip() for line in f]

print(records)

