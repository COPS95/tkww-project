# TKWW Project

This project encompasses the development of an API designed to serve predictions from a machine learning model, specifically a RandomForestClassifier from the sklearn. The primary functionality of the API is to expose a GET /predict endpoint. This endpoint accepts input features ("sepallength", "sepalwidth", "petallength", "petalwidth") and returns a prediction in JSON format, including the species predicted and the name of the model used for the prediction.

Additionally, the project includes a scheduled task feature that simulates periodic re-trainings of the model. This task randomly selects one of the provided models, evaluates it using test metrics, and then communicates with the API to update the model currently in service. This ensures that the model serving predictions remains optimal over time. The periodic re-training task is executed using GitHub Actions.

The API is deployed on an AWS EC2 instance, making it accessible for public use. You can interact with the API through the public endpoint at `http://18.201.57.160:80`.

For more detailed information about the project, including how to use the API and an overview of the scheduled tasks, please visit our documentation site at [https://cops95.github.io/tkww-project/](https://cops95.github.io/tkww-project/).



## Getting Started

To get started with the project, you will first need to clone the repository to your local machine. This can be done by executing the following command in your terminal:

```
git clone https://github.com/COPS95/tkww-project.git
```

After cloning the project, it is recommended to create a virtual environment to manage the project's dependencies separately from your global Python environment. You can create a virtual environment by running:

```
python -m venv env_name
```

Replace `env_name` with your preferred name for the virtual environment. Once the virtual environment is set up, you should activate it. The activation command varies depending on your operating system.

Next, to install the project dependencies, you'll first need to install Poetry, a tool for dependency management and packaging in Python. Install Poetry using pip:

```
pip install poetry
```

With Poetry installed, you can now install the project dependencies. To install all dependencies, including those required for documentation and testing, run:

```
poetry install --with docs,test
```

If you only need the base dependencies for the project, simply running `poetry install` will suffice. This will install the necessary packages to get the project up and running for development and testing purposes.

