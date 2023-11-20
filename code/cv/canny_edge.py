import cv2

if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    win_name = "Canny Edge Detection"
    th = 0
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, 0, 0)

    # Utility functions
    def show():
        edges = cv2.Canny(img, th, 3 * th)
        cv2.imshow(win_name, edges)

    def change_th(new_value):
        global th
        th = new_value
        show();

    # Add sliders
    cv2.createTrackbar("th", win_name, 0, 255, change_th)

    show();
    while True:
        # Get pressed key
        key = cv2.waitKey(1)

        # Conditions to break loop
        pressed_esc = key == 27
        window_hidden = cv2.getWindowProperty(win_name, cv2.WND_PROP_VISIBLE) <= 0

        # If shoud close, break from loop
        if(pressed_esc or window_hidden):
            break;