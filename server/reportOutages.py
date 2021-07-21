import mysql.connector
import time
import random

db = mysql.connector.connect(
    host="localhost",
    user="testuser",
    password="test123",
    database='netmonitordb')
if db.is_connected():
    print("Successfully connected to Network KPI Database")
print("Network Probe Active")
print("Reading Network Metrics...")

cursor = db.cursor(buffered=True)

def updateOutages(severity, link):
    query =f"INSERT INTO `outages`(`severity`, `link`) VALUES ('{severity}','{link}')"
    cursor.execute(query)
    db.commit()
    print(f"Report: Link: {link}, Severity: {severity}")


def reportOutages():
    while True:
        query = "TRUNCATE TABLE outages"
        cursor.execute(query)
        outs = random.randint(10,15)
        links = ['A-B','B-C','C-D','D-E','E-F','F-G','G-H','H-I','I-J','J-K','K-L','A-C','A-D','A-F','A-L','B-K','C-F','C-G','G-L','J-H']
        random.shuffle(links)
        for x in range(outs):
            severities = ['Warning','Minor','Major','Critical']
            sevNum = random.randint(0,3)
            updateOutages(severities[sevNum], links[x])
        print(f"Total Alarms: {outs}")
        time.sleep(60)

if __name__ == "__main__":
    reportOutages()