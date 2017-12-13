<?php

$url = 'https://profootballapi.com/schedule';

$api_key = 'VuJintgmsOqcEZNKGdYyjMS0C5Hx4Qep';

$query_string = 'api_key=' . $api_key;

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);

curl_setopt($ch, CURLOPT_POSTFIELDS, $query_string);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);


$result = curl_exec($ch);

$myJSON = json_decode($result, true);

$headers = array_keys($myJSON[0]);

$file = fopen("games.csv", 'w');
fputcsv($file, $headers);


$firstLineKeys = false;
foreach ($myJSON as $game){
  $values = array_values($game);
  fputcsv($file, $values);
}
fclose($file);

curl_close($ch);

?>
