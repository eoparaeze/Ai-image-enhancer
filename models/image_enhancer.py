import cv2
import numpy as np

def enhance_image(image_path):
    image = cv2.imread(image_path)
    enhanced = cv2.detailEnhance(image, sigma_s=10, sigma_r=0.15)
    
    cv2.imshow("Enhanced Image", enhanced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    enhance_image("samples/sample.jpg")
