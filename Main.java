import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.io.IOException;
import joinery.*;
import java.util.HashMap;
import java.util.Collection;

public class Main {

    public static HashMap<String, ArrayList<String>> eligibles = new HashMap();

    /**
     * Goal of this operation is to create a list of eligible, required and
     * non-eligible games for each club. This can then be used to construct
     * the schedule.
     */
    public static void main(String... args) {
        int yearToSchedule = Integer.parseInt(args[0]);
        DataFrame games;
        DataFrame standings;
        try { // retrieve games
            games = DataFrame.readCsv("games/games.csv");

        } catch (IOException e) {
            System.out.println("games.csv is missing :(");
            games = null;
        }

        try { // retrieve standings
            String yearBefore = Integer.toString(yearToSchedule - 1);
            standings = DataFrame.readCsv("standings/" + yearBefore + "standings.csv");
        } catch (IOException e) {
            standings = null;
            System.out.println("standings file is missing");
        }

        for (Object column : standings.columns()) {
            System.out.println(column);
        }
        List<String> teamNames = games.unique("home").sortBy("home").col("home"); // get all of the team name aliases (E.g. MIN or KC)
        for (String name : teamNames) {
            eligibles.put(name, new ArrayList<String>()); // for each team's alias create an arraylist of the teams they should be playing
        }
        for (String name : teamNames) { // add the division rivals to their schedules
            String division = (String) where(standings, "alias", "are equal to", name).col("division").get(0);
            DataFrame tbl = where(where(standings, "division", "are equal to", division), "alias", "are not equal to", "team");
            for (Object division_rival : tbl.col("alias")) {
                eligibles.get(name).add((String) division_rival);
                eligibles.get(name).add((String )division_rival);
            }
        }
        printList(eligibles.get("MIN"));

    }
    public static void printList(Collection<String> list) {
        for (String item : list) {
            System.out.print(item + " ");
        }
    }

    public static DataFrame where(DataFrame tbl, String col, String predicate, String val) {
        DataFrame result = new DataFrame();
        if (predicate.equals("are equal to")) {
            int count = 0;
            for (Object item : tbl.col(col)) {
                if (item.equals(val)) {
                    result.append(tbl.row(count));
                }
                count += 1;
            }
            return result;
        } else if (predicate.equals("are not equal to")){
            int count = 0;
            for (Object item : tbl.col(col)) {
                if (!item.equals(val)) {
                    result.append(tbl.row(count));
                }
                count += 1;
            }
            return result;
        }
        System.out.println("No predicate matches that command");
        return result;
    }
}

