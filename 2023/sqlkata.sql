-- CONVERT BOOLEAN VALUES TO STRINGS 'YES' OR 'NO'
SELECT bool, 
       CASE 
           WHEN bool THEN 'Yes'
           ELSE           'No' 
       END AS res 
FROM booltoword

-- SUM ARRAYS

-- COUNTING SHEEP