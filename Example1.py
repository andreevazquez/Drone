from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

drone = connect ("udp:127.0.0.1:14551", wait_ready=True)


print ("Pre-arm Checks...")

print ("Ready to arm: ", drone.is_armable)

while not drone.is_armable:
    print("Vehicle is not armable, waiting...")
    time.sleep(1)

print ("WARNING: Arming Motors!")

drone.mode = VehicleMode("GUIDED")
drone.arm = True

print ("Vehicle Armed")

while not drone.armed:
	print("Waiting for arming...")
	time.sleep(1)

print("Taking off!")
drone.simple_takeoff(20)

while True:
	Altitude = drone.location.global_relative_frame.Altitude

	print("Altitude: ", Altitude)

	if Altitude >=20:
	    print("altitude reached")
		break

    time.sleep(1)

