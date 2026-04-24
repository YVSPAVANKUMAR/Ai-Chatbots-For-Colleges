# College ChatBot Portal

This project is a Flask-based college chatbot portal with a landing page, dashboard, about page, contact page, and campus-specific chatbot views powered by Botpress shareable links.

## Features

- Responsive multi-page Flask app
- Dashboard with college chatbot cards
- Dedicated chatbot pages for each campus bot
- About, contact, and demo login pages
- Render-friendly setup with no local MongoDB dependency

## Project Structure

- `app.py` - main Flask application and chatbot data source
- `templates/` - Jinja templates for all pages
- `static/images/` - image assets used across the site
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python runtime version for deployment

## Local Setup

1. Clone the repository.
2. Open the project folder:

```bash
cd "Chat Bot Final"
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

5. Open:

```text
http://127.0.0.1:5000/
```

## Available Routes

- `/` - homepage
- `/dashboard` - chatbot dashboard
- `/chatbot/<bot-slug>` - individual chatbot page
- `/about` - about page
- `/contact` - contact page
- `/login` - placeholder login page

## Deployment on Render

This project is ready to run on Render without a local MongoDB server.

Recommended settings:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Python version: from `runtime.txt`

Recommended environment variable:

- `SECRET_KEY` - set this in Render for production

## Dashboard Fix Note

The dashboard error on Render happened because the older version of the app tried to connect to:

```text
mongodb://localhost:27017/
```

That works only on a machine with a local MongoDB instance. The current version stores chatbot definitions directly in `app.py`, so `/dashboard` and chatbot pages work in hosted environments too.

## Customizing Bots

The chatbot cards and chatbot pages are driven by the `BOTS` list in [app.py](app.py).

Each bot entry includes:

- `slug`
- `campus_label`
- `name`
- `description`
- `image`
- `shareable_url`
- `status_text`

To add or update a bot, edit that list and redeploy.

## License

This project is licensed under the MIT License.
