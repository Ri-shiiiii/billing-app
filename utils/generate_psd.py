from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf(customer_name, customer_address, product_list, total_amount):
    file_path = f"generated_bills/{customer_name}_bill.pdf"
    
    # Ensure the directory exists
    if not os.path.exists("generated_bills"):
        os.makedirs("generated_bills")
    
    # Create PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    
    c.setFont("Helvetica", 12)
    
    # Adding customer information
    c.drawString(100, 750, f"Customer Name: {customer_name}")
    c.drawString(100, 735, f"Address: {customer_address}")
    
    # Adding products
    c.drawString(100, 700, "Products:")
    y = 680
    for product in product_list.split(','):
        c.drawString(100, y, f"- {product.strip()}")
        y -= 20
    
    # Adding total amount
    c.drawString(100, y - 20, f"Total Amount: {total_amount}")
    
    # Save the PDF
    c.save()
    
    return file_path
