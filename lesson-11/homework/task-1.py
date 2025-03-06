import sqlite3

def connect_db():
    return sqlite3.connect("roster.db")

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)

def insert_data(cursor):
    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

def update_name(cursor, old_name, new_name):
    cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", (new_name, old_name))

def query_species(cursor, species):
    result = cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", (species,))
    print("Bajoran Characters:")
    for row in result:
        print(row)

def delete_old_entries(cursor):
    cursor.execute("DELETE FROM Roster WHERE Age > 100")

def add_rank_column(cursor):
    cursor.execute("PRAGMA table_info(Roster);")
    columns = [column[1] for column in cursor.fetchall()]
    if "Rank" not in columns:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

def update_ranks(cursor):
    cursor.executemany("""
        UPDATE Roster SET Rank = ? WHERE Name = ?
    """, [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ])

def display_sorted_by_age(cursor):
    result = cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("\nCharacters sorted by Age:")
    for row in result:
        print(row)

def main():
    with connect_db() as conn:
        cursor = conn.cursor()
        create_table(cursor)
        insert_data(cursor)
        update_name(cursor, "Jadzia Dax", "Ezri Dax")
        query_species(cursor, "Bajoran")
        delete_old_entries(cursor)
        add_rank_column(cursor)
        update_ranks(cursor)
        display_sorted_by_age(cursor)
        conn.commit()

if __name__ == "__main__":
    main()
