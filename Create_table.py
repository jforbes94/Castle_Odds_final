# import mysql.connector

# mydb = mysql.connector.connect(
#   host="CastleOdds.mysql.pythonanywhere-services.com",
#   user="CastleOdds",
#   password="banjobanjobanjo",
#   database="CastleOdds$default"
# )

CREATE TABLE games (
    game_id varchar(255),
    away_team varchar(255),
    home_team varchar(255),
    start_time datetime,
    sport_key varchar(255),
    sport_title varchar(255)
);