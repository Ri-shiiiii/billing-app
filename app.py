from flask import Flask, render_template, request, send_file
from utils.generate_psd import generate_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_bill():
    customer_name = request.form['customer_name']
    customer_address = request.form['customer_address']
    product_list = request.form['product_list']
    total_amount = request.form['total_amount']
    
    # Generate PDF
    pdf_file = generate_pdf(customer_name, customer_address, product_list, total_amount)
    
    return send_file(pdf_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
