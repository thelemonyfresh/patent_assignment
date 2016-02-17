# patent_assignment
Parse patent assignment data from the USPTO, compile list of top assignors, assignees, and top keywords from assigned patent titles.

Obtain patent assignment XML records from Reed Tech (http://trademarks.reedtech.com/assignment.php), published daily. Unpack the .zip file, and then pass the path of the "adYYYYMMDD.xml" file. More info at http://danielporter.ca/blog/?p=43.

The script prints the top 20 words most frequently occurring in assigned patent titles, and the top assignors/assignees for a given dat.

Example usage: 

python assignment.py ad20140512.xml

Output:
On 20140512 there are a total of 395 assignment records.

Top 20 assigned patent title tokens:
1 magnetic
2 dynamic
3 surgical
4 disk
5 row
6 layers
7 content
8 amplification
9 flash
10 program
11 rod
12 rise
13 novel
14 headgear
15 categories
16 delivery
17 splitter
18 respiratory
19 sensor
20 solution

Top 20 assignees (by number of assignment records)
1 MIRACOR MEDICAL SYSTEMS GMBH
2 SONOS, INC.
3 INVENTOR HOLDINGS, LLC
4 YUKON MEDICAL, LLC
5 ENKI TECHNOLOGY, INC.
6 STC.UNM
7 BULLARD SPINE, LLC
8 FORO ENERGY, INC.
9 INVOTRON AS
10 BIO-RAD LABORATORIES INC.
11 NOVARTIS VACCINES AND DIAGNOSTICS SRL
12 ALZA CORPORATION
13 INTERNATIONAL BUSINESS MACHINES CORPORATION
14 MACCARRON INDUSTRIES, INC.
15 GOOGLE TECHNOLOGY INC.
16 BECKMAN COULTER, INC.
17 MCEWEN, KATHY
18 INTELLIPACK
19 ACHESON INDUSTRIES, INC.
20 KOP-COAT, INC.

Top 20 assignors (by number of assignment records):
1 SANTOS, ROBERT
2 PHILLIPS, JAMES WILLIAM
3 SHOWA DENKO K.K.
4 SCHÄFER, RALF-PETER
5 XIAO, GUOHUA
6 DATTELBAUM, ANDREW M.
7 ROSS, ALAN S.
8 SEWARD, DAVID
9 SZYMANSKI, CHESTER J.
10 PENG, SONG
11 E.I. DUPONT DE NEMOURS COMPANY
12 KOBLICK, YESHAYA
13 YANO, TETSUYA
14 SCHNEIDER, TIMOTHY W.
15 CYMER, LLC
16 SUN, JEONGHOON
17 CHENG, FUHUA
18 HELLMAN, SCOTT M.
19 ANTHONYSON, ROBERT B.
20 KHO, DAVID CHUANHANKHO
