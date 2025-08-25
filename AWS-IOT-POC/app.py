import csv
import json
import time
from awscrt import mqtt
from awsiot import mqtt_connection_builder

# AWS IoT endpoint and certs
ENDPOINT = "a2lgtrntxmx70z-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "My-IoT-Device-100"
PATH_TO_CERT = "./certificates/device-cert.pem.crt"
PATH_TO_KEY = "./certificates/device-private.pem.key"
PATH_TO_ROOT = "./certificates/AmazonRootCA1.pem"

TOPIC = "test/device"
CSV_FILE = "CSV-Data.csv"

# Build MQTT connection
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERT,
    pri_key_filepath=PATH_TO_KEY,
    ca_filepath=PATH_TO_ROOT,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30
)

print("Connecting...")
mqtt_connection.connect().result()
print("✅ Connected!")

# Read CSV and publish rows
with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)  # Reads CSV header into dict keys
    for row in reader:
        message = {
            "deviceId": CLIENT_ID,
            "timestamp": row["timestamp"],
            "temperature": float(row["temperature"]),
            "humidity": float(row["humidity"])
        }
        mqtt_connection.publish(
            topic=TOPIC,
            payload=json.dumps(message),  # JSON format
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        print(f"📡 Sent: {message}")
        time.sleep(2)  # Wait 2 sec before sending next row

mqtt_connection.disconnect().result()
print("🔌 Disconnected!")

