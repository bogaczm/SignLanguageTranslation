# Using openCV to get multile mask and no mask images from webcam
import cv2
import json
from PIL import Image
import requests
import math

# Save Img as temp
def saveTmp(img):
    file_name = "C:/Users/moko/OneDrive/Studia/MagisterkaINF/sem2/AzureAI/SignLanguageTranslation/src/images/tmp/tmp.jpg"
    cv2.imwrite(file_name, img)
    return file_name

# Sending request
def sendRequest(img_path, img):
    analyze_url = 'https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/c96024d9-0574-44cb-9f1a-33ba0cb131ce/detect/iterations/Iteration4/image'

    # save as bit representation
    img_data = open(img_path, "rb").read()

    headers = {'Prediction-key': '82d7181a581f40f88432e6b8f4a4a9a9',
               'Content-Type': 'application/octet-stream'}
    params = {'numTagsPerBoundingBox': '1'}
    response = requests.post(analyze_url, headers=headers, params=params, data=img_data)
    response.raise_for_status()

    analysis = response.json()

    return analysis

# Analyse the API answer [JSON]
def getInfoData(json_file):
    probability = json_file['predictions'][0]['probability']
    tag_name = json_file['predictions'][0]['tagName']
    bbox = json_file['predictions'][0]['boundingBox']

    return probability, tag_name, bbox
            
# Change the image based on the 
def showOnImg(image, tag_name, probability, bbox):
    HEIGHT, WIDTH, _ = image.shape

    left = math.floor(bbox['left'] * WIDTH)
    top = math.floor(bbox['top'] * HEIGHT)
    width = math.floor(bbox['width'] * WIDTH)
    height = math.floor(bbox['height'] * HEIGHT)

    identyfication_str = tag_name+' '+str(probability)
    if probability>0.7:
        cv2.putText(image, identyfication_str, (left, top-5), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2, cv2.LINE_AA)
        cv2.rectangle(image, (left, top), (left+width, top+height), (0,0,255), 1)

# Video stream
wideo = cv2.VideoCapture(0)

# analysis loop
while(wideo):
    _, ramka = wideo.read()

    cv2.imshow('You',ramka)

    # q - take image for analysis
    # ESC - wyjscie z programu
    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

    elif k == ord('q'):
        print('Pobrano zdjęcie do analizy')
        ramka_analiza = ramka.copy()
        
        file_path = saveTmp(ramka_analiza)
        response = sendRequest(file_path, ramka_analiza)
        probability, tag_name, bbox = getInfoData(response)
        showOnImg(ramka_analiza, tag_name, probability, bbox)

        cv2.imshow('Img for analysis', ramka_analiza)



wideo.release()       
cv2.destroyAllWindows()