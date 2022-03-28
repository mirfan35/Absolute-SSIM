# Github link: https://github.com/mirfan35/Absolute-SSIM.
# Documentation: http://arqiipubl.com/ojs/index.php/AMS_Journal/article/download/328/130.

import cv2
import numpy as np
from os import listdir

##################################################################################
# mssim from cv2 (https://docs.opencv.org/4.x/d5/dc4/tutorial_video_input_psnr_ssim.html)
##################################################################################
def MSSISM(i1, i2, win=11, ret_map=False):
    C1 = 6.5025
    C2 = 58.5225
    # INITS
    I1 = np.float64(i1) # cannot calculate on one byte large values
    I2 = np.float64(i2)
    I2_2 = I2 * I2 # I2^2
    I1_2 = I1 * I1 # I1^2
    I1_I2 = I1 * I2 # I1 * I2
    # END INITS
    # PRELIMINARY COMPUTING
    mu1 = cv2.GaussianBlur(I1, (win, win), 1.5)
    mu2 = cv2.GaussianBlur(I2, (win, win), 1.5)
    mu1_2 = mu1 * mu1
    mu2_2 = mu2 * mu2
    mu1_mu2 = mu1 * mu2
    sigma1_2 = cv2.GaussianBlur(I1_2, (win, win), 1.5)
    sigma1_2 -= mu1_2
    sigma2_2 = cv2.GaussianBlur(I2_2, (win, win), 1.5)
    sigma2_2 -= mu2_2
    sigma12 = cv2.GaussianBlur(I1_I2, (win, win), 1.5)
    sigma12 -= mu1_mu2
    t1 = 2 * mu1_mu2 + C1
    t2 = 2 * sigma12 + C2
    t3 = t1 * t2                    # t3 = ((2*mu1_mu2 + C1).*(2*sigma12 + C2))
    t1 = mu1_2 + mu2_2 + C1
    t2 = sigma1_2 + sigma2_2 + C2
    t1 = t1 * t2                    # t1 =((mu1_2 + mu2_2 + C1).*(sigma1_2 + sigma2_2 + C2))
    ssim_map = cv2.divide(t3, t1)    # ssim_map =  t3./t1;
    mssim = np.mean(ssim_map)       # mssim = average of ssim map

    if ret_map==True:
        return mssim, ssim_map
    else:
        return mssim

##################################################################################
# absolute mssim
##################################################################################
def absoluteMSSIM(i1, i2, win=11, ret_map=False):
    C2 = 58.5225
    C3 = C2/2
    k = 1 # constant k, control contrast sensitivity

    # INITS
    I1 = np.float64(i1) # cannot calculate on one byte large values
    I2 = np.float64(i2)
    I2_2 = I2 * I2 # I2^2
    I1_2 = I1 * I1 # I1^2
    I1_I2 = I1 * I2 # I1 * I2
    # END INITS
    # PRELIMINARY COMPUTING
    mu1 = cv2.GaussianBlur(I1, (win, win), 1.5) # means
    mu2 = cv2.GaussianBlur(I2, (win, win), 1.5)
    mu1_2 = mu1 * mu1
    mu2_2 = mu2 * mu2
    mu1_mu2 = mu1 * mu2
    sigma1_2 = cv2.GaussianBlur(I1_2, (win, win), 1.5) # variance (sigma^2)
    sigma1_2 -= mu1_2
    sigma2_2 = cv2.GaussianBlur(I2_2, (win, win), 1.5)
    sigma2_2 -= mu2_2
    sigma12 = cv2.GaussianBlur(I1_I2, (win, win), 1.5)
    sigma12 -= mu1_mu2

    sigma1_2 = np.clip(sigma1_2, a_min=0, a_max=65025) # variance should be in range of (0~65025) for 8bit image
    sigma2_2 = np.clip(sigma2_2, a_min=0, a_max=65025)
    sigma1 = np.sqrt(sigma1_2) # standard deviation
    sigma2 = np.sqrt(sigma2_2)

    lm = 1 - (cv2.absdiff(mu1, mu2)/255) # luminance
    cn = np.where(sigma1<sigma2,(sigma1+k)/(sigma2+k),(sigma2+k)/(sigma1+k)) # contrast
    st = (sigma12+C3)/((sigma1*sigma2)+C3) # structure

    ssim_map = lm*cn*st
    mssim = np.mean(lm*cn*st)

    if ret_map==True:
        return mssim, ssim_map
    else:
        return mssim

##################################################################################
# main
##################################################################################
img1 = cv2.imread(r'images\\caps.bmp')
img2 = cv2.imread(r'images\\img126.bmp')

ssim1, map1 = MSSISM(img1, img2, ret_map=True)
ssim2, map2 = absoluteMSSIM(img1, img2, ret_map=True)

print('MSSIM            :', ssim1) 
print('Absolute MSSIM   :', ssim2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)