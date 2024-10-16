import os
from dotenv import load_dotenv
from export_function.export import lambda_handler

# Load the environment variables
load_dotenv()

def test_lambda_function():
    # Mock input event
    event = {
        'taxi_id': '10133',  # Replace with a valid taxi ID from your DB
        'date': '2008-02-02'  # Replace with a date you want to query
    }
    
    # Mock context (not used in this example but required by lambda_handler)
    context = {}
    
    # Invoke the Lambda function
    result = lambda_handler(event, context)
    
    # Output the result
    print(result)

if __name__ == "__main__":
    test_lambda_function()
