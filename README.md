# Virtual Camera
## A python application that uses OpenCV lib and IP Webcam app to convert your phone into a portable Webcam

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/eersnington/virtualCamera)


## What does it do?

For online classes, I found it difficult to use teams/zoom for online classes on my phone cause I don't have a webcam for my computer, so I found a way to use my phone as a webcam.

## Installation and Setup

Clone the repository
```sh
git clone https://github.com/eersnington/virtualCamera.git

```
Change directory and install OpenCV
```sh
cd virtualCamera
pip3 install opencv-python
```
Now install IP Webcam in your mobile phone.

<img src="https://i.imgur.com/pjPhBSL.jpg" alt="alt text" width="250" height="250">

Open the application and start the server

<img src="https://i.imgur.com/5sIov1Z.png" alt="alt text" width="125" height="250">

Note down the link where your video feed is hosted.

<img src="https://i.imgur.com/ZU1evg6.png" alt="alt text" width="500" height="250">

Now open Cam.py in your IDE or any Editor and replace the link with yours.

<img src="https://i.imgur.com/TnNtoXa.png" alt="alt text">

Save the file and now run the script.
```sh
python3 cam.py
```

Now for your computer to recognise the feed as a virtual camera, you can use an application like OBS and use their virtual camera plugin.

Here is a [link to a video](https://www.youtube.com/watch?v=bfrknjDzukI) that explains how to use OBS for a virtual camera

