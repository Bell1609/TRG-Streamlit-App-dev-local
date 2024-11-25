from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch SQL connection details from .env file
SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USERNAME = os.getenv('SQL_USERNAME')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

# Create the SQLAlchemy engine using pymssql
def get_engine():
    try:
        # Create the connection string for SQLAlchemy using pymssql
        connection_string = f"mssql+pymssql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}"
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f"Error creating SQLAlchemy engine: {e}")
        return None

# Create a function to run queries and return a DataFrame
def run_query(query):
    engine = get_engine()
    if engine is not None:
        try:
            # Execute the query and load the result into a DataFrame
            df = pd.read_sql(query, engine)
            return df
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
    else:
        print("Failed to create engine.")
        return None

# Define your SQL query to select all data from FSAllDealsExtraction table
query = """
SELECT *
FROM FSAllDealsExtraction
"""

# Run the query and get the result as a DataFrame
df = run_query(query)

# Export the DataFrame to CSV if query was successful
if df is not None:
    # Export to CSV
    df.to_csv("test.csv", index=False)
    print("All data from the table has been exported to 'test.csv'")
else:
    print("No data returned or query failed.")
