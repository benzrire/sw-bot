import module as _

import matplotlib as plt
import numpy as np
import cv2
import base64

def main():
	# display screen
	display = [0, 14, 556, 328]

	# startButton = [minx, miny, maxx, maxy]
	startButton = [420, 220, 520, 260]

	# "Reward" position
	rewardWord = [245, 117, 314, 142]

	# "Revive" position
	reviveWord = [190, 209, 242, 229]

	# touch screen
	touchScreen = [90, 90, 465, 280]

	# chest box
	chestBox = [220, 155, 325, 250]

	# intersection between ok button and sell button
	okSellButton = [243, 259, 266, 269]

	# prepare button
	prepareButton = [320, 260, 338, 269]

	counter = 1

	while True:
		_.randomDelay(4000, 6000)

		print('\n\nBattle round {}'.format(counter))

		# check setting page
		(count, percentage) = _.imageCompare(_.captureRegion(display), _.getImageFromStatic('setting-page.png'))
		print('setting-page match {} %'.format(percentage))
		if percentage > 70:
			_.mMoveTo(startButton, 0.1)
			_.mClick('left')

			# check case
			while True:
				_.randomDelay(4000, 6000)

				#  victory case
				if _.ocr(_.captureRegion(rewardWord)) == 'Reward':
					print('Victory!')
					
					while True:
						# click screen
						_.mMoveTo(touchScreen, 0.1)
						_.mClick('left')
						_.randomDelay(4000, 5000)

						# check chest box
						(count, percentage) = _.imageCompare(_.captureRegion(display), _.getImageFromStatic('chest.png'))
						print('chest box match {} %'.format(percentage))

						if percentage > 50:
							break
						else:
							continue
					

					while True:
						# click chest box
						_.mMoveTo(chestBox, 0.1)
						_.mClick('left')
						_.randomDelay(4000, 5000)

						# check chest box again
						(count, percentage) = _.imageCompare(_.captureRegion(display), _.getImageFromStatic('chest.png'))
						print('chest box match {} %'.format(percentage))

						if percentage > 50:
							continue
						else:
							break

					while True:
						# click ok sell button
						_.mMoveTo(okSellButton, 0.1)
						_.mClick('left')
						_.randomDelay(4000, 5000)

						# check last page of victory sequence
						(count, percentage) = _.imageCompare(_.captureRegion(display), _.getImageFromStatic('victory-last.png'))
						print('victory-last match {} %'.format(percentage))

						if percentage > 50:
							break
						else:
							continue

					while True:
						# click prepare button
						_.mMoveTo(prepareButton, 0.1)
						_.mClick('left')
						_.randomDelay(4000, 5000)

						# check setting page
						(count, percentage) = _.imageCompare(_.captureRegion(display), _.getImageFromStatic('setting-page.png'))
						print('setting-page match {} %'.format(percentage))

						if percentage > 50:
							break
						else:
							continue

					counter += 1
					break

				# defeated case
				if _.ocr(_.captureRegion(reviveWord)) == 'Revive':
					print('Defeated..')
					break

if __name__ == '__main__':
	main()