Attempting to process and extract information from PDF documents.

What all has been tried so far:
1. PyPDF4 - Can extract the text but looses the order of data within a table
2. tabula - Not able to identify the tables within PDF as tables because of lack of metadata.
3. pdf2image - Converts PDF text file to image. Needs image processing as further step - This approach needs to be further explored
4. camelot - Able to extract tables. Need to handle multiline splits.

Also, none of the methods extract text formatting related information.