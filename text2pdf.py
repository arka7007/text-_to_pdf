from fpdf import FPDF
import utils as utl

def text_to_pdf(text, font, size, out_file):
	""" Converting text to pdf

		Parameters
		____________
			* param1: text
				* type: string
			* param2: font
				* type: string
			* param3: size
				* type: int
			* param4: out_file
				* type: string

		Returns
		__________
			* return1: check
				* type: bool
	"""  


	pdf = utl.create_instance()
	pdf = utl.add_new_page(pdf)
	pdf = utl.set_font_size(pdf, font, size)
	pdf = utl.page_config(text,pdf)
	check = utl.save_pdf(out_file, pdf)
	return check


# if __name__ == '__main__':
# 	text = "Hope it works"
# 	font = "Arial"
# 	size = 12
# 	out = "1.pdf"
# 	text_to_pdf(text, font, size,out)







