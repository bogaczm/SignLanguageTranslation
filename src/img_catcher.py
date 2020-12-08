# Using openCV to get multile mask and no mask images from webcam
import cv2
# UUID i so everyone can create data without name collisions
import uuid

# Video stream
wideo = cv2.VideoCapture(0)

# Name generation
IMG_PATH = './images/'


# analysis loop
while(wideo):
    _, ramka = wideo.read()

    cv2.imshow('Your Face',ramka)

    # q - no mask
    # w - wrong mask save
    # e = good mask
    # ESC - wyjscie z programu
    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

    elif k == ord('q'):
        name = 'ILY_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('i'):
        name = 'i_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('l'):
        name = 'l_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('y'):
        name = 'y_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('a'):
        name = 'a_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('b'):
        name = 'b_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('c'):
        name = 'c_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))

    elif k == ord('o'):
        name = 'o_'+str(uuid.uuid1())
        img_path = IMG_PATH+name+'.jpg'
        cv2.imwrite(img_path, ramka)
        print('Img saved as: {}'.format(name))    

wideo.release()       
cv2.destroyAllWindows()