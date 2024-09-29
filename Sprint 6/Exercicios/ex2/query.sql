WITH Decadas AS (
    SELECT 
        nome,
        SUM(total) AS total, 
        (FLOOR(ano / 10) * 10) AS decade
    FROM 
        nomes_ano
    WHERE 
        ano >= 1950
    GROUP BY 
        nome, (FLOOR(ano / 10) * 10) 
),
MaisNomes AS (
    SELECT 
        nome,
        total,
        decade,
        ROW_NUMBER() OVER (PARTITION BY decade ORDER BY total DESC) AS rn 
    FROM 
        Decadas
)
SELECT 
    decade,
    nome,
    total
FROM 
    MaisNomes
WHERE 
    rn <= 3
ORDER BY 
    decade, total DESC;