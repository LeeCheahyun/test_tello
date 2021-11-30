from djitellopy import Tello

tello = Tello()

tello.connect()

tello.takeoff()

# move
tello.move_up(150)
tello.move_forward(90)
tello.move_right(100)
tello.move_back(120)
tello.move_left(120)
tello.query_battery()

tello.land()

pass