#!/usr/bin/env python3

from openapi_server.app import connexion_app

# For local debugging only, Dockerfile uses app.py
if __name__ == "__main__":
    connexion_app.run(port=8080, host="0.0.0.0", debug=False)

