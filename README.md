# Netherland-Traffic-Recognition-System
Final Project of Ironhack Data Analytics Bootcamp


This project contains four traffic sign image folder and python, csv and models include folder:
  Examples: Images for using in the model
  Files: Notebooks, models and python file to open and run traffic classifier
  images_test: Images for testing the neural network model(traffic_classifier.h5)
  signs from the street: Images directly taken from street by me.
  Training: Images within the 149 groups to train the model(my_model.h5)
 
1) Images taken from Natinaal Dataportal Wegveerker and the classifier built for Dutch roads. Here is the API url "https://docs.ndw.nu/api/trafficsigns/nl/index.html"
After getting the 1858922 rows of dataset to pull the images some data cleaning is taken care of in "traffic_signs_api_ and_dataframes.ipynb" file.

2) In the same file after getting the urls of images into a dataframe it's needed to save images. To do that limiting  images out of more than 1,8 million images makes us work easier on building our model. At the end we got 65150 images and 149 classes to build our training data.

3) Then we built another dataframe to use in our validation part in notebook 'traffic_classifier' and saved it into csv file.

4) Now in our second notebook file 'traffic_signs.ipynb' we start building our training model. And we put our training images into array to be able to split them for modeling/

5) After getting train-test split built CNN(Convolutional Neural Network) model and saved it into 'my_model.h5' file.

6)Then to get the accuracy score we imported 'test_df.csv' file which we saved in previous notebook and merging with image list from 'images_test' file. When we get the predictions we get the accuracy score as 0.81.

7) At this point we can give the statements to 149 classes. They're given again from 'NDW' website. That's why the language is Dutch.

8) With the function we can get desired traffic sign image get in the array and have the prediction. To do that it's needed to be put the image path into the functon.

9) On the third notebook file 'classifier.ipynb' everything is more simple. We open the model and feed with the classes list which we did above with dutch statements and put in the function to get the results. It's done for the make it easier in Command Prompt.

10) The fourth notebook 'Classificatie van Verkeersborden.ipynb' is for to get everything into an interface. To do that we are using the 'tkinter' library. With the GUI toolkit in the standard python library now we can run the code by typing 'python Classificatie_van_Verkeersborden.py' in the command line. In this file, we have first loaded the trained model ‘traffic_classifier.h5’ using Keras from tensorflow. And then we build the GUI for uploading the image and a button is used to classify which calls the classify() function. The classify() function is converting the image into the dimension of shape (1, 30, 30, 3). This is because to predict the traffic sign we have to provide the same dimension we have used when building the model. Then we predict the class, the model.predict_classes(image) returns us a number between (0-148) which represents the class it belongs to. We use the dictionary to get the information about the class.


Used links:
https://docs.ndw.nu/api/trafficsigns/nl/index.html
https://www.ndw.nu/
https://towardsdatascience.com/traffic-sign-recognition-with-tensorflow-2-x-7ab4e8611a83
https://medium.com/analytics-vidhya/a-traffic-signs-classifier-the-flask-api-ceb9e34ad415
https://www.kaggle.com/tusharsharma118/belgian-traffic-dataset/notebook
https://data-flair.training/blogs/python-project-traffic-signs-recognition/
https://cloud.google.com/appengine/docs/standard/python/images

