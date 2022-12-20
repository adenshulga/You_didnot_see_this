import cv2

temp_img = cv2.imread("frame_00_delay-0.08.png")

a1 = []
for i in range(0, 9):
    a1.append('0{}'.format(i))
  

for i in a1[1:]:
    temp_img = cv2.hconcat([temp_img, cv2.imread("frame_{}_delay-0.08s.png".format(i))])



cv2.imshow('aaaaaa', temp_img)