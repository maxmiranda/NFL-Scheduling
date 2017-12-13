from datascience import *

year = 2017

standings = Table.read_table("standings/" + str(year-1) + "standings.csv")
games = Table.read_table("games/games.csv")

same_conference_rotations = {}
same_conference_rotations["NFC North"] = ["NFC East", "NFC South", "NFC West"]#2017 season, divided by 3 = remainder 2
same_conference_rotations["NFC South"] = ["NFC West", "NFC North", "NFC East"]
same_conference_rotations["NFC East"]  = ["NFC North", "NFC West", "NFC South"]
same_conference_rotations["NFC West"] = ["NFC South", "NFC East", "NFC North"]

same_conference_rotations["AFC North"] = ["AFC East", "AFC South", "AFC West"]
same_conference_rotations["AFC South"] = ["AFC West", "AFC North", "AFC East"]
same_conference_rotations["AFC East"] = ["AFC North", "AFC West", "AFC South"]
same_conference_rotations["AFC West"] = ["AFC South", "AFC East", "AFC North"]

opposite_conf_rotations = {}
opposite_conf_rotations["NFC North"] = ["AFC South", "AFC North", "AFC East", "AFC West"] # %4 now should return 0 for 2016 still so let's start with last year
opposite_conf_rotations["NFC South"] = ["AFC West", "AFC East", "AFC South", "AFC North"]
opposite_conf_rotations["NFC East"]= ["AFC North", "AFC West", "AFC East", "AFC South"]
opposite_conf_rotations["NFC West"] = ["AFC East", "AFC South", "AFC North", "AFC West"]

opposite_conf_rotations["AFC North"] = ["NFC East", "NFC North", "NFC West", "NFC South"]
opposite_conf_rotations["AFC South"] = ["NFC North", "NFC West", "NFC South", "NFC East"]
opposite_conf_rotations["AFC East"] = ["NFC South", "NFC East", "NFC North", "NFC West"]
opposite_conf_rotations["AFC West"] = ["NFC West", "NFC South", "NFC East", "NFC North"]
teams = games.group("home").column("home")

eligibles = {}
for team in teams:
    eligibles[team] = []

for team in teams: #adding the rivals from each division
    division = standings.where("alias", team).column("division")
    if division.size == 0:
        print(team)
    tbl = standings.where("division", division).where("alias", are.not_equal_to(team))
    for rival in tbl.column("alias"):
        eligibles[team].append(rival)
        eligibles[team].append(rival)
    same_conf_div = same_conference_rotations[division.item(0)][year % 3]
    for nfc_opponent in standings.where("division",same_conf_div).column("alias"):
        eligibles[team].append(nfc_opponent)
    opp_conf_div = opposite_conf_rotations[division.item(0)][year %4]
    for afc_opponent in standings.where("division", opp_conf_div).column("alias"):
        eligibles[team].append(afc_opponent)
    team_div_rank = standings.where("alias", team).column("rank_division")
    team_conf = standings.where("alias", team).column("conference")
    teams_same_rank = standings.where("rank_division", team_div_rank).where("conference", team_conf).where("alias", are.not_equal_to(team))
    for team_same_rank in teams_same_rank.column("alias"):
        eligibles[team].append(team_same_rank)
print(eligibles)
print(eligibles["MIN"])

games_and_standings = games.join("away", standings ,"alias")#now let's figure out from games which divisions they played
