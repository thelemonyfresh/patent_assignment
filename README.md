# patent_assignment
Parse patent assignment data from the USPTO, compile list of top assignors, assignees, and top keywords from assigned patent titles.

Obtain patent assignment XML records from Reed Tech (http://trademarks.reedtech.com/assignment.php), published daily. Unpack the .zip file, and then pass the path of the "adYYYYMMDD.xml" file.

The script prints the top 20 words most frequently occurring in assigned patent titles, and the top assignors/assignees for a given dat.

Example usage: 

python assignment.py ad20160216.xml
