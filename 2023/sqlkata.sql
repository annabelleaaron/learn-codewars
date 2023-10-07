-- CONVERT BOOLEAN VALUES TO STRINGS 'YES' OR 'NO'
select bool,
    case -- use case when there is more than one condition
        when bool then 'Yes'
        else 'No'
    end as res
from booltoword

-- SUM ARRAYS

-- COUNTING SHEEP



-- GRASSHOPPER - SUMMATION
select n, n * (n + 1) / 2 as res from kata


-- REVERSED STRINGS
select str, reverse(str) as res from solution