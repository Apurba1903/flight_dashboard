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


SELECT Source, COUNT(*)
FROM (
			SELECT Source
			FROM flightdb
			UNION ALL
			SELECT Destination
			FROM flightdb
) t1
GROUP BY t1.Source
ORDER BY COUNT(*) DESC;


SELECT Date_of_Journey, COUNT(*)
FROM flightdb
GROUP BY Date_of_Journey;


