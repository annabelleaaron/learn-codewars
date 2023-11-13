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


-- OPPOSITES ATTRACT
select flower1, flower2,
    case
        when flower1 % 2 <> flower2 % 2 then true
        else false
    end as res
from love


-- REMOVE FIRST AND LAST CHARACTER
select s, substring(s, 1, length(s) - 2) as res from removechar


-- FAKE BINARY
select x, translate(x, '123456789', '000011111') as res from fakebin
select x, regexp_replace(regexp_replace(x, '[0-4]', '0', 'g'), '[5-9]', '1', 'g') as res from fakebin
-- my solution, definitely not a solution
select x, replace(replace(replace(replace(replace(replace(replace(replace(replace(x, '1', '0'), '2', '0'), '3', '0'), '4', '0'), '5', '1'), '6', '1'), '7', '1'), '8', '1'), '9', '1') as res from fakebin


-- KEEP HYDRATED!
select *, floor(hours * 0.5) as liters from cycling


-- GRASSHOPPER - MESSI GOALS FUNCTION
select (la_liga_goals + copa_del_rey_goals + champions_league_goals) as res from goals


-- EVEN OR ODD
select number,
  case
    when number%2 = 0 then 'Even'
    else 'Odd'
  end as is_even
from numbers


-- GRASSHOPPER - TERMINAL GAME MOVE FUNCTION
select (position + roll + roll) as res from moves


-- SQL BASICS: SIMPLE WHERE AND ORDER BY
select * from people
where age > 50
order by age desc


-- DISEMVOWEL TROLLS
select str, regexp_replace(str, '[aeiou]', '', 'ig') res from disemvowel
-- my solution
select str, translate(str, 'aeiouAEIOU', '') as res from disemvowel


-- SQL BASICS: SIMPLE JOIN AND COUNT
select p.id, p.name, count(t.id) as toy_count
from people as p
left join toys as t on p.id = t.people_id
group by p.id


-- REGEX REPLACE
select project, commits, contributors, regexp_replace(address, '[0-9]', '!', 'g') as address from repositories


-- STRANGE PRINCIPAL
select n, floor(sqrt(n))::integer as res from numofopenlockers


-- EASY SQL: MOVING VALUES
select 
  length(name) as id, 
  length(legs::text) as name, 
  length(arms::text) as legs, 
  length(characteristics) as arms, 
  length(id::text) as characteristics 
from monsters


-- SQL BASICS: RAISE TO THE POWER
select power(number1, number2) as result from decimals


-- THIRD ANGLE OF A TRIANGLE
select a, b, (180-a-b) as res from otherangle


-- REGEX STRING TO TABLE
select regexp_split_to_table(text, E'[aeiou]') as results from random_string


-- SQL WITH SAILOR MOON: THINKING ABOUT JOINS...
select s.senshi_name as sailor_senshi, s.real_name_jpn as real_name, ct.name as cat, sc.school as school
from sailorsenshi as s
left join cats as ct on ct.id = s.cat_id
left join schools as sc on sc.id = s.school_id
-- join only displays rows that have values, left join includes rows with no values



