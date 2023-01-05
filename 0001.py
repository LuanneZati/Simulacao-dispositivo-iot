import time
from paho.mqtt import client as mqtt_client
import uuid
from random import randint

print("Iniciando")

HOST = ""
PORT = 1883
TOPIC = ""
USER = ""
PASSWD = ""
NSER = ''

def connect_mqtt() -> mqtt_client:
  CLIENT_ID = str(uuid.uuid1())
  def on_connect(client, userdata, flags, rc):
    print("Connecting to broker with client ID '{}'...".format(CLIENT_ID))
    if rc == 0:
      print("Connected to MQTT Broker!")
    else:
      print("Failed to connect, return code %d\n", rc)
  client = mqtt_client.Client(CLIENT_ID)
  client.username_pw_set(USER, PASSWD)
  print('teste')
  client.on_connect = on_connect
  print('teste2')
  client.connect(HOST, PORT)
  return client

def publish(client):
  temp = randint(0,99)
  obj = f'"nser": "{NSER}", "rssi": -42,"temp": {temp},"long": -78.14587, "lat": -85.587459'
  msg = '{' + obj + '}'
  result = client.publish(TOPIC, msg)
  status = result[0]
  if status == 0:
    print(f"Send `{msg}` to topic `{TOPIC}`")
  else:
    print(f"Failed to send message to topic {TOPIC}")
  time.sleep(10)  
def run():
  client = [None] * 100
  for x in range(0, 100):
    client[x] = connect_mqtt()
    client[x].loop_start()
    publish(client[x])
  while True:
    for x in range(0, 100):
      client[x].loop_start()
      publish(client[x])
      print(x)
    
if __name__ == '__main__':
  run()

