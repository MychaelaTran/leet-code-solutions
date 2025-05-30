# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person p 
LEFT OUTER JOIN Address a ON p.personID = a.personID

#if person has no address report null