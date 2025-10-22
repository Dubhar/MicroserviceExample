import os
from flask import abort
import requests
from jose import jwt, JWTError

# Read Keycloak config from environment variables, with defaults
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "https://keycloak.example.com/realms/myrealm")
AUDIENCE = os.getenv("KEYCLOAK_CLIENT_ID", "my-client-id")
JWKS_URL = f"{KEYCLOAK_URL}/protocol/openid-connect/certs"

# Fetch JWKS once at startup
jwks = requests.get(JWKS_URL).json()

def get_public_key(token_kid):
    for key in jwks["keys"]:
        if key["kid"] == token_kid:
            return key
    raise Exception("Public key not found")

def verify_token(token: str):
    unverified_header = jwt.get_unverified_header(token)
    key = get_public_key(unverified_header["kid"])
    payload = jwt.decode(token, key, algorithms=["RS256"], audience=AUDIENCE)
    return payload

def token_auth(token, required_scopes=None):
    if not token:
        abort(401, "Missing token")
    try:
        payload = verify_token(token)
        return payload
    except JWTError as e:
        abort(401, str(e))

