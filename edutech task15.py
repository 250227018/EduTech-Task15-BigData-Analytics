import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import time

fake = Faker()

# ─── PART 1: Large Volume Logs generate karo ───────────────────────────────
print("=== Generating Large Volume Log Data ===")

log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
services = ['AuthService', 'PaymentService', 'UserService', 'OrderService', 'NotificationService']

logs = []
base_time = datetime(2024, 1, 1)

for i in range(100000):  # 1 lakh rows = large volume
    logs.append({
        'log_id': i + 1,
        'timestamp': base_time + timedelta(seconds=random.randint(0, 86400*30)),
        'log_level': random.choice(log_levels),
        'service': random.choice(services),
        'user_id': random.randint(1000, 9999),
        'response_time_ms': random.randint(10, 5000),
        'ip_address': fake.ipv4(),
        'message': random.choice([
            'Request processed successfully',
            'Connection timeout',
            'Authentication failed',
            'Database query executed',
            'Payment processed',
            'User logged in',
            'Session expired',
            'Rate limit exceeded'
        ])
    })

df = pd.DataFrame(logs)
df.to_csv('large_volume_logs.csv', index=False)
print(f"Dataset created: {len(df)} rows, {len(df.columns)} columns")
print(f"File size: ~{df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB in memory")

# ─── PART 2: MapReduce Simulation ──────────────────────────────────────────
print("\n=== MapReduce Simulation ===")

# MAP Phase: Key-Value pairs banao
print("\n[MAP Phase] - Mapping log_level to count...")
start = time.time()
mapped = df['log_level'].value_counts()
map_time = time.time() - start
print(mapped)
print(f"Map time: {map_time:.4f} seconds")

# REDUCE Phase: Aggregate karo
print("\n[REDUCE Phase] - Reducing by service + log_level...")
start = time.time()
reduced = df.groupby(['service', 'log_level']).size().reset_index(name='count')
reduce_time = time.time() - start
print(reduced.head(10))
print(f"Reduce time: {reduce_time:.4f} seconds")

# ─── PART 3: Big Data Analysis ─────────────────────────────────────────────
print("\n=== Big Data Analysis ===")

# Average response time by service
print("\n[1] Avg Response Time by Service:")
avg_response = df.groupby('service')['response_time_ms'].mean().round(2)
print(avg_response)

# Error rate by service
print("\n[2] Error Rate by Service:")
error_rate = df[df['log_level'] == 'ERROR'].groupby('service').size()
total = df.groupby('service').size()
error_pct = (error_rate / total * 100).round(2)
print(error_pct)

# Peak hours analysis
print("\n[3] Peak Hours Analysis:")
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
peak_hours = df.groupby('hour').size().sort_values(ascending=False).head(5)
print(peak_hours)

# Save results
reduced.to_csv('mapreduce_output.csv', index=False)
avg_response.to_csv('avg_response_time.csv')
print("\nAll results saved!")

# ─── PART 4: 5V Summary ────────────────────────────────────────────────────
print("\n=== Big Data 5V Characteristics ===")
print(f"Volume    : {len(df):,} log records generated")
print(f"Velocity  : Real-time logs from {len(services)} services")
print(f"Variety   : {len(df.columns)} different data fields")
print(f"Veracity  : Log levels (INFO/WARNING/ERROR/DEBUG)")
print(f"Value     : Error detection, performance monitoring")
print("\nDone!")