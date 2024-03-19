/**
Problem Statement:

Write a query to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.
Sample Input:

Table: cinema
id  movie        desc          rating
1   WAR          great 3D      8.9
2   Science      Fiction       8.5
3  iris          boring        6.2
4  ice song      fantacy       8.6
5  House Card    Interesting    9.1
**/
SELECT *
FROM cinema
WHERE id % 2 != 0 AND LOWER(description) != 'boring'
ORDER BY rating DESC;
