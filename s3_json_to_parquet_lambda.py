import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Fetching environment variables
s3_cleansed_layer = os.environ['s3_cleansed_layer']
glue_catalog_db_name = os.environ['glue_catalog_db_name']
glue_catalog_table_name = os.environ['glue_catalog_table_name']
write_data_operation = os.environ['write_data_operation']

def lambda_handler(event, context):
    # Retrieve the bucket name and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # Read JSON file from S3 and create DataFrame
        df_raw = wr.s3.read_json(f's3://{bucket}/{key}')
        
        # Normalize JSON data to extract required columns
        df_normalized = pd.json_normalize(df_raw['items'])
        
        # Write DataFrame to S3 as a Parquet file
        wr_response = wr.s3.to_parquet(
            df=df_normalized,
            path=s3_cleansed_layer,
            dataset=True,
            database=glue_catalog_db_name,
            table=glue_catalog_table_name,
            mode=write_data_operation
        )
        
        return wr_response
    
    except Exception as e:
        print(f"Error processing object {key} from bucket {bucket}: {str(e)}")
        raise e
