# College ChatBot Portal

A college chatbot portal built with Flask and Tailwind CSS. The site includes a landing page, an about section, a contact form, and a dashboard for browsing institution-specific chatbot links.

## Features

- Responsive homepage and shared site layout
- Dashboard with dedicated campus chatbot cards
- Individual chatbot pages powered by Botpress shareable links
- About, contact, and placeholder login pages
- AOS animations and Tailwind-based styling

## Project Structure

- `app.py` - Flask application entry point
- `templates/` - Jinja templates for each page
- `static/images/` - image assets used in the site
- `requirements.txt` - Python dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Change into the project folder:
   ```bash
   cd "Chat Bot Final"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Start the Flask server:

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Deployment Notes

- The dashboard no longer depends on a local MongoDB instance, so it can run on Render as-is.
- Set `SECRET_KEY` in your hosting environment for production.
- Use `gunicorn app:app` as the start command on Render if you need to set it manually.

## License

This project is licensed under the MIT License.
