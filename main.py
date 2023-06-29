from app import App
from app.routes import initialise_routes


def main():
    """
    Summary
    -------
    Initialise all routes and serve the app
    """
    initialise_routes()
    App.run(debug=True)


if __name__ == "__main__":
    main()
