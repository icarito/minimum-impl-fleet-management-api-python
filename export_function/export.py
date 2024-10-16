import os
import boto3
import json
from psycopg import connect, OperationalError
from fleet_api.config import Config

# Initialize S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Load environment variables configured in Config
    env = Config()
    
    # Retrieve taxi ID and date from the event data
    taxi_identifier = event.get('taxi_id')
    date = event.get('date')  # Expected format: 'YYYY-MM-DD'

    if not taxi_identifier or not date:
        raise ValueError("taxi_id and date must be provided")

    # Get database connection
    try:
        connection = connect(conninfo=env.DATABASE_URL)
    except OperationalError as ex:
        print(f"Database connection failed: {ex}")
        raise

    # Fetch trajectories data for the given taxi and date
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT date,latitude,longitude
                   FROM TRAJECTORIES
                   WHERE taxi_id = %s AND CAST(date AS DATE) = %s""",
                (taxi_identifier, date)
            )
            resultset = cursor.fetchall()
            trajectories = [{"date": str(row[0]), 
                             "latitude": row[1], 
                             "longitude": row[2]} for row in resultset]
    except Exception as ex:
        print(f"Failed to fetch data: {ex}")
        connection.close()
        raise

    # Close the database connection
    connection.close()

    # Convert data to JSON
    data = json.dumps(trajectories)

    # Create S3 object key
    object_name = f"{env.S3_OBJECT_PREFIX}taxi_{taxi_identifier}_{date}_trajectories.json"

    # Upload to S3
    try:
        s3_client.put_object(Bucket=env.S3_BUCKET_NAME, Key=object_name, Body=data)
        print(f"Data successfully uploaded to S3 bucket {env.S3_BUCKET_NAME} with key {object_name}")
    except Exception as ex:
        print(f"Failed to upload data to S3: {ex}")
        raise

    return {
        'statusCode': 200,
        'body': json.dumps('Data successfully processed and uploaded!')
    }
