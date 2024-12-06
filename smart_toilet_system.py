class SmartToiletSystem:
    def __init__(self):
        self.sensors = {
            "water_level": 100,
            "temperature": 25,
            "occupancy": False
        }
        self.alerts = []

    def check_sensors(self):
        self.alerts = []  # Clear previous alerts
        if self.sensors["water_level"] < 50:
            self.alerts.append("Low water level detected!")
        if self.sensors["temperature"] > 30:
            self.alerts.append("High temperature detected!")
        if not self.sensors["occupancy"]:
            self.alerts.append("No occupancy detected!")

    def send_alerts(self):
        if self.alerts:
            for alert in self.alerts:
                print(f"ALERT: {alert}")
        else:
            print("All systems are functioning normally.")

toilet_system = SmartToiletSystem()
toilet_system.check_sensors()
toilet_system.send_alerts()
