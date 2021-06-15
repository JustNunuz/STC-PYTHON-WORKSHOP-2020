  # :snake: STC-PYTHON-WORKSHOP-2020
  Welcome to this beginner friendly walkthrough Python. The purpose of this lesson is to introduce you to Python and give you an overview on what Python can do.
  Check out the Sunway Tech Club's page right :point_right:[here](https://github.com/sunwaytechclub):point_left:.
## Topics Covered
* Setting up your Python and Visual Studio Code
* Input
* Output
* IF statements
* Loops
* Importing Libraries
* File
* *Making something cool*
 ## :world_map: GETTING STARTED
  * Installing Python:
    * :point_right: https://www.python.org/downloads/  
    * Download Python 3 for your operating system.
    * :point_right: https://www.youtube.com/watch?v=UvcQlPZ8ecA
  * Downloading VS code: 
    * :point_right: https://code.visualstudio.com/Download 
    * Download the one for your operating system.
    * :point_right: https://www.youtube.com/watch?v=MlIzFUI1QGA
    
    
    # We will be making a REPORT GENEATOR USING PYTHON
    ## :bulb: Idea
    * Creating a program in python that can read from a file and store the information as a PDF.
    * It should be able to make a sample coverpage for assignments.
    
    ## STEP 1 : GO TO YOUR TERMINAL IN VISUAL STUDIO CODE
    Type the code below. :point_down:
    
    ``` pip install pyPdf```
    
    * :point_right: Official website :https://pypi.org/project/pyPdf/
    * Visit the website to know more about what Pypdf can do!
  ## STEP 2: MAKE YOUR FIRST PDF!
  ```
from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(200,10,txt="This is line number 1",ln=1,align="C")
pdf.cell(200,10,txt="This is line number 2",ln=2,align="L")
pdf.cell(200,10,txt="This is line number 3",ln=3,align="R")
#Alignment is totally your choice
```
## Adding an image

```
pdf.output("Demo1.pdf")
#"Demo" is just the name, the name can be anything you desire.
```
  ## READY TO MOVE TO THE NEXT SESSION?
  
  * Session 1 (Beginner): https://github.com/JustNunuz/STC-PYTHON-WORKSHOP-2020
  * Session 2 (Intermediate): https://github.com/shongyang/STC-PYTHON-WORKSHOP-2020---INTERMEDIATE
  * Session 3 (Project / Advanced): https://github.com/easonchai/python2020-workshop
  
  ## Additional Learning materials
  * Python:https://www.w3schools.com/python/default.asp
  * Reading a file line by line : https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
  * How to work with Pypdf: https://realpython.com/pdf-python/
  * Work with pdf and word documents: https://automatetheboringstuff.com/2e/chapter15/
  
  Takayoshi Y once said

> “I learned the fundamentals for programming, 
> which is just what I needed as a first step for my career change!”
  
