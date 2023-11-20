import cv2
import numpy as np

if __name__ == '__main__':
    win_name = "Real-time Features"
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        _, frame = cap.read()
        # frame = np.fliplr(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # FAST Detector
        detector = cv2.FastFeatureDetector_create()
        keypoints = detector.detect(gray)

        # Extract edges with Canny
        edges = cv2.Canny(gray, 50, 200, 3)
        img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        # Draw keypoints
        img = cv2.drawKeypoints(img, keypoints, None)

        # Extract lines with Hough
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, 50, 10)
        for l in lines:
            l = l[0]
            cv2.line(img, 
                     (l[0], l[1]), 
                     (l[2], l[3]), 
                     (0, 0, 255))
        
        # Display the resulting frame
        cv2.imshow(win_name, img)
    
        # Get pressed key
        key = cv2.waitKey(1)

        # Conditions to break loop
        pressed_esc = key == 27
        window_hidden = cv2.getWindowProperty(win_name, cv2.WND_PROP_VISIBLE) <= 0

        # If shoud close, break from loop
        if(pressed_esc or window_hidden):
            break;
