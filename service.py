import text2pdf
import utils as util

input_path = 'input'
output_path = 'output/'
font = "Arial"
size = 10
files = util.get_text_files(input_path)
data = 	[util.read_text_file(t) for t in files]

for each in data:
	text = each['text']
	file_name = each['file_name']
	out_file = output_path+file_name+'.pdf'
	check = text2pdf.text_to_pdf(text, font, size, out_file)
	if check:
		print("---file:  {}.txt------------ converted ".format(file_name)) 