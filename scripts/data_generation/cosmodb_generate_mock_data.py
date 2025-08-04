from azure.cosmos import CosmosClient, PartitionKey
import random
from datetime import datetime, timedelta
from faker import Faker
import time
import argparse
import yaml


# Function to generate and insert booking data into Cosmos DB record by record
def generate_and_insert_booking_data(num_records, customer_ids, faker_object, cosmodb_database_container_object):
    for _ in range(num_records):
        # Create a single record object
        record = {
            'id': faker_object.uuid4(),  # Cosmos DB requires a unique 'id' field
            'booking_id': faker_object.uuid4(),
            'property_id': faker_object.uuid4(),
            'customer_id': random.choice(customer_ids),
            'owner_id': faker_object.uuid4(),
            'check_in_date': faker_object.date_this_year().strftime('%Y-%m-%d'),
            'check_out_date': (faker_object.date_this_year() + timedelta(days=random.randint(1, 14))).strftime('%Y-%m-%d'),
            'booking_date': faker_object.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': round(random.uniform(50, 1000), 2),
            'currency': random.choice(['USD', 'EUR', 'GBP', 'CAD']),
            'property_location': {
                'city': faker_object.city(),
                'country': faker_object.country()
            },
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Insert each record individually into the Cosmos DB container
        cosmodb_database_container_object.create_item(body=record)
        print(f"Inserted record: {record}")
        
        # Sleep for a short time to simulate real-time data insertion
        time.sleep(5)


def main(args):
    # Initialize Cosmos DB Client
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    cosmodb_url = config['cosmosdb']['url']
    cosmodb_key = config['cosmosdb']['key']
    cosmodb_client_object = CosmosClient(cosmodb_url, credential = cosmodb_key)

    # Database and Container setup
    database_name = config['cosmosdb']['database_name']
    container_name = config['cosmosdb']['database_container_name']

    # Create the CosmosDB database's container object to insert rows into it
    cosmodb_database_object = cosmodb_client_object.create_database_if_not_exists(id=database_name)
    cosmodb_database_container_object = cosmodb_database_object.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/booking_id"),
        offer_throughput=200
    )

    # Define the parameters for the bookings data
    customer_ids = list(range(1, 101))
    records = args.records

    # Initialize Faker
    faker_object = Faker()

    # Insert records into the CosmosDB database's container
    generate_and_insert_booking_data(records, customer_ids, faker_object, cosmodb_database_container_object)


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Define arguments
    parser.add_argument("--records", type=int, required=True, help="Number of records to insert into the CosmosDB database's container")

    # Parse the arguments
    args = parser.parse_args()

    main(args)
