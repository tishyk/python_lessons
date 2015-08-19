#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import PyPDF2

#--- Extracting Text from PDFs -------------------------------
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.isEncrypted => True|False
# if pdf file with password access use -> pdfReader.decrypt('password')
# pdfReader.numPages  => 19
pageObj = pdfReader.getPage(0) # set page number
Text_from_PDF = pageObj.extractText()

#--- Creating PDFs (Modifying)--------------------------------
""" Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
    Create a new PdfFileWriter object.
    Copy pages from the PdfFileReader objects into the PdfFileWriter object.
    Finally, use the PdfFileWriter object to write the output PDF
"""

#--- Copy pages from one PDF document to another. -------------
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
  pageObj = pdf1Reader.getPage(pageNum)
  pdfWriter.addPage(pageObj) # addPage() method will only add pages to the end(no middle insertion).
  
for pageNum in range(pdf2Reader.numPages):
  pageObj = pdf2Reader.getPage(pageNum)
  pdfWriter.addPage(pageObj)
  
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#--- Rotating Pages -------------------------------------------------
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)

page.rotateClockwise(90) #=>   {'/Contents': [IndirectObject(961, 0), IndirectObject(962, 0),   --snip--   }

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

#--- Overlaying Pages ------------------------------------------------
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
  pageObj = pdfReader.getPage(pageNum)
  pdfWriter.addPage(pageObj)
  
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

#--- Encrypting PDFs --------------------------------------------------
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
  pdfWriter.addPage(pdfReader.getPage(pageNum))
  
pdfWriter.encrypt('swordfish') #<= Add password here

resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf) #HW save into the same filename?
resultPdf.close()

# Home work
# Cut out specific pages from PDFs.
# Create a PDF from only those pages that have some specific text, identified by extractText()
# Reorder pages in a PDF

