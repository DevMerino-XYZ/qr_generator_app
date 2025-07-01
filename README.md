# QR Code Generator 📱

A simple and elegant web application for generating QR codes from URLs, built with Flask and Python.

## 🌟 Features

- ✨ **Modern and responsive interface**: Attractive design that works on desktop and mobile
- 🔗 **QR generation from URLs**: Convert any URL into a QR code
- 📁 **Multiple formats**: Supports PNG and JPG
- 💾 **Direct download**: Download generated QR codes
- 🖼️ **Integrated gallery**: View all your generated QR codes
- 🚀 **Easy to use**: Intuitive and user-friendly interface

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **qrcode** - QR code generation
- **Pillow (PIL)** - Image processing
- **HTML5/CSS3** - Modern frontend

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation and Setup

### 1. Clone or download the project
```bash
# If you have git installed
git clone <REPOSITORY_URL>
cd qr_generator_app

# Or simply download and extract the ZIP file
```

### 2. Create and activate virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🎮 Application Usage

### Run the application
```bash
python app.py
```

The application will be available at: `http://127.0.0.1:5000`

### Main features:

1. **Main Page**:
   - Enter any valid URL
   - Select image format (PNG or JPG)
   - Click "Generate QR Code"

2. **Results Page**:
   - View the generated QR code
   - Download the image
   - Access the gallery
   - Generate another QR code

3. **Gallery**:
   - View all generated QR codes
   - Download any previous QR code
   - Easy navigation between pages

## 📁 Project Structure

```
qr_generator_app/
├── app.py                 # Main Flask application
├── run.py                 # Startup script
├── requirements.txt       # Project dependencies
├── README.md             # This file
├── start_qr_generator.bat # Windows batch startup file
├── templates/            # HTML templates
│   ├── index.html        # Main page
│   ├── result.html       # Results page
│   └── gallery.html      # QR code gallery
├── static/               # Static files
│   └── qr_codes/         # Generated QR codes
└── venv/                 # Virtual environment (generated)
```

## 🎨 Screenshots

The application features a modern design with:
- Attractive gradients
- Emoji icons for better UX
- Responsive design
- Smooth animations
- Intuitive interface

## 🔧 Advanced Configuration

### Customize settings in `app.py`:

```python
# Change port and host
app.run(debug=True, host='0.0.0.0', port=8000)

# Change QR codes directory
QR_CODES_DIR = os.path.join('my_folder', 'qr_codes')

# Modify QR configuration
qr = qrcode.QRCode(
    version=1,                    # QR size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,                  # Size of each box
    border=4,                     # Border size
)
```

## 📖 API Endpoints

- `GET /` - Main page
- `POST /generate` - Generate QR code
- `GET /download/<filename>` - Download QR code
- `GET /gallery` - View QR code gallery

## 🐛 Troubleshooting

### Error: "No module named 'flask'"
```bash
# Make sure the virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### Error: "Address already in use"
```bash
# Port 5000 is busy, change the port in app.py:
app.run(debug=True, host='127.0.0.1', port=5001)
```

### QR codes are not generated
- Verify that the URL is valid (must include http:// or https://)
- Make sure the `static/qr_codes/` folder has write permissions

## 🚀 Production Deployment

To deploy in production:

1. **Disable debug mode**:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

2. **Use a WSGI server** like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app -b 0.0.0.0:5000
```

3. **Configure a reverse proxy** with Nginx (optional)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is under the MIT License. See the `LICENSE` file for more details.

## 👨‍💻 Author

Created with ❤️ by Carlos Merino

## 🆘 Support

If you have problems or questions:
1. Check the troubleshooting section
2. Create an issue in the repository
3. Contact the developer

---

Enjoy generating QR codes! 🎉
