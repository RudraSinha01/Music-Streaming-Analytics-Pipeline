# Real-Time Music Streaming Analytics Pipeline

## Overview
This project builds a music streaming analytics pipeline using MongoDB, Kafka, and Databricks. The pipeline processes 299 music streaming records, scales the `streams` column by 100 million, and computes the average streams per genre. The goal was to implement real-time streaming, but due to persistent connectivity issues with Kafka, the pipeline was completed in batch mode, with an attempt at streaming logic.

## Results
### Batch Mode Results
#### Visualization
Horizontal bar chart showing the top 20 genres by average streams, with Jazz/Big Band leading at 1.936 billion streams.

![Top 20 Genres by Average Streams (Batch)](avg_streams_per_genre_batch.png)

#### Average Streams per Genre (Batch)
| Genre                       | Avg Streams (Billions) |
|-----------------------------|------------------------|
| Jazz/Big Band               | 1.936                  |
| Bubblegum Pop               | 1.732                  |
| Pop/Classic                 | 1.716                  |
| Folk Rock                   | 1.688                  |
| Instrumental/Easy Listening | 1.561                  |
| Soul/Pop                    | 1.537                  |
| R&B/Hip Hop                 | 1.465                  |
| Rock and Roll/Soul          | 1.454                  |
| Rock and Roll/Pop           | 1.446                  |
| Rock and Roll               | 1.435                  |
| Latin Rock                  | 1.371                  |
| Swing/Jazz                  | 1.367                  |
| Pop/Funk                    | 1.365                  |
| Country/Pop                 | 1.348                  |
| Rock                        | 1.249                  |
| Country/Western             | 1.237                  |
| Psychedelic Rock            | 1.202                  |
| New Wave/Disco              | 1.197                  |
| New Wave                    | 1.161                  |
| Country/Folk                | 1.151                  |

### Streaming Mode Attempt
- **Implementation**: Attempted to process the `music_streaming_events` topic in real-time using Spark Structured Streaming with a 1-minute tumbling window to compute average streams per genre.
- **Challenge**: Encountered persistent `TimeoutException` errors (`Timed out waiting for a node assignment. Call: describeTopics`) due to Kafka connectivity issues between Databricks and the Kafka broker (`bore.pub:9093`).
- **Resolution**: Stabilized Kafka by resolving log rotation errors, but streaming still failed due to network or configuration issues. Reverted to batch mode to complete the project, with a simulated streaming approach as a fallback.

## Notebooks
- [Batch Notebook](Music_Streaming_Analytics_Batch.ipynb): Contains the batch logic to read data from Kafka, compute average streams per genre, and visualize the results.
- [Streaming Notebook (Attempt)](Music_Streaming_Analytics_Streaming.ipynb): Contains the attempted streaming logic, which faced connectivity issues.

## Challenges and Solutions
- **Bore Tunnel Port Conflict**: Encountered "port already in use" on `bore.pub:9092`. Resolved by switching to `bore.pub:9093`.
- **Kafka Timeout in Streaming**: Streaming queries in Databricks timed out. Switched to batch mode to get results, attempted streaming with increased timeouts, but ultimately couldn’t resolve connectivity issues.
- **Kafka Log Rotation Error**: Encountered `log4j:ERROR Failed to rename [C:\Kafka/logs/controller.log]`. Resolved by renaming the log file and fixing permissions.
- **Plot Overcrowding**: Initial bar chart had 73 genres, causing overlapping labels. Fixed by using a horizontal bar chart and limiting to the top 20 genres.

## Future Improvements
- Resolve Kafka streaming connectivity by hosting Kafka on a cloud provider (e.g., AWS MSK) to avoid local tunneling issues.
- Integrate a database sink (e.g., MongoDB) to store results for further analysis.
- Add more metrics, such as top artists or time-based trends.
