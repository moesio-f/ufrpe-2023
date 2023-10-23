import cv2

if __name__ == '__main__':
    img = cv2.imread('cat_gray.jpg')
    f_hat = cv2.GaussianBlur(img, (21, 21), 10.0)
    win_name = "Cat"
    A = 1.0
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, 0, 0)

    # Utility functions
    def show():
        global f_hat
        Af = cv2.convertScaleAbs(img, alpha=A)
        r = cv2.subtract(Af, f_hat)
        cv2.imshow(win_name, r)

    def update_A(new_value):
        global A
        A = 1.0 + (new_value / 10)
        show();

    # Add sliders
    cv2.createTrackbar("A", win_name, 0, 30, update_A)

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