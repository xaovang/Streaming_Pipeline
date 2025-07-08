# Streaming Pipeline Project

This project simulates a simple real-time streaming data pipeline using Python. It generates fake user event logs, processes them with a producer-consumer queue pattern, aggregates metrics in real time, and saves results to a CSV file for analysis.

## Features
- Simulates realistic event data in JSON format (user_id, action, timestamp)
- Producer-consumer architecture using Python's queue module
- Real-time ingestion and processing
- Aggregates event counts by action type
- Persists rolling metrics to CSV for easy analysis

## Example Event
```json
{
  "user_id": 123,
  "action": "click",
  "timestamp": "2025-07-07T12:34:56"
}
