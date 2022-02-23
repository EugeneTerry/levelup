SELECT * FROM levelupapi_gametype;

SELECT * FROM auth_user;

SELECT * FROM authtoken_token;

SELECT * FROM levelupapi_events;

SELECT * FROM levelupapi_games

SELECT
    g.id,
    g.name,
    g.maker,
    g.gametype_id,
    g.number_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_games g
JOIN
    levelupapi_gamer gr ON g.game_creator_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id