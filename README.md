# ZenDrive
![Logo](https://github.com/user-attachments/assets/e48a9f90-74a2-4c9b-951b-6620248afe99)
Distracted Driver Detection for Safety

This project analyzes the State Farm Distracted Driver Detection dataset from Kaggle to understand driver behaviors and potential distractions. The focus is on data exploration, visualization, and bounding box annotation to highlight distraction-related elements in images.
________________________________________

Dataset Overview

The dataset is sourced from Kaggle:

Kaggle Competition: State Farm Distracted Driver Detection

The dataset consists of images categorized into 10 classes, each representing a different driver action:

●	c0: Normal driving

●	c1: Texting - right hand

●	c2: Talking on the phone - right hand

●	c3: Texting - left hand

●	c4: Talking on the phone - left hand

●	c5: Operating the radio

●	c6: Drinking

●	c7: Reaching behind

●	c8: Hair and makeup

●	c9: Talking to passenger

________________________________________
Data Exploration

Understanding the Data

●	Verified the structure of the dataset files.

●	Checked the number of unique drivers and their respective image counts.

Visualizing Image Distributions

●	Created a histogram to show the number of images per driver.

●	Created another histogram to show the number of images per class.

Image Dimension Analysis

●	Verified whether all images have the same dimensions.

●	Counted the number of unique image resolutions.

________________________________________

Bounding Box Annotation

Since the dataset does not provide bounding boxes, manual annotations are being created using FiftyOne to mark distraction-related elements in images.

Annotations Include:

●	Identifying the driver in the image.

●	Highlighting objects contributing to distractions, such as mobile phones or drinks.

●	Marking key actions like texting, reaching, or talking.

________________________________________

Tools Used

●	Kaggle Notebooks – For dataset exploration and visualization

●	FiftyOne – For bounding box annotation

●	Matplotlib & Seaborn – For data visualization

________________________________________
Next Steps
●	Complete bounding box annotations for all distraction classes.
●	Analyze object positioning in images to understand distraction trends.
●	Identify patterns that could improve dataset insights.

