import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_query(connection, query, args=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, args)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def main():
    host_name = 'your_host'
    user_name = 'your_username'
    user_password = 'your_password'
    db_name = 'your_db_name'

    connection = create_server_connection(host_name, user_name, user_password, db_name)

    # Task 1: Insert data
    insert_members = """
    INSERT INTO Members (id, name, age) VALUES
    (1, 'Jane Doe', 28),
    (2, 'John Smith', 35);
    """
    execute_query(connection, insert_members)

    insert_workout_sessions = """
    INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES
    (1, 1, '2023-10-01', '08:00 AM', 'Yoga'),
    (2, 2, '2023-10-01', '10:00 AM', 'Weightlifting');
    """
    execute_query(connection, insert_workout_sessions)

    # Task 2: Update data
    update_session_time = """
    UPDATE WorkoutSessions 
    SET session_time = '06:00 PM' 
    WHERE member_id = (SELECT id FROM Members WHERE name = 'Jane Doe');
    """
    execute_query(connection, update_session_time)

    # Task 3: Delete data
    delete_member = "DELETE FROM Members WHERE name = 'John Smith';"
    execute_query(connection, delete_member)

    delete_workout_sessions = """
    DELETE FROM WorkoutSessions 
    WHERE member_id = (SELECT id FROM Members WHERE name = 'John Smith');
    """
    execute_query(connection, delete_workout_sessions)

if __name__ == "__main__":
    main()
