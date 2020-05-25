from PIL import Image
import numpy as np
import os
from tensorflow.keras.utils import Sequence


class ImageGenerator(Sequence):
	def __init__(self):
		pass

	def on_epoch_end(self):
		pass

	def __len__(self):
		pass

	def __getitem__(self, item):
		pass


def load_images(dir):
	'''
	loads all the image file in a directory
	:param dir: the parent directory of images
	:return: images loaded as PIL image files
	'''
	images = []
	for subdir in os.listdir(dir):
		for filename in os.listdir(os.path.join(dir, subdir)):
			image = Image.open(os.path.join(dir, subdir, filename)).convert('RGB')
			images.append(np.asarray(image))
	return np.stack(images)


if __name__ == '__main__':
	raw_images = load_images('small_data')
