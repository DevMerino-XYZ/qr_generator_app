"""
QR Code Generator Web Application

A Flask-based web application for generating QR codes from URLs.
Features include multiple image formats (PNG/JPG), download functionality,
and a gallery to view previously generated QR codes.

Author: Carlos Merino
License: MIT
Version: 1.0.0
"""

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import qrcode
from qrcode.image.styledpil import StyledPilImage
import os
import datetime
import uuid
from PIL import Image

app = Flask(__name__)
app.secret_key = 'qr_generator_secret_key_2024'

# Configuration
QR_CODES_DIR = os.path.join('static', 'qr_codes')

# Ensure the directory exists
os.makedirs(QR_CODES_DIR, exist_ok=True)

@app.route('/')
def index():
    """
    Render the main page with the QR code generation form.
    
    Returns:
        str: Rendered HTML template for the main page
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    """
    Generate a QR code from a URL submitted via POST request.
    
    Accepts form data containing:
    - url: The URL to encode in the QR code
    - format: Image format (PNG or JPG, defaults to PNG)
    
    Returns:
        flask.Response: Either redirects to index on error or renders result page on success
        
    Raises:
        Exception: Any error during QR code generation will be caught and displayed to user
    """
    url = request.form.get('url')
    image_format = request.form.get('format', 'PNG').upper()
    
    if not url:
        flash('Please enter a valid URL.', 'error')
        return redirect(url_for('index'))
    
    try:
        # Generate unique filename for the QR code
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"qr_{timestamp}_{unique_id}.{image_format.lower()}"
        filepath = os.path.join(QR_CODES_DIR, filename)
        
        # Create QR code object with configuration
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create and save the image based on format
        if image_format == 'PNG':
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filepath, 'PNG')
        elif image_format == 'JPG' or image_format == 'JPEG':
            img = qr.make_image(fill_color="black", back_color="white")
            # Convert to RGB for JPG (JPG files don't support transparency)
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if len(img.split()) == 4 else None)
            rgb_img.save(filepath, 'JPEG')
        
        flash(f'QR Code generated successfully! Format: {image_format}', 'success')
        return render_template('result.html', 
                             url=url, 
                             filename=filename, 
                             qr_path=f'static/qr_codes/{filename}',
                             format=image_format)
    
    except Exception as e:
        flash(f'Error generating QR code: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_qr(filename):
    """
    Download a previously generated QR code file.
    
    Args:
        filename (str): Name of the QR code file to download
        
    Returns:
        flask.Response: File download response or redirect to index on error
        
    Raises:
        Exception: Any error during file download will be caught and displayed to user
    """
    try:
        filepath = os.path.join(QR_CODES_DIR, filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            flash('File does not exist.', 'error')
            return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error downloading file: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/gallery')
def gallery():
    """
    Display a gallery of all generated QR codes.
    
    Shows the 20 most recently generated QR codes in reverse chronological order.
    
    Returns:
        str: Rendered HTML template for the gallery page
        
    Raises:
        Exception: Any error loading gallery will be caught and user redirected to index
    """
    try:
        qr_files = []
        if os.path.exists(QR_CODES_DIR):
            files = [f for f in os.listdir(QR_CODES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            files.sort(reverse=True)  # Most recent first
            qr_files = files[:20]  # Show only the last 20
        
        return render_template('gallery.html', qr_files=qr_files)
    except Exception as e:
        flash(f'Error loading gallery: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) 