# Requirements:

Have some containerization installed (Docker, Podman, ...)

# Steps to setup a new Microservice:

1) Define API endpoints using `openapi.yml`
2) Generate server stub from API definition:
  - FastAPI (newer) `docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/openapi.yml -g python-fastapi -o /local/src`
  - OR
  - Flask (mature) `docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/openapi.yml -g python-flask -o /local/src`
3) Implement the stubbed controller functions in `src/openapi_server/controllers/*.py`
4) Build and run the Microservice as container:
  - `cd src`
  - `docker build -t cv-backend .`
  - `docker run -p 8080:8080 cv-backend`
  - Open [http://localhost:8080/ui/](http://localhost:8080/ui/) in a WebBrowser
  - Test API endpoint, e.g. `curl -o john_doe_cv.pdf "http://localhost:8080/cv?firstName=John&lastName=Doe"`
5) Generate client code:
  - `docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/openapi.yml -g typescript-fetch -o /local/ts-client --additional-properties="supportsES6=true,npmName=@dubhar/cv-client,npmVersion=0.1.0,typescriptThreePlus=true,useSingleRequestParameter=true"`
