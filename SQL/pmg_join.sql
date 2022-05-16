-- 없어진 기록 찾기
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID is NULL
ORDER BY A.ANIMAL_ID


-- 오랜 기간 보호한 동물(1)
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3