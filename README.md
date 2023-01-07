# dota2-match-data-farmer
 **-Autogenerate JSON data from real Dota 2 matches-**

![ezgif_2_ca4cb50125](https://user-images.githubusercontent.com/116339318/211147011-9c69b4f8-53e0-44b9-aef9-1149a3afac81.gif)

This script uses OpenDota to fetch full match and player data from random Dota 2 matches. <br>
Each match will be saved as its own JSON file {matchId}.json <br>
![image](https://user-images.githubusercontent.com/116339318/211148456-d97ac5af-aa6f-4efd-b0b9-30f2d33fb153.png)

### Note
OpenDota free tier only allows 60 requests/min.<br>
By default 60 requests get sent, then it will cooldown for 1 minute. If you have Premium tier on OpenDota you can change the max requests sent.
