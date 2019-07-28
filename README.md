# Plant-Leaf-Disease-DetectionPLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 1
ACKNOWLEDGEMENT
We would like to extend our heartiest thanks with a deep sense of gratitude and respect to all those who provided us immense help and guidance during our training period.
We would like to express our sincere thanks to our mentor Prof. S. U. Mane who gave us an opportunity to undertake such a great challenge and innovative work. We are grateful to him for his guidance, encouragement, understanding and insightful support in the development process.
Last but not the least we would like to mention here that we are thankful to each and everybody who has been associated with our project at any stage but whose name does not find a place in this acknowledgement.
Name PRN No.
Ruturaj More - 1603003
Vaibhav Kumbhar - 1603012
Mrinmayee Arde - 1603015
Anagha Pakhare - 1603026
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 2
ABSTRACT
Project aims at training best working model for plant disease detection and diagnosis using healthy and diseased leaves of three different plants in ten distinct classes. We discuss the progress made leading to current development scene and possible future enhancements. This project deals with efficient and new technique for real time plant-leaf disease detection in field of agriculture. Main objective behind this project is to understand the deep learning architecture, neural networks and application of same in leaf disease detection system. It includes preparation of dataset consisting of healthy and diseased leaves and pre-processing of same for training and testing of model.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 3
INDEX
Sr. No.
Content
Page No.
1.
Introduction
4
2.
Problem Statement
5
3.
Domain Area
6
4.
Hardware and Software Requirements
6
5.
Project Implementation Details and flow diagram
7
6.
Results, Screenshots & Discussion
9
7.
Conclusion & Future Scope
12
8.
Learning and Reflections from the project
13
9.
References
14
10.
Activity Chart
15
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 4
INTRODUCTION
Plant disease has become a major threat to global food security. Plant diseases contribute 10–16% losses in the global harvest of crops each year costing an estimated US$220 billion. According to a report of the Food and Agriculture Organization (FAO) , our world population is anticipated to hit 9.1 billion in 2050. Therefore, agricultural production needs to be increased up to 70% to fulfill the food requirements of a steadily growing population. On the other hand, abundant use of chemicals such as bactericides, fungicides, and nematicides to control plant diseases has been causing adverse effects in the agro-ecosystem. Currently, there is a need for effective early disease detection techniques to control plant diseases for food security and sustainability of agro-ecosystem. Plant disease affects the quality of fruits, vegetables, grains, legumes and causes heavy losses in production. Lethal plant diseases result in high mortality in plants. Typically, plant disease damages the photosynthetic apparatus and affects the growth of plant. Most plant diseases (around 85%) are caused by fungal or fungal-like organisms. Other serious diseases of plants are caused by bacteria, viruses, and viroids, and few diseases are caused by certain nematodes . Hence, timely treatment of such diseased plants is required. Present method for plant disease detection is manual that involve naked eye observation by experts. This method requires large team of experts and continuous plant monitoring. For large agricultural fields, this method will be time consuming. To overcome this issues, an automatic plant disease detection system will be beneficial. This issue was the main inspiration behind this project.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 5
PROBLEM STATEMENT
In India, agriculture is the main source of income. Indian economy greatly depends on agricultural productivity. Disease detection of plants and crops and timely treatment of same plays efficient and significant role in agricultural production. In India, existing method for plant disease detection is manual one i.e., with naked eyes through experts. This project deals with newly developed technique for this purpose which makes use of deep learning algorithms and neural networks.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 6
DOMAIN AREA OF PROJECT
Convolutional neural networks have wide application in image classification and detection. For many years neural networks are in the centre of attention when we talk about image processing, video and natural language processing etc. In our project, plant disease detection and deep learning approach are combined.
Clustering is a task of dividing number of data points in different groups on basis of similarities. In short, clustering aims to segregation of groups with same traits.
In our project we are using clustering to detect the infected area of diseased leaf and percentage calculation of same. Convolutional neural network is used for training our model to identify the particular disease of leaf.
Image segmentation is used to extract the diseased patch of leaf and passed through convolutional layers.
HARDWARE AND SOFTWARE REQUIREMENTS
No Hardware And Software Characteristics
1 Memory 8GB DDR4
2 Processor (CPU) Intel Core i7, 7th Gen.
3 Graphics (GPU) NVIDIA GeForce GTX 1050Ti
4 Operating System Windows 10N Pro
5 Anaconda Version 3.6
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 7
IMPLEMENTATION DETAILS AND FLOW DIAGRAM
Proposed Work: We have around 1000 images in each class but we picked just 600 images from each class. Next we converted each image from BGR to RGB. Then we converted each image to an array and also we resized every image to 256 by 256 shape as shown below.
Using Scikit-learn’s Label Binarizer , we converted each image label to binary levels. Then we saved the label binarizer instance using pickle.
We further pre-process the input data by scaling the data points from [0, 255] (the minimum and maximum RGB values of the image) to the range [0, 1]. We then performed a
Fig, Dataset Loading Fig, Class Labeling
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 8
training/testing split on the data using 80% of the images for training and 20% for testing. We created an image generator object which performs random rotations, shifts, flips, crops, and sheers on our image dataset. This allows us to use a smaller dataset and still achieve high results. Next we created our model. In the model we are defaulting to “channel_last” architecture but also creating a switch for backend that support “channel first” on the fourth line. Then we created the first CONV => RELU => POOL. Our CONV layer has 32 filters with a 3 x 3 kernel and RELU activation (Rectified Linear Unit). We apply batch normalization, max pooling, and 25% (0.25) dropout. Next we created two sets of (CONV => RELU) * 2 => POOL blocks. Then only one set of FC (Fully Connected Layer)=> RELU layers.
CNN architecture:
We used the Keras Adam Optimizer for our model. Training our network is initiated by calling model.fit_generator , supplying our data augmentation object, training/testing data, and the number of epochs we wish to train for. We used an epochs value of 25 for this project. Fig, Splitting dataset into Test and Train Fig, CNN Architecture
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 9
RESULT
Front-end:
We have designed graphical user interface at front end that include ‘Load Image’, ‘Proceed’, ‘Predict’, ’Pre-processing’ tabs.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 10
Accuracy and Loss Graph:
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 11
Detected Disease:
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 12
CONCLUSION
We prepared an efficient working model for leaf disease detection which detects and identifies disease of leaf. Still more future work is remaining such as adding RNN model to use description provided by user along with image of leaf. This model can be used to solve the farmer problems by providing them better and fast solution. Still we require bigger dataset to gain high accuracy.
FUTURE SCOPE
 Collecting more dataset.
 We need to add the RNN model to process the description provided by the farmer and provide optimal solution for particular disease to farmer.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 13
LEARNING AND REFLECTIONS FROM PROJECT
This project helps us in the deeper understanding of how the CNN and RNN work. We came to know how to build a layer and assigning different parameters to them.
We learned to pre-process the data and fed it into the model which changes upon the type of model we are working. Our team had the wide exposure to different kinds of libraries and their implementation.
The RNN part is new to us and we came to know how to pre-process the text and how the machine understands the word and its correlation with other word. The interest of learning is stirred up by our mentor by teaching us about some important concepts of python and image processing.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 14
REFERENCES
[1] Mohanty, S.P., Hughes, D.P. and Salathé, M., 2016. Using deep learning for image-based plant disease detection. Frontiers in plant science, 7, p.14
[2] Al-Bashish, D., M. Braik and S. Bani-Ahmad, 2011.Detection and classification of leaf diseases using K means-based segmentation and neural-networks-based classification. Inform. Technol. J.
[3] Camargo, A. and Smith, J. S., (2009). An image processing based algorithm to automatically identify plant disease visual symptoms, Biosystems Engineering, Volume 102, Issue 1, and January 2009.
[4] Fast and Accurate Detection and Classification of Plant Diseases. H. Al-Hiary, S. Bani-Ahmad, M. Reyalat, M. Braik and Z. ALRahamneh, March 2011.
PLANT LEAF DISEASE DETECTION USING DEEP LEARNING
RIT RAJARAMNAGAR Dept. of CSE Page 15
ACTIVITY CHART
TIME
ACTIVITIES PERFORMED
1ST week
12 Jan to 27 Jan
Project selection
2ND week
1 Feb to 16 Feb
Study of related articles
3rd week
27 Feb to 5 March
Preparation of custom dataset of healthy and diseased plant leaves
4TH week
23 March to 28 March
Training, testing of model and report writing Guide Mini-Project In-charge Head Of Department (C.S.E), (Prof. S. U. Mane) (Prof. D. P. Kshirsagar) (Dr. N. V. Dharwadkar)
