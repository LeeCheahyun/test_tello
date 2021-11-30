from djitellopy import Tello

tello = Tello()

tello.connect()


# move

import cv2

panel = cv2.imread('./tello.jpg')
cv2.imshow('tellopanel', panel)
# tello.move_up(150)
# tello.move_forward(90)
# tello.move_right(100)
# tello.move_back(120)
# tello.move_left(120)
# tello.query_battery()
while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    elif key == ord('u'):
        tello.move('up', 50)
    elif key == ord('w'):
        tello.move('forward', 50)
    elif key == ord('s'):
        tello.move('back', 50)
    elif key == ord('d'):
        tello.move('right', 50)
    elif key == ord('a'):
        tello.move('left', 50)
    elif key == ord('j'):
        tello.move('down', 50)
    elif key == ord('b'):
        tello.query_battery()
pass