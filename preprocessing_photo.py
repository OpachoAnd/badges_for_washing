from PIL import Image
from os.path import isfile, join

from PIL import Image
from tqdm import tqdm

TRAIN_DATA_PATH = r'C:\Users\opacho\Documents\dataset_CARE_LABEL_2'
TARGER_DATA_PATH = r'C:\Users\opacho\Documents\dataset_care_label_resize'

def train_images(data_path: str):
    return [f for f in listdir(data_path) if isfile(join(data_path, f))]

def resize_images(path: str, target_path: str):
    list_images = train_images(path)
    for i in tqdm(list_images, 'Resize_Images'):
        img = Image.open(join(path, i))
        new_image = img.resize((256, 256))
        new_image.save(join(target_path, i))

if __name__ == '__main__':
    resize_images(path=TRAIN_DATA_PATH, target_path=TARGER_DATA_PATH)


