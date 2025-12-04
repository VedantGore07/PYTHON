# PLEASE DO NOT CHANGE THE CODE SKELETON GIVEN. CHANGE ONLY THE NECESSARY PLACES ALONE

import psycopg2

# Read database configuration from the properties file
with open('database.properties') as f:
    lines = [line.strip().split("=", 1) for line in f.readlines() 
             if not line.strip().startswith('#') and line.strip()]
    db = {key.strip(): value.strip() for key, value in lines}

# Create Connection String with error handling
try:
    conn = psycopg2.connect(
        host=db['DB_HOST'],
        user=db['DB_USER'],
        password=db['PGPASSWORD'],
        database=db['DB_SCHEMA']
    )
    print("Database connection successful.")
except psycopg2.OperationalError as e:
    print("Database connection failed.")
    print(f"Error: {e}")
    conn = None   # Ensure None on failure


# ----------------------------------------------------------
# Function 1: Retrieve the Most Recently Published Book
# ----------------------------------------------------------
def get_most_recent_book():
    if conn is None:
        return "Database connection is not available"

    try:
        cursor = conn.cursor()
        query = """
            SELECT title, author, publicationdate
            FROM books
            ORDER BY publicationdate DESC
            LIMIT 1;
        """
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()

        if row:
            title, author, pub_date = row
            # Convert date to YYYY-MM-DD without extra imports
            pub_date = pub_date.isoformat()
            return {
                "title": title,
                "author": author,
                "publication_date": pub_date
            }
        else:
            return "No book records found in the database."

    except Exception as e:
        return f"An error occurred: {e}"


# ----------------------------------------------------------
# Function 2: Identify Books with Limited Copies (< 3)
# ----------------------------------------------------------
def get_books_with_limited_copies():
    if conn is None:
        return "Database connection is not available"

    try:
        cursor = conn.cursor()
        query = """
            SELECT title, author, copiesavailable
            FROM books
            WHERE copiesavailable < 3
            ORDER BY title;
        """
        cursor.execute(query)
        rows = cursor.fetchall()   # fetchall -> get all matching rows
        cursor.close()

        if rows:
            result = []
            for title, author, copies in rows:   # iterate over all rows
                result.append({
                    "title": title,
                    "author": author,
                    "copies_available": copies
                })
            return result
        else:
            return "No books with copies less than 3 found."

    except Exception as e:
        return f"An error occurred: {e}"



# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------
def main():
    # Most Recent Book
    recent = get_most_recent_book()
    print("\nMost Recent Book:\n")

    if isinstance(recent, dict):
        print(f"Title: {recent['title']}\n")
        print(f"Author: {recent['author']}\n")
        print(f"Publication Date: {recent['publication_date']}\n")
    else:
        print(recent + "\n")

    # Books with Limited Copies
    limited = get_books_with_limited_copies()
    print("Books with Limited Copies:\n")

    if isinstance(limited, list):
        for book in limited:
            print(
                f"Title: {book['title']}, "
                f"Author: {book['author']}, "
                f"Copies Available: {book['copies_available']}"
            )
    else:
        print(limited)


if __name__ == "__main__":
    try:
        main()
    finally:
        if conn is not None:
            conn.close()
            print("\nDatabase connection closed")


