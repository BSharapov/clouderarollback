SELECT * FROM
    (SELECT productname, 
            buyprice, 
            productline,
            ROW_NUMBER() OVER(PARTITION BY productline ORDER BY buyprice DESC) AS rownumber
    FROM products
    WHERE buyprice IS NOT NULL) 
WHERE rownumber <= 5;
