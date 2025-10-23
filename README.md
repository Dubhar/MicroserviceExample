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
6) Pack client code as package and provide to actual clients
  - `docker run --rm -v "$PWD/ts-client":/app -w /app node:latest bash -c "npm install && npm run build || true && npm pack"`
  - Distribute `ts-client/dubhar-cv-client-0.1.0.tgz` i.e. via Package Registry

# Steps to setup a Client:

1) Install the provided, version specific package:
  - `npm install ~/Downloads/cv-client-0.1.0.tgz`
2) Use the package to access Microservice:
  ```TypeScript
  import { Configuration, CvApi, HealthApi } from "cv-client";

  const config = new Configuration({ basePath: "http://localhost:8080" });

  const cvApi = new CvApi(config);
  const healthApi = new HealthApi(config);

  await healthApi.getHealth();
  const pdf = await cvApi.getCv({ firstname: "John", lastname: "Doe" });
  ```

