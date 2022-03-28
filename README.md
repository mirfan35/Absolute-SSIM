# Absolute SSIM

SSIM or Structural Similarity is not a metric or distance function, different pixel value is weighted differently and sometimes can lead to undesired results. Two high values are easier to score high similarity even though the difference between the two is clearly visible and when comparing two low values the score is low similarity even when the two images look almost the same. This measurement bias is caused by some components in the SSIM.

Absolute SSIM is just another variance of SSIM by replacing the luminance and contrast component of the original SSIM with relative difference relation. 

# SSIM vs Absolute SSIM

# Luminance Test

Measuring the mean SSIM between the intensity of 0 and 26 only scored 0.009527 similarities even though the two images look almost similar indicating the bias measurement of SSIM. On the other hand, Absolute SSIM scores it as 0.898039 because Absolute SSIM measures relative error between the two intensities. Absolute SSIM is more suitable to be used when comparing darker or low-intensity images. 

![](images/AbsoluteSSIM_vs_SSIM.png)

# Human Perception Test 

The distribution score of SSIM is not linear with the human perception score. SSIM is more generous than the human judgment of similarity. Absolute SSIM is a lot more similar to human subjective score. (Dataset used available at: http://live.ece.utexas.edu/research/quality/).

# Documentation

Download link: http://arqiipubl.com/ojs/index.php/AMS_Journal/article/download/328/130.

# APA (7th Edition) Citation

Jaafar, M., Nawawi, S., & Abdul Rahim, R. (2022). Improving Measurement Bias of SSIM using Absolute Difference Equation. Arqiipubl.com. Retrieved from http://arqiipubl.com/ojs/index.php/AMS_Journal/article/download/328/130.
