import csv
import codecs
import sqlite3

# Custom error handler that replaces undecodable bytes with '?'
def replace_with_questionmark(exception):
    if not isinstance(exception, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exception)
    return ('?', exception.start + 1)

# Register the custom error handler
codecs.register_error('replace_with_questionmark', replace_with_questionmark)

def fetch_id(cursor, table_name, column_name, value):
    cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name} = ?", (value,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

def generate_insert_statements(file_path, db_path, skin_name_header, weapon_header, rarity_header, collection_header, min_float_header, max_float_header, stattrak_header):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(file_path, mode='r', newline='', encoding='utf-8', errors='replace_with_questionmark') as csvfile:
        reader = csv.DictReader(csvfile)
        print("CSV Headers:", reader.fieldnames)

        for row in reader:
            try:
                def clean_string(s):
                    return ''.join(['?' if ord(c) > 127 else c for c in s])

                skin_name = clean_string(row[skin_name_header])
                weapon_name = row[weapon_header]
                rarity_name = row[rarity_header]  
                collection_name = row[collection_header]
                min_float = row[min_float_header]
                max_float = row[max_float_header]
                stattrak = row[stattrak_header]

                # Fetch IDs for weapon, rarity, and collection
                weapon_id = fetch_id(cursor, "Weapons", "Weapon_Name", weapon_name)
                rarity_id = fetch_id(cursor, "Rarity", "Rarity_Name", rarity_name)
                collection_id = fetch_id(cursor, "Collections", "Collection_Name", collection_name)

                if weapon_id and rarity_id and collection_id:
                    insert_statement = (
                        "INSERT INTO Skins (Skin_Name, WeaponID, RarityID, CollectionID, Min_Float, Max_Float, Is_Stattrak) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)"
                    )
                    cursor.execute(insert_statement, (skin_name, weapon_id, rarity_id, collection_id, min_float, max_float, stattrak))
                else:
                    print(f"Missing ID for row: {row}")
                
            except KeyError as e:
                print(f"KeyError: {e} - Row: {row}")
            except sqlite3.Error as e:
                print(f"SQLite error: {e} - Row: {row}")

        conn.commit()
        conn.close()

db_path = 'Database/DATA.db'
file_path = 'Database/skindata.csv'
skin_name_header = 'Skin'
weapon_header = 'Weapon'
rarity_header = 'Rarity'
collection_header = 'Collection'
min_float_header = 'Min_Float'
max_float_header = 'Max_Float'
stattrak_header = 'Is_Stattrak'
generate_insert_statements(file_path, db_path, skin_name_header, weapon_header, rarity_header, collection_header, min_float_header, max_float_header, stattrak_header)
