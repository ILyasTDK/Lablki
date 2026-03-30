from connect import connect

def test_connection():
    conn = connect()
    if conn:
        conn.close()
        print("Connection closed")

test_connection()

from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully")

create_table()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Contact {name} added")

def get_all_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

create_table()
insert_from_console()
get_all_contacts()

def insert_from_console():
    ...

import csv

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # пропускаем заголовок
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted")

def get_all_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def search_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s",
        ('%' + name + '%',)
    )
    print(cur.fetchall())
    cur.close()
    conn.close()

def search_by_phone_prefix(prefix):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (prefix + '%',)
    )
    print(cur.fetchall())
    cur.close()
    conn.close()

def update_contact(old_name, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute(
            "UPDATE contacts SET name=%s WHERE name=%s",
            (new_name, old_name)
        )
    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE name=%s",
            (new_phone, old_name)
        )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated")

def delete_contact(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM contacts WHERE name=%s OR phone=%s",
        (value, value)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted")

def menu():
    while True:
        print("""
1. Create table
2. Insert from console
3. Insert from CSV
4. Show all
5. Search by name
6. Search by phone prefix
7. Update
8. Delete
0. Exit
""")
        choice = input("Choose: ")
        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            insert_from_csv("contacts.csv")
        elif choice == "4":
            get_all_contacts()
        elif choice == "5":
            search_by_name(input("Name: "))
        elif choice == "6":
            search_by_phone_prefix(input("Prefix: "))
        elif choice == "7":
            update_contact(
                input("Old name: "),
                input("New name (or leave blank): ") or None,
                input("New phone (or leave blank): ") or None
            )
        elif choice == "8":
            delete_contact(input("Enter name or phone: "))
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()

insert_from_csv("contacts.csv")