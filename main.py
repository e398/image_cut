import cv2
global img
global point1, point2

def image_cut(action, x, y, flags, param):
    global img, point1, point2
    img = cv2.imread('5807568.jpg')
    img2 = img.copy()

    if action == cv2.EVENT_FLAG_LBUTTON:
        point1 = (x, y)

    elif action == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # Hold left button and drag
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
        cv2.imshow('image', img2)

    elif action == cv2.EVENT_LBUTTONUP:
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
        cv2.imshow('image', img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        cut_img = img[min_y:min_y + height, min_x:min_x + width]
        cv2.imwrite('img_n.jpg', cut_img)


def main():
    img = cv2.imread('5807568.jpg')
    cv2.putText(img, 'Move the mouse and cut out the image',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2);
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', image_cut)
    cv2.waitKey(0) & 0xFF


if __name__ == '__main__':
    main()

