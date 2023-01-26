import mysql.connector

def search_sql(sql_file, search_term):
    # Connect to the SQL database
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    # Open and read the SQL file
    with open(sql_file, "r") as file:
        sql_query = file.read()

    # Replace the placeholder with the user's search term
    sql_query = sql_query.replace("{search_term}", search_term)

    # Execute the SQL query
    cursor = connection.cursor()
    cursor.execute(sql_query)

    # Fetch and print the results
    results = cursor.fetchall()
    for result in results:
        print(result)

    # Close the connection
    cursor.close()
    connection.close()

# Example usage
search_sql("search.sql", "example search term")
