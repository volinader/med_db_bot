CREATE TABLE class_mkb(
  id INT,
  name VARCHAR(2000),
  code VARCHAR(2000),
  parent_id INT,
  parent_code VARCHAR(2000),
  node_count INT,
  additional_info VARCHAR(10000)
);
COPY class_mkb
FROM '/var/lib/postgresql/data/pgdata/med_db.csv'
DELIMITER ','
CSV HEADER;