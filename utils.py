from fpdf import FPDF


def create_instance():
	"""
		Creating instance of fdpf

		Returns
		____________
			* True:
				* return: pdf
					* type: fpdfObject
			* False:
				* return: False
					* type: bool 
	"""
	try:
		pdf = FPDF()
		return pdf
	except Exception as e:
		return False


def add_new_page(pdf):
	"""
		Initializing new Page in fpdfObject

		Parameters
		______________
			* param1: pdf
				* type: fpdfObject

		Returns
		__________
			* True:
				* return: pdf
					* type: fpdfObject
			* False:
				* return: False
					* type: bool
	"""

	try:
		pdf.add_page()
		return pdf
	except Exception as e:
		return False


def set_font_size(pdf,font, sze): 
	"""
		Setting font size to write the text

		Parameters
		______________
			* param1: pdf
				* type: fpdfObject
			* param2: font
				* type: string
			* param3: sze
				* type: int

		Returns
		__________
			* True:
				* return: pdf
					* type: fpdfObject
			* False:
				* return: False
					* type: bool
	"""
	try:
		pdf.set_font(font, size=sze)
		return pdf
	except Exception as e:
		return False


def page_config(text,pdf):
	"""
		Initializing new Page in fpdfObject

		Parameters
		______________
			* param1: pdf
				* type: fpdfObject

		Returns
		__________
			* True:
				* return: pdf
					* type: fpdfObject
			* False:
				* return: False
					* type: bool
	"""
	try:
		pdf.cell(8, 5, txt=text, ln=20, align="C")
		pdf.write(8, text)
		pdf.ln(20)
		return pdf
	except Exception as e:
		return False


def save_pdf(file_name,pdf):
	""" Save the PDF file
		
		Parameters
		_____________
			* param1: file_name
				* type: string
			* param2: pdf
				* type: fpdfObject

		Returns
		____________
			* True:
				* return: True
					* type: bool
			* False:
				* return: False
					* type: bool
	"""
	try:
		pdf.output(file_name)
		return True
	except Exception as e:
		return False


def get_text_files(dir):
	""" Collecting all text files from input folder

		Parameters
		_____________
			* param1: dir
				* type: string

		Returns
		___________
			* True:
				* return: files
					* type: list
			* False:
				* return: False
					* type: bool 
	"""
	import glob, os
	try:
		files = glob.glob(dir+"/*.*")
		return files
	except Exception as e:
		return False
	
def get_file_name(file):
	""" Extracting file name

		Parameters
		____________
			* param1: file
				* type: list

		Returns
		__________
			* True:
				* return: file
					* type: string
			* False:
				* return: False
					* type: bool
	"""
	file = file.split('/')[-1].split('.')[0]
	return file


def read_text_file(file):
	""" Reading text from text files

		Parameters
		____________
			* param1: file
				* type: list

		Returns
		__________
			* True:
				* return: texts
					* type: dict
			* False:
				* return: False
					* type: bool
	"""
	try:
		data = {}
		data['file_name'] = get_file_name(file)
		print("here")
		with open(file, 'r') as file:
			text = file.read()
		data['text'] = text
		return data
	except Exception as e:
		return False
	
