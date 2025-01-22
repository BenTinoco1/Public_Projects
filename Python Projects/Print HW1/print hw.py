from fpdf import FPDF

# Create PDF class with formatting
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Homework Study Guide", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 8, body)
        self.ln(5)

# Create PDF object
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Homework content
content = [
    ("Problem 1: Alien Attack Plans",
     "We are given n cities with specific attack methods.\n"
     "Cities A and B must be attacked with all four methods (1 way each).\n"
     "City C must be attacked with exactly 2 out of 4 methods (6 ways).\n"
     "Remaining cities have 16 options each.\n"
     "Final answer: 6 * 16^(n-3)."),

    ("Problem 2: Parity Proofs",
     "(a) If m and n are odd, their multiplication results in odd values, and subtraction results in even.\n"
     "(b) If m is even and n is odd, subtraction results in odd.\n"
     "(c) Expanding squares shows the expression results in even values."),

    ("Problem 3: Go Board Squares",
     "Counting squares using the number of spaces between 19 lines.\n"
     "1x1 squares: 18*18 = 324.\n"
     "Largest square: 18*18 = 324 cm^2.\n"
     "Set of all square sizes: {1^2, 2^2, ..., 18^2}.\n"
     "9x9 squares: (18-9+1)^2 = 100."),

    ("Problem 4: Divisibility by 8",
     "If x is odd, expressing x = 2k+1 and expanding x^2 - 1 leads to 8m, proving divisibility."),

    ("Problem 5: Recursive Sets",
     "(a) Counting elements in nested sets, leading to final count of 3.\n"
     "(b) Cartesian product recursion, final count is 4.")
]

# Add content to the PDF
for title, body in content:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Save the PDF
pdf_filename = "Homework_Study_Guide.pdf"
pdf.output(pdf_filename)

print(f"PDF successfully created: {pdf_filename}")

