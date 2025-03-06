import sqlite3

def connect_db():
    return sqlite3.connect("library.db")

def create_books_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    """)

def insert_books_data(cursor):
    data = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", data)

def update_book_year(cursor):
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

def query_books_genre(cursor):
    genre = input("Enter Genre to search: ")
    result = cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", (genre,))
    print(f"\nBooks in Genre: {genre}")
    for row in result:
        print(row)

def delete_old_books(cursor):
    cursor.execute("DELETE FROM Books WHERE Year_Published <= 1950")

def add_books_rating_column(cursor):
    cursor.execute("PRAGMA table_info(Books);")
    columns = [column[1] for column in cursor.fetchall()]
    if "Rating" not in columns:
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

def update_books_ratings(cursor):
    cursor.executemany("""
        UPDATE Books SET Rating = ? WHERE Title = ?
    """, [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ])

def display_sorted_books_by_year(cursor):
    result = cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print("\nBooks sorted by Year Published:")
    for row in result:
        print(row)

def main():
    with connect_db() as conn:
        cursor = conn.cursor()
        
        while True:
            print("""
            1. Create table
            2. Insert data
            3. Update data
            4. Query data
            5. Delete data
            6. Add column
            7. Update column
            8. Advanced Query data
            9. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                create_books_table(cursor)
            elif choice == "2":
                insert_books_data(cursor)
            elif choice == "3":
                update_book_year(cursor)
            elif choice == "4":
                query_books_genre(cursor)
            elif choice == "5":
                delete_old_books(cursor)
            elif choice == "6":
                add_books_rating_column(cursor)
            elif choice == "7":
                update_books_ratings(cursor)
            elif choice == "8":
                display_sorted_books_by_year(cursor)
            elif choice == "9":
                break
            else:
                print("Invalid choice, try again.")
            conn.commit()

if __name__ == "__main__":
    main()
