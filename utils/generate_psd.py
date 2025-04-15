from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_invoice_pdf(data, invoice_id):
    os.makedirs('invoices', exist_ok=True)
    path = f"invoices/invoice_{invoice_id}.pdf"

    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"INVOICE ID: {invoice_id}")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 30

    c.drawString(50, y, f"Customer: {data['name'][0]}")
    y -= 20
    c.drawString(50, y, f"Phone: {data['phone'][0]}")
    y -= 20
    c.drawString(50, y, f"Email: {data['email'][0]}")
    y -= 20
    c.drawString(50, y, f"Address: {data['address'][0]}")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Items:")
    y -= 20
    c.setFont("Helvetica", 11)

    subtotal = 0
    for i in range(len(data['product'])):
        try:
            if not data['product'][i]: continue
            qty = int(data['qty'][i])
            price = float(data['price'][i])
            total = qty * price
            c.drawString(60, y, f"{data['product'][i]} - {qty} x ₹{price} = ₹{total:.2f}")
            y -= 20
            subtotal += total
        except: continue

    c.drawString(50, y, f"Subtotal: ₹{subtotal:.2f}")
    y -= 20
    gst = float(data.get('gst', ['18'])[0] or 18)
    gst_amount = subtotal * gst / 100
    c.drawString(50, y, f"GST ({gst}%): ₹{gst_amount:.2f}")
    y -= 20

    discount = float(data.get('discount', ['0'])[0] or 0)
    discount_amount = (subtotal + gst_amount) * discount / 100
    c.drawString(50, y, f"Discount ({discount}%): ₹{discount_amount:.2f}")
    y -= 20

    grand_total = subtotal + gst_amount - discount_amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total Payable: ₹{grand_total:.2f}")
    y -= 40

    c.setFont("Helvetica-Oblique", 11)
    c.drawString(50, y, "Thank you for your business!")
    c.save()
    return path