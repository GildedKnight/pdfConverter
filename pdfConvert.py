# coding: utf-8

import csv
import ast
import glob
from fpdf import FPDF

#Open CSV file to read CSV, note: reading and write file should be under "with"
with open("/home/musadiq/Downloads/resume_e.csv","r+") as csvFile:
    #Read CSV
    readCsv = csv.reader(csvFile)
    for row in readCsv:     
        #Get Values and manupilate in the file.write
        ID = row[0]
        Category = row[1]
        Resume = row[2]
#         print(Resume.encode('utf-8'))
        
        
        #Write CSV you need format it to string if the value is an int
        with open('/home/musadiq/Desktop/resume_text/'+str(Category)+str(ID)+".txt","w") as f:
            f.write(Resume)
#         f.close()


#List of all files created from each row of csv
file_list = glob.glob('/home/musadiq/Desktop/resume_text/*.txt')

for file in file_list:
    try:
        with open(file, "r+") as f:
            text = [ast.literal_eval(line.decode('utf-8')) for line in f]
            for l in text:
                f.write(ast.literal_eval(l.decode('utf-8')))
            f.close()
    except Exception as e:
        with open('log.txt','w+') as f:
            f.writelines(file)



#Converting to pdf format
file_name = glob.glob('/home/musadiq/Desktop/resume_text/*.txt')

class PDF(FPDF):
    def pdf_print(self,name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('ascii')
        PDF.add_page(self)
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5)


        with open("/home/musadiq/Downloads/resume_e.csv","r+") as csvFile:
        #Read CSV
            readCsv = csv.reader(csvFile)
            for row in readCsv:     
                #Get Values and manupilate in the file.write
                ID = row[0]
                Category = row[1]

                self.output('/home/musadiq/Desktop/resume_pdf/'+str(Category)+str(ID)+'.pdf', 'F')
pdf=PDF()
for name in file_name:     
    pdf.pdf_print(name)