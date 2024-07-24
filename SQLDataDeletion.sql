-- Deleting John Smith's record from Members table
DELETE FROM Members WHERE name = 'John Smith';

-- Deleting John Smith's workout sessions
DELETE FROM WorkoutSessions WHERE member_id = (SELECT id FROM Members WHERE name = 'John Smith');
