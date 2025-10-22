import connexion

from openapi_server import encoder

connexion_app = connexion.App(__name__, specification_dir='./openapi/')
connexion_app.app.json_encoder = encoder.JSONEncoder
connexion_app.add_api(
    'openapi.yaml',
    arguments={'title': 'CV Download Service'},
    options={'swagger_ui': False, 'redoc': False, 'strict_validation': True},
    pythonic_params=True
)

app = connexion_app.app

