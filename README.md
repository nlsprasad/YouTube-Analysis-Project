# YouTube Analysis Project

## Overview
This project is designed to manage, streamline, and analyze structured and semi-structured YouTube video data based on video categories and trending metrics. The project emphasizes data security, scalability, and effective cloud-based processing.

## Project Goals
1. **Data Ingestion** — Develop a mechanism to ingest data from various sources.
2. **ETL System** — Transform raw data into a structured format suitable for analysis.
3. **Data Lake** — Create a centralized repository for storing data from multiple sources.
4. **Scalability** — Ensure that the system scales efficiently as data volume increases.
5. **Cloud-Based Processing** — Leverage AWS to handle large datasets and enable cloud computing.
6. **Reporting** — Build a dashboard to provide insights and answer predefined analytical questions.

## AWS Services Utilized
1. **Amazon S3** — Scalable object storage with high data availability, security, and performance.
2. **AWS IAM** — Identity and Access Management to securely control access to AWS services and resources.
3. **Amazon QuickSight** — A serverless, machine learning-powered BI tool for cloud-based data visualization.
4. **AWS Glue** — Serverless data integration service for discovering, preparing, and combining data.
5. **AWS Lambda** — A compute service that allows code execution without the need for server management.
6. **AWS Athena** — An interactive query service for S3, allowing data analysis without loading data into another service.

## Dataset
The dataset used in this project is sourced from Kaggle and contains daily statistics on popular YouTube videos from multiple regions. Up to 200 trending videos are recorded daily for each region. The dataset includes:
- **Video Information**: title, channel title, publication time, tags, views, likes, dislikes, description, comment count
- **Category Information**: category_id (region-specific and included in a JSON file associated with each region)

**Link to Dataset**: [YouTube Trending Dataset on Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)

## Getting Started

### Prerequisites
- AWS account with permissions to use Amazon S3, IAM, Glue, Lambda, QuickSight, and Athena.
- Basic knowledge of data engineering concepts and cloud computing.

### Installation and Setup
1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/YouTube-Analysis-Project.git
    ```
2. **Set up AWS Resources**:
   - Create and configure S3 buckets for raw and transformed data.
   - Set up IAM roles with necessary permissions for Glue, Lambda, and other AWS services.
3. **Data Ingestion**:
   - Use AWS Glue or custom scripts to pull data from the source and upload it to S3.
4. **ETL Process**:
   - Implement transformation scripts using AWS Glue to format raw data.
5. **Data Analysis and Reporting**:
   - Use AWS Athena to query data stored in S3 and QuickSight to create dashboards.

### Running the Project
Follow the steps in `docs/Setup.md` for detailed instructions on running ETL jobs, querying data, and generating reports.

## Acknowledgments
- [Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new) for providing the YouTube Trending Dataset.
- AWS for providing cloud-based services to facilitate data engineering and analysis.

