<h1 align="center">
  <a href="https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08">
    <!-- Please provide path to your logo here -->
    <img src="docs/images/logo.png" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
  INFOM126_GROUPE_08
  <br />
  <br />

  [![Pipeline status](https://img.shields.io/github/actions/workflow/status/UNamurCSFaculty/2324_INFOM126_GROUPE_08/main.yml?style=flat-square&label=Main-pipeline
)](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/actions/workflows/main.yml)
  <br />
  <br />
  <a href="https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  ·
  <a href="https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/UNamurCSFaculty/2324_INFOM126_GROUPE_08.svg?style=flat-square)](LICENSE)
[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
    - [Built With](#built-with)
- [Getting Started](#getting-started)
    - [Before running the app](#before-running-the-app)
    - [Development purpose](#development-purpose)
    - [Production purpose](#production-purpose)
- [Roadmap](#roadmap)
- [Support](#support)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)

</details>

---

## About

This project is a small application for generating a QR code from a URL, with the added feature of a feedback function. The aim of this use case is to put into practice the implementation of a production pipeline based on a technology stack. A demo of the project is accessible on [79.124.7.38](http://79.124.7.38).

### Built With

- Database : PostgreSQL
- Back-end : Flask, SQLAlchemy, pytest
- Front-end : Vue3, cypress

## Getting Started

### Before running the app

Before running the project, you need to configure some environment variables.

- `POSTGRES_USER` : the username of the database
- `POSTGRES_PASSWORD` : the password of the user for the database
- `POSTGRES_DB` : the name of the database
- `HOST_ADDRESS` : the address where the project will be run, `http://localhost` if deployed locally or `http://example.com` is deployed on a production server

To do so, you have two options:

1) Create an `.env` file at the root of the project

2) Add variables in your own environment

Note that the first option is prefered.

#### Create an ´.env´ file

The file should contain the 4 variables above. It should look like this:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=grespost
POSTGRES_DB=INFOM126
HOST_ADDRESS=http://localhost
```

#### Add variables manualy

You can export manually these variables in your environment. To do so, execute the following commands in your terminal:

```sh
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=grespost
export POSTGRES_DB=INFOM126
export HOST_ADDRESS=http://localhost
```

### Development purpose

If you want to run the application in a development context, run the following command :

```sh 
docker compose up
```

This will use the `docker-compose.yml` script used for a development environment.

The files inside `/back-end` and `/front-end` can be changed while services are running with the usage of volumes in the script. Thus the project will be dynamically updated without the need of restarting the containers.

The following ports will be used by the services:

- `5432`: `database` i.e. the Postgres database
- `5000`: `back-end` i.e. the Flask API app
- `3000`: `front-end` i.e. the Vue project running a Node server

### Production purpose

If you just want to run the application, set your current directory to the root of the project and run :

```sh
docker compose -f 'docker-compose.prod.yml' up
```

This will use the `docker-compose.prod.yml` script aiming for a production context.

The following ports will be used by the services:

- `5432`: `database` i.e. the Postgres database
- `5000`: `back-end` i.e. the Flask API app deployed with the waitress server
- `80`: `front-end` i.e. the Vue project deployed on a Nginx server

## Roadmap

See the [open issues](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Send a mail to our support [support@infom126-groupe-08.be](contact@infom126-groupe-08.be)

## Project assistance

If you want to say **thank you** or/and support active development of INFOM126_GROUPE_08:

- Add a [GitHub Star](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08) to the project.
- Use the #INFOM126_GROUPE_08 hashtag on your favorite social network.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make INFOM126_GROUPE_08 **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

<!-- The original setup of this repository is by [Hugo Boss](https://github.com/UNamurCSFaculty). ????????????????? -->

For a full list of all authors and contributors, see [the contributors page](https://github.com/UNamurCSFaculty/2324_INFOM126_GROUPE_08/contributors).

## Security

INFOM126_GROUPE_08 follows good practices of security, but 100% security cannot be assured.
INFOM126_GROUPE_08 is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.
