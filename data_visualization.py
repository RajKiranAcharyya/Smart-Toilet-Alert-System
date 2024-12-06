import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5]  
water_level = [100, 90, 70, 45, 30]  
temperature = [25, 27, 29, 30, 35]  

plt.figure(figsize=(10, 5))
plt.plot(time, water_level, label="Water Level (%)", marker="o")
plt.plot(time, temperature, label="Temperature (°C)", marker="x")
plt.title("Smart Toilet Sensor Data")
plt.xlabel("Time (hours)")
plt.ylabel("Sensor Readings")
plt.legend()
plt.grid()
plt.show()
