import cv2
from PIL import Image, ImageOps, ImageFilter
import moviepy.video
import moviepy.video.fx
import pytesseract
import numpy as np
from moviepy import VideoFileClip 


in_file = VideoFileClip("summit_final.mp4")

# gets the frame at specific timestamp in the match as a numpy array
clip = in_file.get_frame(780)
# saves the image as an numpy image
image = Image.fromarray(clip)
# crops the image to player 1's score
player1_score = image.crop([417,18,593,49])
player1_score = ImageOps.invert(player1_score)
player1_score = player1_score.resize([2839,500], Image.Resampling.NEAREST)
player1_score = player1_score.filter(ImageFilter.GaussianBlur(radius= 5))
player1_score = player1_score.convert('L')
player1_score = cv2.threshold(np.array(player1_score), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
player1_score = Image.fromarray(player1_score[1])
#saves the whole image + players scores
image.save("pissnpoo.png")
player1_score.save("player1_score.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(player1_score, lang="eng", config = '--psm 8 -c tessedit_char_whitelist=0123456789')
print(text)
scoreCount = 0
lineCount = 0


score = ""
scores = []
for i in text:

    lines = []
    if i in "0123456789ABCDEF" and len(score) < 6:
        score = score + i
        if len(score) == 6:
            scores.append(score)
    else:
        if score != "":
            score = ""
        
print(scores)

