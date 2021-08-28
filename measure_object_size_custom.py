from object_detector import *
import numpy as np
import getmaxfromlist
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

def Measuredim(inputimage_path,op_image_path):
    
    # Load Aruco detector

    parameters = cv2.aruco.DetectorParameters_create()

    # To create a ArUco Go to https://chev.me/arucogen/
    # Select the 5x5 (50, 100, 250, 1000) in dictionary
    # Print it into a Paper
    # While taling a photo , Make Sure about the presence of the ArUco marker
    # We used 5X5 with perimeter of 20

    # 5X5 - 50 mm is added
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

    # Load Object Detector
    detector = HomogeneousBgDetector()

    # Read and Load Image - Path hot coded
    img = cv2.imread(inputimage_path)

    # Get Aruco marker
    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

    # Draw polygon around the marker
    int_corners = np.int0(corners)
    cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

    # Aruco Perimeter
    aruco_perimeter = cv2.arcLength(corners[0], True)

    # Pixel to cm ratio
    pixel_cm_ratio = aruco_perimeter / 20

    # detect all the contours of an image
    contours = detector.detect_objects(img)

    # Capture the area and contour in seperate list
    mdict_cnt = []
    mdict_area = []

    for cnt in contours:

        # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect
        area = int(w*h)
        mdict_cnt.append(cnt)
        mdict_area.append(area)

    # Get the largest area rectangle
    cnt = getmaxfromlist.getmaxfun(mdict_area, mdict_cnt)

    # Draw objects boundaries
    # for cnt in contours:

    # Get rect from the large bounding box
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    object_width = w / pixel_cm_ratio
    print('object_width - ', object_width)

    # 95 % accuracy
    # object_width = object_width*.960
    # print('96 % - of object_width - ', object_width)


    object_height = h / pixel_cm_ratio
    print('object_height - ', object_height)
    # object_height = object_height*.960
    # print('96 % - of object_height - ', object_height)

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)

    width_cm = "Width {} cm".format(round(object_width, 1))
    height_cm = "Height {} cm".format(round(object_height, 1))
    
    # Write text items
    cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(
        x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(
        x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)


    # cv2.imshow("Image", img)
    # cv2.waitKey(0)

    cv2.imwrite(op_image_path, img)

    # Open the Images
    img = mpimg.imread(op_image_path)
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.title(width_cm +" / "+ height_cm)
    plt.show()
