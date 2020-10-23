#What does this code do????
#---------------------------
#this code creates a pdf with 3 lines
# each line has a different alignment 
#This code also prints the information from a text file.


from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(200,10,txt="This is line number 1",ln=1,align="C")
pdf.cell(200,10,txt="This is line number 2",ln=2,align="L")
pdf.cell(200,10,txt="This is line number 3",ln=3,align="R")

file=open("newfile.txt","r")
for line in file:
        pdf.cell(200,10,txt=line,ln=1,align="C")
#the code will print the information from a file
pdf.output("Demo1.pdf")
#Demo.pdf will be your file name