from os import environ as env


class Config:
    """
    Summary
    -------
    Static class for configuration

    Attributes
    ----------
    PORT (int) : port to serve the application on
    HOST (str) : host to serve the application on
    """

    PORT = int(env.get("PORT", 5000))
    HOST = str(env.get("HOST", "0.0.0.0"))
