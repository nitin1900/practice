#just copied from github...

from fpdf import FPDF


def main():

    name = get_name()
    merge(name)


def get_name():
    return input("Name: ")


def merge(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=80)
    pdf.set_font("helvetica", "", 54)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "", 28)
    pdf.text(x=50, y=150, txt=f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()