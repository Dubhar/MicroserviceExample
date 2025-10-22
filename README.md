# Requirements:

Have some containerization installed (Docker, Podman, ...)

# Steps to setup a new Microservice:

1) Define API endpoints using `openapi.yml`
2) Generate server stub from API definition:
  - FastAPI (newer) `docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/openapi.yml -g python-fastapi -o /local/src`
  - OR
  - Flask (mature) `docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/openapi.yml -g python-flask -o /local/src`

