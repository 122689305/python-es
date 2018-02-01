local sensitivity: 36
prelist: [{'male': 4, 'female': 3}, {('Duke', 'General'): 4, ('James', 'Soldeir'): 4, ('Ava', 'Scientist'): 3}, {120: 3, 10: 7, 11: 4}, {1: 10, 2: 7}]
postlist [{('Alice1', '21'): 2, ('Alice5', '21'): 3, ('Adim', '18'): 2, ('Hank', '20'): 2, ('Alice6', '21'): 3, ('Alice', '21'): 3, ('Andrew', '30'): 2}, {'male': 2, 'female': 3}, {('Duke', 'General'): 2, ('Ava', 'Scientist'): 3}, {120: 1, 10: 2, 130: 9}]
preMax: [4, 4, 7, 10]
postMax: [3, 3, 3, 9]
---
databases:
- database: "test"
  dialect: "vertica"
  namespace: "public"
  tables:
  - table: "R0"
    columns:
    - name: "col0"
      maxFreq: 1
    - name: "col1"
      maxFreq: 4
    - name: "col2"
      maxFreq: 4
  - table: "R1"
    columns:
    - name: "col0"
      maxFreq: 2
    - name: "col1"
      maxFreq: 1
    - name: "col2"
      maxFreq: 1
  - table: "R2"
    columns:
    - name: "col0"
      maxFreq: 2
    - name: "col1"
      maxFreq: 2
    - name: "col2"
      maxFreq: 2
  - table: "R3"
    columns:
    - name: "col0"
      maxFreq: 9
    - name: "col1"
      maxFreq: 10

SELECT COUNT(*) FROM R0 JOIN R1 ON R0.col2 = R1.col0 JOIN R2 ON R1.col1 = R2.col0 AND R1.col2 = R2.col1 JOIN R3 ON R2.col2 = R3.col0


Result
====================


PathJoin sensitivity: 36 
Elastic sensitivity: 150.0
