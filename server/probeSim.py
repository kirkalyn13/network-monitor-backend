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

def updateVoice(callSR, callDR, callDelay):
    query = f"INSERT INTO `voicelogs`(`callSR`, `callDR`,`callDelay`) VALUES ('{callSR}','{callDR}','{callDelay}')"
    cursor.execute(query)
    db.commit()
    print(f"Voice KPIs: Call SR: {callSR}, Call DR: {callDR}, Call Delay: {callDelay}")

def updateSMS(smsMOSR, smsMTSR, smsDelay):
    query = f"INSERT INTO `smslogs`(`smsMOSR`, `smsMTSR`,`smsDelay`) VALUES ('{smsMOSR}','{smsMTSR}','{smsDelay}')"
    cursor.execute(query)
    db.commit()
    print(f"SMS KPIs: SMS MO SR: {smsMOSR}, SMS MT SR: {smsMTSR}, SMS Delay: {smsDelay}")

def updateData(attachSR, dltput, latency, users):
    query = f"INSERT INTO `datalogs`(`attachSR`, `dltput`,`latency`,`users`) VALUES ('{attachSR}','{dltput}','{latency}','{users}')"
    cursor.execute(query)
    db.commit()
    print(f"Data KPIs: Attach SR: {attachSR}, DL TPut: {dltput}, Latency: {latency}, Camped Users: {users}")



def runProbe():
    print("Simulate Random Metrics...")
    while True:
        callsr = round(random.uniform(90,95),2)
        calldr = round(random.uniform(0.5,3),2)
        calldelay = random.randint(2000,5000)
        smsmosr = round(random.uniform(97.5,99),2)
        smsmtsr = round(random.uniform(97.5,99),2)
        smsdelay = random.randint(2000,3000)
        attachsr = round(random.uniform(70,80),2)
        dltput = round(random.uniform(10,30),2)
        latency = random.randint(30,50)
        users = random.randint(50,200)
        updateVoice(callsr, calldr, calldelay)
        updateSMS(smsmosr, smsmtsr, smsdelay)
        updateData(attachsr, dltput, latency, users)
        time.sleep(60)


if __name__ == "__main__":
    runProbe()