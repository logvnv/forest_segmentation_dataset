import cv2
import os

category = ["train", "val", "test"]
_type= ["", "_mask", "_border"]


for t in _type:
	count = 0
	for cat in category:
		imgs = sorted(os.listdir("full_sized/" + cat + t))
		
		for _img in imgs:
			if _img[0] == '.':
				continue

			img = cv2.imread("full_sized/" + cat + t + "/" + _img)

			for i in range(0, img.shape[0], 608):
				for j in range(0, img.shape[1], 608):
					crop = img[i:i+608, j:j+608]
					_t = "img"
					if len(t) > 0:
						_t = t[1:]

					print("clipped/" + _t + "/" + str(count) + ".png")

					cv2.imwrite("clipped/" + _t + "/" + str(count) + ".png", crop)
					count +=1

