SELECT * FROM levelupapi_gametype;

SELECT * FROM auth_user;

SELECT * FROM authtoken_token;

SELECT * FROM levelupapi_events;

SELECT * FROM 

SELECT g.id,
    g.gametype_id,
    g.name,
    g.maker,
    g.game_creator_id,
    g.number_of_players,
    g.skill_level
FROM levelupapi_games g