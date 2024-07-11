import csv

# Read the CSV file and extract unique weapon names
unique_weapons = set()
with open('Database\skindata.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        weapon_name = row[2].strip()
        if weapon_name:
            unique_weapons.add(weapon_name)

# Generate SQL insert statements
insert_statements = []
for weapon_name in unique_weapons:
    insert_statements.append(f"INSERT INTO Collections (Collection_Name) VALUES ('{weapon_name}');")

# Output the SQL insert statements
for statement in insert_statements:
    print(statement)
