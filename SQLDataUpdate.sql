-- Updating workout session time for Jane Doe
UPDATE WorkoutSessions 
SET session_time = '06:00 PM' 
WHERE member_id = (SELECT id FROM Members WHERE name = 'Jane Doe');
