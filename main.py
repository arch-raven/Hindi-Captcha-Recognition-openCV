import os
import cv2
import numpy as np

from classifier import ClassifierInference
from segmentation import character_segmentation


clf = ClassifierInference(
    model_state_path="torch_model.pt", labels_map_json_path="labels2devchar.json"
)


def predict(image):
    """
    input: RGB image of shape (X,Y,3)
    pass plot_images=True, to plot the segmented images
    """
    seg_imgs = character_segmentation(image, plot_images=False)
    answer = []
    for img in seg_imgs:
        answer.append(clf.predict(img))
    return answer
