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
    /** Goal of this operation is to create a list of eligible, required and
     * non-eligible games for each club. This can then be used to construct
     * the schedule. */
    public static void main(String... args) {
        int yearToSchedule = Integer.parseInt(args[0]);
        DataFrame games;
        DataFrame standings;
        try {
            games = DataFrame.readCsv("games/games.csv");

        } catch (IOException e) {
            System.out.println("games.csv is missing :(");
            games = null;
        }

        try {
            String yearBefore = Integer.toString(yearToSchedule - 1);
            standings = DataFrame.readCsv("standings/" + yearBefore +"standings.csv");
        } catch (IOException e) {
            standings = null;
            System.out.println("standings file is missing");
        }
        List<String> teamNames = games.unique("home").sortBy("home").col("home");
        for (String name : teamNames) {
            eligibles.put(name, new ArrayList<String>());
        }
        for (String name: teamNames) {

        }
    }

    public static void printList(Collection<String> list) {
        for (String item : list) {
            System.out.print(item + " ");
        }
    }

}