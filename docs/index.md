# Welcome to the TKWW Project

In the technical aspect of the project, I opted to develop an API using FastAPI over other considered frameworks such as Flask or BentonML. The decisive factors for choosing FastAPI were its ease of use and the speed at which a proof of concept (PoC) could be realized. The API's architecture is inspired by the Model-View-Controller (MVC) pattern, aiming for modularity and scalability to accommodate future projects or enhancements.

The core idea was to embrace various MLOps practices and concepts. This includes using Poetry for dependency management, implementing logging for effective monitoring post-deployment (with plans to integrate Prometheus or Grafana for enhanced insights), version control via GitHub, leveraging AWS for the environment, and adopting CI/CD principles. These practices ensure that all changes undergo testing before deployment and facilitate automatic deployment alongside the execution of periodic tasks.

The primary development effort has been focused on creating an API that serves an ML model, located within the `tkww_api` directory. This includes:
- A `service` layer responsible for the logic
- `envelopes` for ensuring the integrity of input and output data using Pydantic for validation,
- `controllers` for defining the API endpoints,
- and a `util` folder containing models, data, and various utility functions.

For the periodic retraining task, development is encapsulated in `retrainings.py`, utilizing HTTP communication with the API for model updates. While alternatives like Kafka were considered for their benefits in distributed messaging, HTTP was chosen for its simplicity and sufficiency for the PoC's scope.

Additional documentation has been created using MKDocs to provide comprehensive insights into the project. Logging mechanisms are in place to ensure transparency and traceability. A `test` directory has been established, currently housing a few unit tests. However, to guarantee the API's functionality and robustness, further testing strategies including integration tests, load tests, acceptance tests, and compatibility tests are deemed necessary. Time constraints have limited the extent of testing, but the importance of these tests is well recognized for future development.

This project's development emphasizes the application of MLOps practices to streamline the deployment and maintenance of ML models, ensuring that the API remains robust, scalable, and efficient.