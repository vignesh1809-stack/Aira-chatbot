# Aira Chatbot Web Application

Aira Chatbot is a simple web application for a restaurant, featuring a chatbot powered by Dialogflow, a menu gallery, location info, and contact details.

## Features
- **Home Page**: Banner image and navigation bar.
- **Menu**: Displays menu items with images.
- **Location**: Shows the restaurant address.
- **Contact Us**: Provides phone and email contact.
- **Chatbot**: Integrated Dialogflow chatbot for customer interaction.

## Project Structure
```
frontend/
  main.html        # Main web page
  main.css         # Stylesheet
  banner.jpeg      # Banner image
  menu1.jpg        # Menu item image 1
  menu2.jpg        # Menu item image 2
  menu3.jpg        # Menu item image 3
backend/
  main.py          # Backend server (Python)
  db_helper.py     # Database helper
  generic_helper.py# Generic helper functions
requirements.txt   # Python dependencies
```

## How to Run

### Frontend
1. Open `frontend/main.html` in your browser to view the website.
2. The chatbot is available on the page via Dialogflow integration.

### Backend
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the backend server:
   ```bash
   python backend/main.py
   ```

## Customization
- Update images in the `frontend/` folder as needed.
- Edit `main.html` and `main.css` for UI changes.
- Update backend logic in `backend/` as required.

## Contact
For questions or support, contact: info@vigneshbalusu.com

---
*Developed by Vignesh Balusu*
