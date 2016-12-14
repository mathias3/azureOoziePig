DROP TABLE IF EXISTS weather;

CREATE EXTERNAL TABLE weather
(year INT,
 month INT,
 max_temp FLOAT,
 min_temp FLOAT,
 frost_days INT,
 rainfall FLOAT,
 sunshine_hours FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE LOCATION '/data/convertedweather';
