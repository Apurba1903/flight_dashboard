USE flightdb;
SELECT * FROM flightdb;


SELECT DISTINCT(Source)
FROM flightdb
UNION
SELECT DISTINCT(Destination)
FROM flightdb;


SELECT Airline, Route, Dep_Time, Duration, Total_Stops, Price
FROM flightdb
WHERE Source = 'Banglore' AND Destination = 'Delhi';


SELECT Airline, COUNT(*)
FROM flightdb
GROUP BY Airline;

