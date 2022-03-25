import cv2
import os

_type= ["img", "border"]


for t in _type:
	count = 0
	imgs = sorted(os.listdir("full_sized/" + t))
	
	for _img in imgs:
		if _img[0] == '.':
			continue

		img = cv2.imread("full_sized/" + t + "/" + _img)

		for i in range(0, img.shape[0], 608):
			for j in range(0, img.shape[1], 608):
				crop = img[i:i+608, j:j+608]
				if crop.shape[0] != 608 or crop.shape[1] != 608:
					count
					continue

				path = "clipped/" + t + "/" + str.zfill(str(count), 5) + ".jpg"

				cv2.imwrite(path, crop)
				print(path)
				count +=1

