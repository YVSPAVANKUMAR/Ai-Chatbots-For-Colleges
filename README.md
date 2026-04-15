# College ChatBot Portal

A professional college chatbot portal built with Flask, Tailwind CSS, and MongoDB. The site offers a polished landing page, an about section, a contact form, and a dashboard for browsing institution-specific chatbots.

## Features

- Modern homepage with professional layout and polished UX
- Responsive navigation and site-wide layout
- Dashboard with dedicated campus bots
- Individual chatbot pages powered by Botpress shareable links
- About and contact pages with clean visual presentation
- AOS animations and custom Tailwind-based styling

## Project Structure

- `app.py` - Flask application entry point
- `templates/` - Jinja templates for each page
- `static/css/style.css` - custom site styling
- `static/js/script.js` - custom JavaScript for menu and interactions
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

## Configuration

1. Ensure MongoDB is running locally or update the connection string in `app.py`.
2. Add bot documents to the `college_chatbot` database in the `bots` collection.

### Example bot document

```json
{
  "name": "Library Bot",
  "description": "Answers library-related questions",
  "channel": "library-bot"
}
```

## Running the App

Start the Flask server:

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Notes

- The app uses Flask's `static` folder for CSS and JavaScript assets.
- The `dashboard` page dynamically loads bots from MongoDB.
- The `chatbot` route displays a Botpress webchat iframe configured by each bot's `channel`.

## License

This project is licensed under the MIT License.