#What does this code do?
#---------------------------
#using a text file to create a pdf
#enter our information.


from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(200,10,txt="This is line number 1",ln=1,align="C")
pdf.cell(200,10,txt="This is line number 2",ln=2,align="L")
pdf.cell(200,10,txt="This is line number 3",ln=3,align="R")

file=open("newfile.txt","r")
for line in file:
    if line.startswith("NAME"):
        name=input("Please enter your name")
        pdf.cell(200,10,txt=name,ln=1,align="C")
    if line.startswith("COURSE"):
        course=input("Please enter your COURSE")
        pdf.cell(200,10,txt=course,ln=1,align="C")
    if line.startswith("ID"):
        id=input("Please enter your ID")
        pdf.cell(200,10,txt=id,ln=1,align="C")


pdf.output("Demo4.pdf")