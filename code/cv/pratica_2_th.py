import cv2

if __name__ == '__main__':
    img = cv2.imread('cat_gray.jpg')
    win_name = "Cat"
    value = 0
    type = cv2.THRESH_BINARY
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, 0, 0)

    # Utility functions
    def show():
        _, bin = cv2.threshold(img, value, 255, type)
        cv2.imshow(win_name, bin)

    def change_type(new_value):
        global type
        type = new_value
        show();

    def change_value(new_value):
        global value
        value = new_value
        show()

    # Add sliders
    cv2.createTrackbar("type", win_name, 0, 4, change_type)
    cv2.createTrackbar("value", win_name, 0, 255, change_value)

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