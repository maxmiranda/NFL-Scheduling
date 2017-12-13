<?php
$curl = curl_init();
$url = "http://api.sportradar.us/nfl-ot2/seasontd/2014/standings.json?api_key=r3h895sdurxsgr22hwuqbt8u";
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($curl);
$array = json_decode($result,TRUE);
// Below code is for future reference in case you want to deal with how to access the JSON object.
#$headers = array_keys($array["conferences"]["0"]["divisions"]["0"]["teams"]["0"]);
#array_push($headers, "division");
#print_r($headers);

$file = fopen("2014standings.csv", 'w');
$teamCount = 0;
foreach ($array["conferences"] as $conference){ // 0, 1
  $conf = $conference["name"];
  foreach ($conference["divisions"] as $divisions) {
    $division = $divisions["name"];
    foreach ($divisions["teams"] as $team) {
      $teamvals = array();
      $teamkeys = array();
      foreach($team as $key => $value) {
        if (gettype($value) == "string" || gettype($value) == "integer") {
          array_push($teamvals, $value);
          array_push($teamkeys, $key);
        }
        if (gettype($value) == "array") {
          foreach($value as $subkey => $subvalue) {
            if(gettype($subvalue) == "string" || gettype($subvalue) == "integer") {
              array_push($teamvals, $subvalue);
              array_push($teamkeys, $key."_".$subkey);
            }
          }
        }
      }
      if ($teamCount == 0) {
        array_push($teamkeys, "division");
        array_push($teamkeys, "conference");
        fputcsv($file, $teamkeys);
      }
      $teamCount = $teamCount + 1;
      array_push($teamvals, $division);
      array_push($teamvals, $conf);
      fputcsv($file, $teamvals);
    }

  }
}
fclose($file);

curl_close($curl);
?>
