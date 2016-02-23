# patent_assignment: Daily Patent Assignment Trends

This script allows the user to parse patent assignment data from the USPTO, compile list of top assignors, assignees, and top keywords from assigned patent titlnnnes on a given day.

## How to Use

Obtain patent assignment XML records from [Reed Tech](http://trademarks.reedtech.com/assignment.php), published daily. Unpack a .zip file, and then pass the path of the "adYYYYMMDD.xml" file to the script. More info on my [blog post](http://danielporter.ca/blog/?p=43).

The script prints the top 20 words most frequently occurring in assigned patent titles, and the top assignors/assignees for a given date.

### Example usage: 
```
wget http://trademarks.reedtech.com/downloads/PatentAssignmentText/2016/ad20160101.zip
unzip ad20160101.zip
python assignment.py ad20160101.xml
```


### Output:
On 20160101 there are a total of 199 assignment records.


Top 20 assigned patent title tokens:


1. resistance
2. surgical
3. chair
4. semiconductor
5. weakening
6. methyl
7. thiazolecarboxamides
8. treating
9. cable
10. transmission
11. force
12. pulse
13. power
14. thickness
15. cell
16. delivering
17. water
18. operating
19. janus
20. military


Top 20 assignees (by number of assignment records):


1. COLORADO ENERGY RESEARCH TECHNOLOGIES, LLC
2. VYNCA, LLC
3. ACER INCORPORATED
4. XGENE PHARMACEUTICAL INC.
5. INTERNATIONAL BUSINESS MACHINES CORPORATION
6. AGIO INTERNATIONAL COMPANY, LTD.
7. DIC CORPORATION
8. CMC MAGNETICS CORP.
9. LG CHEM, LTD.
10. BIOTIUM, INC.
11. INSTITUT PASTEUR
12. ENDOCARE, INC.
13. LIFE SCIENCE INSTITUTE, LLC
14. INTEGRATED HEALING TECHNOLOGIES, LLC
15. SURVIVA LINK CORPORATION
16. BAYER HEALTHCARE LLC
17. ROHDE & SCHWARZ GMBH & CO. KG
18. GEMALTO SA
19. AMAANI, LLC
20. GYNAECOLOGIC PTY LTD


Top 20 assignors (by number of assignment records):


1. PICA, FRANCESCO
2. CHEW, HONG MENG ALAN
3. SHINTANI, KOICHI
4. BRILLHART, PAUL
5. KAGE, TAKAKAZU
6. ARMSTRONG, PETER MICHAEL
7. SHELKE, ANIL MARUTI
8. GROENKE, ALLEN W.
9. BOYD, EDWARD
10. HIROSE, SHIMPEI
11. BENWARE, SHEILA
12. GOLD STANDARD SIMULATIONS LTD.
13. MBDA DEUTSCHLAND GMBH
14. LETOCART, PHILIPPE
15. NAZARIAN, HAGOP
16. THE UNIVERSITY OF HONG KONG
17. SWARTZ, TANYA L.
18. STENDAHL, GARY B.
19. KIM, JOO-SANG
20. O'BRIEN, BENJAMIN MARC
