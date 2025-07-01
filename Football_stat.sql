-- Step 1: Create table with UNIQUE constraint
CREATE TABLE IF NOT EXISTS player_stats (
    player_name TEXT,
    team TEXT,
    goals INTEGER,
    assists INTEGER,
    matches INTEGER,
    minutes INTEGER,
    UNIQUE(player_name, team)
);

-- Step 2: Insert data safely
INSERT OR IGNORE INTO player_stats (player_name, team, goals, assists, matches, minutes) VALUES
('Messi', 'PSG', 20, 15, 30, 2700),
('Haaland', 'MCI', 28, 5, 29, 2600),
('Saka', 'ARS', 14, 11, 30, 2550),
('Mbappe', 'PSG', 25, 7, 30, 2700),
('De Bruyne', 'MCI', 8, 18, 28, 2500),
('Salah', 'LIV', 19, 12, 31, 2800);

-- Step 3: Query example - top 5 players by goal contributions
SELECT player_name, team, goals, assists, (goals + assists) AS goal_contributions
FROM player_stats
ORDER BY goal_contributions DESC
LIMIT 5;