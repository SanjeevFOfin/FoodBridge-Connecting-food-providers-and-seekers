CREATE DATABASE food_wastage;

USE food_wastage;

#1.Quick Sanity check
-- Row counts
SELECT 'providers_data' AS table_name, COUNT(*) AS total_rows FROM providers_data
UNION ALL
SELECT 'receivers_data', COUNT(*) FROM receivers_data
UNION ALL
SELECT 'food_listings_data', COUNT(*) FROM food_listings_data
UNION ALL
SELECT 'claims_data', COUNT(*) FROM claims_data;

#2.View table structures
DESCRIBE providers_data;
DESCRIBE receivers_data;
DESCRIBE food_listings_data;
DESCRIBE claims_data;

#3.Number of unique providers
SELECT COUNT(DISTINCT Provider_ID) AS unique_providers
FROM providers_data;

#4.Number of unique receivers
SELECT COUNT(DISTINCT Receiver_ID) AS unique_receivers
FROM receivers_data;

#5.Most listed food items
SELECT Food_Name, COUNT(*) AS listings_count
FROM food_listings_data
GROUP BY Food_Name
ORDER BY listings_count DESC
LIMIT 5;

#Food Providers & Receivers
#1. How many food providers and receivers are there in each city?
SELECT City, 
       COUNT(DISTINCT Provider_ID) AS Total_Providers,
       COUNT(DISTINCT Receiver_ID) AS Total_Receivers
FROM (
    SELECT City, Provider_ID, NULL AS Receiver_ID FROM providers_data
    UNION ALL
    SELECT City, NULL AS Provider_ID, Receiver_ID FROM receivers_data
) AS combined
GROUP BY City;

#2.Maximum Providers
SELECT City, COUNT(*) AS Provider_Count
FROM providers_data
GROUP BY City
ORDER BY Provider_Count DESC
LIMIT 1;

#3.Maximum Receivers
SELECT City, COUNT(*) AS Receiver_Count
FROM receivers_data
GROUP BY City
ORDER BY Receiver_Count DESC
LIMIT 1;

#4.Combined Results on Total
SELECT 
    p.City,
    COUNT(DISTINCT p.Provider_ID) AS Provider_Count,
    COUNT(DISTINCT r.Receiver_ID) AS Receiver_Count
FROM providers_data p
LEFT JOIN receivers_data r 
    ON p.City = r.City
GROUP BY p.City
ORDER BY Provider_Count DESC, Receiver_Count DESC;

#5.Combined Results on Maximum counts
SELECT 
    p.City AS Max_Providers_City,
    p.Provider_Count,
    r.City AS Max_Receivers_City,
    r.Receiver_Count
FROM 
    (SELECT City, COUNT(*) AS Provider_Count
     FROM providers_data
     GROUP BY City
     ORDER BY Provider_Count DESC
     LIMIT 1) p
CROSS JOIN
    (SELECT City, COUNT(*) AS Receiver_Count
     FROM receivers_data
     GROUP BY City
     ORDER BY Receiver_Count DESC
     LIMIT 1) r;
     
#6.Which type of food provider contributes the most food?
SELECT Provider_Type, COUNT(*) AS Total_Food_Listings
FROM food_listings_data
GROUP BY Provider_Type
ORDER BY Total_Food_Listings DESC
LIMIT 4;

#7. Contact information of food providers in a specific city (e.g., 'New Carol')
SELECT Name, Contact,Address
FROM providers_data
WHERE City = 'New Carol';

#8. Which receivers have claimed the most food?
SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
FROM claims_data c
JOIN receivers_data r ON c.Receiver_ID = r.Receiver_ID
GROUP BY r.Name
ORDER BY Total_Claims DESC;

#9.Maximumof 10 counts
SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
FROM claims_data c
JOIN receivers_data r ON c.Receiver_ID = r.Receiver_ID
GROUP BY r.Name
ORDER BY Total_Claims DESC
LIMIT 10;

#Food Listings & Availability
#10. Total quantity of food available from all providers?
SELECT SUM(Quantity) AS Total_Quantity_Available
FROM food_listings_data;

#11.Top 10 Providers?
SELECT p.Name AS Provider_Name, 
       SUM(f.Quantity) AS Total_Quantity
FROM food_listings_data f
JOIN providers_data p 
     ON f.Provider_ID = p.Provider_ID
GROUP BY p.Name
ORDER BY Total_Quantity DESC
LIMIT 10;

#12. Which city has the highest number of food listings?
SELECT Location AS City, COUNT(*) AS Total_Listings
FROM food_listings_data
GROUP BY Location
ORDER BY Total_Listings DESC
LIMIT 1;#change limits for top cities listing counts

#13. Most commonly available food types
SELECT Food_Type, COUNT(*) AS Occurrences
FROM food_listings_data
GROUP BY Food_Type
ORDER BY Occurrences DESC;

#Claims & Distribution
#14. How many food claims have been made for each food item?
SELECT f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
GROUP BY f.Food_Name
ORDER BY Total_Claims DESC;

#15. Provider with highest number of successful food claims?
SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
JOIN providers_data p ON f.Provider_ID = p.Provider_ID
WHERE c.Status = 'Completed'
GROUP BY p.Name
ORDER BY Successful_Claims DESC
LIMIT 1;#change limit for top providers name

#16. Percentage of food claims by status?
SELECT Status, 
       COUNT(*) AS Count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims_data), 2) AS Percentage
FROM claims_data
GROUP BY Status;

#Analysis & Insights
#17. Average quantity of food claimed per receiver?
SELECT r.Name, ROUND(AVG(f.Quantity), 2) AS Avg_Quantity_Claimed
FROM claims_data c
JOIN receivers_data r ON c.Receiver_ID = r.Receiver_ID
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
GROUP BY r.Name
LIMIT 10;  # we can remove limits if we need total receivers name and Avg Quantity Claimed.

#18. Which meal type is claimed the most?
SELECT Meal_Type, COUNT(*) AS Claim_Count
FROM claims_data c
JOIN food_listings_data f ON c.Food_ID = f.Food_ID
GROUP BY Meal_Type
ORDER BY Claim_Count DESC
LIMIT 1; # we can change the limits to view all Meal types.

#19. Total quantity of food donated by each provider?
SELECT p.Name, SUM(f.Quantity) AS Total_Donated
FROM food_listings_data f
JOIN providers_data p ON f.Provider_ID = p.Provider_ID
GROUP BY p.Name
ORDER BY Total_Donated DESC; #we can add limits for top 10 providers.

















     
     












