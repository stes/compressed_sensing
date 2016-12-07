# A Deep Learning Approach to Compressive Sensing

Code, Latex Source and Presentation for seminar project at RWTH Aachen University, summer term 2016.

Based on the paper ["A Deep Learning Approach to Structured Signal Recovery"](https://arxiv.org/abs/1508.04065) by Ali Mousavi, Ankit B. Patel and Richard G. Baraniuk.

Abstract
========

Compressed sensing has proven to be an important technique in signal acquisition, especially in contexts in which sensor quality or the maximum possible duration of the measurement is limited. 
In this report, deep learning techniques are used to improve compressive sensing in the context of image acquisition.
In a previous approach, \cite{Mousavi2015} deployed stacked denoising autoencoders capable of reconstructing images considerably faster than conventional iterative methods.
Apart from reviewing this approach, a possible extension using convolutional autoencoders inspired by the popular VGGnet architecture is discussed.
Instead of learning models from scratch, a simple yet effective way for adapting available filters used in ImageNet classification is presented.
By reformulation of the autoencoder structure in terms of a fully convolutional network, the approach by \cite{Mousavi2015} can be adapted to arbritrarly large images for efficient learning of the measurement matrix and sparsity basis.
Suggestions on the real implementation of such as system conclude the report.

Used Architecture
=================

The input image is first transformed into an overcomplete and likely sparse representation by application of two convolutional blocks as in the original VGG architecture.
These blocks were initialized using the VGG weights pre-trained on the ImageNet dataset.
The resulting filter map undergoes spatial pooling, reducing the filter map size by a factor of 4.
Afterwards, another convolution compresses the feature representation and outputs filter maps spatially reduced by a factor of 4, while the number of feature maps is 3.
Overall, after this bottleneck operation, the measurement vector with $\frac{M}{N} = 0.25$ is obtained.
In the backward pass, deconvolution with tied weights and unpooling using the stored pooling indices upsamples the measurement vector and is used for reconstruction of the image.
Note that normalization layers (Batch Normalization between convolutions and ReLUs) were omitted in the figure.

![Used Architecture](https://github.com/stes/compressed_sensing/blob/master/report/fig/vgg-architecture.png)

Results after Training
======================

Image Reconstruction with pre-trained AE
**(a)** depicts original images fed into the network.
Those are compressed by a factor of M/N = 0.25 using a learnable, nonlinear measurement function.
The reconstructions are shown in **(b)**.
**(c)** depicts the residuum, averaged over all color channels.
Average PSNR over all images and color channels was 25.3 dB.

![Residuals after Training](https://github.com/stes/compressed_sensing/blob/master/report/fig/vgg-ae-rgb-2.png)
