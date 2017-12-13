from datascience import *
'''
This is a script to receive the unordered schedule for every team for a
particular year. The script uses UC Berkeley's original datascience module to
read standings in from csv files and interpret the information within.

Only thing left with this step is to figure out a way to convert this into a
Java HashMap<String, ArrayList> to continue with the project in Java. 
'''
year = 2017

standings = Table.read_table("standings/" + str(year-1) + "standings.csv")

same_conference_rotations = {}
same_conference_rotations["NFC North"] = ["NFC East", "NFC South", "NFC West"]
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
teams = standings.column("alias")

eligibles = {}
for team in teams:
    eligibles[team] = []

for team in teams:
    #below we are adding the rivals from each division
    division = standings.where("alias", team).column("division")
    rivals = standings.where("division", division).where("alias", are.not_equal_to(team)).column("alias")
    for rival in rivals:
        eligibles[team].append(rival)
        eligibles[team].append(rival)

    #below we are adding the division of the same conference that a team plays
    same_conf_div = same_conference_rotations[division.item(0)][year % 3]
    for nfc_opponent in standings.where("division",same_conf_div).column("alias"):
        eligibles[team].append(nfc_opponent)

    #below we are adding the division of the opposing conference that a team plays
    opp_conf_div = opposite_conf_rotations[division.item(0)][year %4]
    for afc_opponent in standings.where("division", opp_conf_div).column("alias"):
        eligibles[team].append(afc_opponent)

    #below we are adding the two remaining games to the schedule by
    #selecting the two teams with the same division rank from the last year
    #that this team has not played yet
    team_div_rank = standings.where("alias", team).column("rank_division")
    team_conf = standings.where("alias", team).column("conference")
    teams_same_rank = standings.where("rank_division", team_div_rank).where("conference", team_conf).where("alias", are.not_equal_to(team))
    for team_same_rank in teams_same_rank.column("alias"):
        eligibles[team].append(team_same_rank)

print(eligibles["KC"]) #Look familiar?
