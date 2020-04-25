import time
import board
import busio
import adafruit_tmp006
import adafruit_vl53l0x

#TMP006{
# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tmp006.TMP006(i2c)

# Initialize communication with the sensor, using the default 16 samples per conversion.
# This is the best accuracy but a little slower at reacting to changes.
# The first sample will be meaningless
while True:
    obj_temp = sensor.temperature
    print('Object temperature: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)))
    time.sleep(5.0)
#}

#vl53l0x{
# Will print the sensed range/distance every second.



# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c, 40)

while True:
    print('Range: {0}mm'.format(vl53.range))
    time.sleep(1.0)
#}