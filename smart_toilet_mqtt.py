import paho.mqtt.client as mqtt

class SmartToiletMQTT:
    def __init__(self, broker_address="broker.hivemq.com", topic="smart_toilet/alerts"):
        self.sensors = {"water_level": 100, "temperature": 25}
        self.alerts = []
        self.client = mqtt.Client("SmartToiletClient")
        self.broker_address = broker_address
        self.topic = topic

    def connect(self):
        self.client.connect(self.broker_address)

    def check_sensors(self):
        self.alerts = []
        if self.sensors["water_level"] < 50:
            self.alerts.append("Low water level detected!")
        if self.sensors["temperature"] > 30:
            self.alerts.append("High temperature detected!")

    def send_alerts(self):
        for alert in self.alerts:
            self.client.publish(self.topic, alert)

toilet_mqtt = SmartToiletMQTT()
toilet_mqtt.connect()
toilet_mqtt.check_sensors()
toilet_mqtt.send_alerts()
