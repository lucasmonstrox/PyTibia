
import cv2
import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
import cv2

def result_pos_draw(image, result_position, name, color_bgr = (255, 255, 0), thickness=2):
    path = f"{currentPath}/validation_images/{name}"
    x, y, width, height = result_position
    cv2.rectangle(image, (x, y), (x+width, y+height), color_bgr, thickness)
    cv2.imwrite(path, image)