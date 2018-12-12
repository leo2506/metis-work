# Can you detect my aircraft?
![](https://github.com/leo2506/metis-work/blob/master/Project%205/Airport_dusk.jpg)

# Overview
According to recent reports, more and more aviation safety accidents and incidents occurred due to overloaded attention of pilots and tower controllers. In 2016 in Shanghai, an aircraft taxied across a runway without noticing another aircraft already speed up to take off on the exact same runway, which would have led to a collision if the pilot on the take-off aircraft had not pulled up responsively. 

This type of incident could have been prevented or alleviated at a very early stage if there were onboard aircraft detecting system in place. It motivates me to use image processing neural network to bridge the gap of technology. Plus, I am highly excited to develop a viable product to ease the workload of pilots and tower controllers, and further enhance aviation safety and improve ground traffic efficiency. Such system can be integrated with Automatic Dependent System - Broadcast (ADS-B) to help pilots recognize aircrafts which may trigger conflict events on the taxiing path. 

# Streamline of Data Analysis
* [Slides](https://github.com/leo2506/metis-work/blob/master/Project%205/slides/Project_5_leo.pdf)
* [Proposal](https://github.com/leo2506/metis-work/blob/master/Project%205/Proposal/Project%20Kojak%20Proposal.pdf)
* [Image_Segmentation.ipynb](https://github.com/leo2506/metis-work/blob/master/Project%205/Image_Segmentation.ipynb) - notebook which collects the images and masks, preprocesses images, constructs a u-net model, evaluates on the testing set and convert segmented masks into bounding boxes. 
* [Video_Detection.ipynb](https://github.com/leo2506/metis-work/blob/master/Project%205/Video_Detection.ipynb) - notebook which decodes video into frames, and draws bounding boxes over predicted aircrafts. 
* [eva_demo.mp4](https://github.com/leo2506/metis-work/blob/master/Project%205/eva_demo.mp4) - a demo of testing model in a video when an aircraft was taxiing.
