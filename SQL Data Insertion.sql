-- Inserting data into Members table
INSERT INTO Members (id, name, age) VALUES (1, 'Jane Doe', 28);
INSERT INTO Members (id, name, age) VALUES (2, 'John Smith', 35);

-- Inserting data into WorkoutSessions table
INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) 
VALUES (1, 1, '2023-10-01', '08:00 AM', 'Yoga');
INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) 
VALUES (2, 2, '2023-10-01', '10:00 AM', 'Weightlifting');
