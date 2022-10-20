"""Runs the web server.
"""

from website import create_app

app = create_app()

# NB: This ensures that only if we run the file (not import) will the following code run.
if __name__ == '__main__':
    # NB: Switch to False when in production.
    app.run(debug=True)
