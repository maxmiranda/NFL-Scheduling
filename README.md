# OperationAtlanta
Hi Levi.

The progression of the project is fairly simple:

1. Who plays who: 

  It turns out it's actually incredibly formulaic who plays who for each year. (See: https://operations.nfl.com/the-game/creating-the-nfl-schedule/), so the first step to be able to test any possible idea of ours, is to be able to automatically calculate who plays who using past games and standings, and simply plugging in a year to our main program.
 
 Thus far I've just used the ProFootballAPI and SportRadar API to be able to access a list of games from 2009 onward and the standings from 2014-2016. I wrote the data that I got from those into games and standings folders respectively (in the form of a csv). Then, I put the data from each of those csvs into the Java equivalent of Python's Panda framework, that way we will be able to manipulate data from csv files incredibly easily. (http://cardillo.github.io/joinery/v1.8/api/reference/joinery/DataFrame.html)

Even though the data was accessed with PHP calls, Java was the obvious choice for actually creating the list of eligible teams for our ability to debug in IntelliJ. 
  
2. Pruning time: 

  The second phase is one of brainstorming precisely what algorithm would be most efficient for figuring out the best allignment of the 256 games in terms of: 
  
  * Mandatory: 
      * Keeping travel distances reasonable from week to week
      * Conforming with the rules laid out by broadcast networks 
          *The Sunday afternoon games are broadcast on Fox (NFC) and CBS (AFC); most games with AFC road teams are shown on CBS, and most of those with NFC road teams are broadcast on Fox.
          * Over the first 16 weeks of the season, Fox and CBS will each get eight doubleheaders — meaning that one will show games during both Sunday afternoon time slots, while the other airs a game in only one. They alternate doubleheader weeks; but not always. While this may result in one network airing doubleheaders on consecutive weeks, the league prevents either network from airing doubleheaders three weeks in a row.
     * Limiting the number of times a team that played the week before has to face a rested team coming off its bye.
     * Limiting the # of consecutive road/ home games to two
     * Specifics: 
        * Teams on the road Mondays must be @ Home the next week.
        * Teams scheduled to play on Thursday nights will not have to play on a short week more than once a season. 
* Us: 
    * Putting the most interesting games in the Primetime slots 
        * (Really think we should use some form of Natural Language Processing on Twitter to analyze which games fans would be most excited to see here, just for the sake of pitching the product) 
    * Balancing the TV Schedules for each network in terms of inteerest in games
    
3. Test basic abililty to create a schedule.

4. Get information from Stubhub's API to take into account conflict. 

5. Enable custom input of conflicts that will be taken into account in the schedule. 

6. Play our hands with customizations like Sentiment Analysis on games.
