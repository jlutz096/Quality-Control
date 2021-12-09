# Quality Control in Manufacturing (QCiM)
Main repository for CS440 project "Image Quality Control in Manufacturing" 

*Program Designed and Built on Linux Ubunutu 21.10*

Developers/Researchers include: Lee Lee, Christian Wills, Justin Lutz, Mark Owoseni.

Former Developer: Ashish Lamichhane 

The main idea behind the conception of this project is to introduce more efficient ways in which Quality Control can be used in a manufacturing setting. The proposed idea is if we can create a system that can allow for faster processing of products in a manufacturing setting, then the more efficient the product can be made and delivered to the customer. 


<h2>Install</h2>

  There are some prerequiste libraries, mostly OpenCV. OpenCv is a library of programming functions mainly aimed at real-time computer vision. This library if installed through a Jupyter Notebook can be installed with pip. 
  
  | pip install opencv-python |
  |--|
  
  Likewise, the user interface is built using tkinter. Tkinter is a standard Python Interface. Similarily, it can be installed through a Jupyter Notebook by using:
  
  |pip install tk|
  |--|
  
  The remaining functionality is provided through standard Python installment. 
  
  NOTE: If you plan to run the program through VSCode or a different IDE, you will have to pip install through the terminal, or by personal preference. 
  
  For demonstration purposes it is easier to use a Jupyter Notebook to run this application in union with the handbook/tutorial provided below.


<h2>Abstract</h2>

  The main idea behind this project is automating the quality control process in a manufacturing environment. The title of the project is Quality Control in Manufacturing (QCiM). The goal QCiM is to accomplish quality control of various products produced in manufacturing. The software runs off a camera feed that objectively 'grades' product as it passed under the video feed. After capture a percentage is returned and the system makes a judgement based upon the result. If passing, the product is allowed to continue down the production line, otherwise it is sent for refurbishment or to be destroyed.
  This product integrates a Computer Vision framework known as OpenCV. This project will be developed in Python, in an Jupyter Notebook environment. More information will be available in following sections.


<h2>Intro</h2>

Quality Control in Manufacturing (QCiM) is an software application that takes in images from a theoretical production line. Once it has an image, it compares it against a template image. A result is returned. Grading critera differs from product to product but the overall goal is Quality Control. Results are of a higher readability when illustrated with Jupyter Notebook. The tutorial section will setforth the steps it takes to create an accurate working application.

Basic Concept

Template image is loaded into the program and subsequent images selected for matching are made. Once the match is made a percentage is displayed, similarily a rectangle is drawn around the highest match. The image is converted into grey scale, for edge detection which makes it easier for matches to be found. 

Implementation

Select template, select image to be matched. Compare image and get result relating to highest percentage of match.
