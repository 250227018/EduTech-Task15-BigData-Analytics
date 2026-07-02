# EduTech-Task15-BigData-Analytics


## Tools Used
Python, Pandas, Faker (PySpark simulation)

## Dataset
Large Volume Log Data - 1,00,000 rows generated
Fields: log_id, timestamp, log_level, service, 
user_id, response_time_ms, ip_address, message

## Concepts Covered

### MapReduce Simulation
- MAP Phase: log_level ko key-value pairs mein map kiya
- REDUCE Phase: service + log_level groupby se aggregate kiya

### Big Data 5V Characteristics
| V | Description |
|---|---|
| Volume | 1,00,000 log records |
| Velocity | Real-time logs from 5 services |
| Variety | 8 different data fields |
| Veracity | Structured log levels (INFO/WARNING/ERROR/DEBUG) |
| Value | Error detection + performance monitoring |

## Analysis Performed
1. Log level distribution (MapReduce)
2. Average response time by service
3. Error rate by service
4. Peak hours analysis

## Interview Answers
**What is Big Data?**
Big Data woh data hai jo itna large, fast, aur complex 
hota hai ki traditional tools (Excel, normal databases) 
se process nahi ho sakta. 5V se define hota hai: 
Volume, Velocity, Variety, Veracity, Value.

**Hadoop vs Spark?**
Hadoop disk pe data store karke process karta hai 
(slow but cheaper). Spark RAM mein data rakhta hai 
(100x faster but expensive). 
Real-time processing ke liye Spark better hai, 
batch processing ke liye Hadoop theek hai.
