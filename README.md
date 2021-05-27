# Weather App

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)


## Project maintainers

Should you have any questions regarding this project, please feel free to @mention @inderbhushanjha

## Good first issues

Want to contribute to the Weather App project? Here are a couple of good first issues to get you started. Thanks!

[Good first issues](https://github.com/inderbhushanjha/WeatherForecast/issues)

## Browser support baseline

The following is a list of browser/version combinations that are supported by the interactive editor. In browsers that do not meet the criteria, the editor degrades gracefully to displaying static examples.

-   Firefox - Latest three release versions.
-   Chrome - Latest three release versions.
-   Opera - Latest two release versions.
-   Safari - Latest two release versions.
-   Internet Explorer - version 11.
-   Edge - Latest release version.

## Contributing

If you're interested in contributing to this project, great! Please see the [CONTRIBUTING](CONTRIBUTING.md) document.

## Contributors

Thanks goes to these wonderful people :

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars3.githubusercontent.com/inderbhushanjha" width="150px;"/><br /><sub><b>Inder Bhushan Jha</b></sub>](https://github.com/inderbhushanjha)<br />[💻](https://github.com/inderbhushanjha/WeatherForecast/commits/main "Code") |
<!-- ALL-CONTRIBUTORS-LIST:END -->

Contributions of any kind welcome!

## Installation

Install Django Framework:

    pip install django
Create ```.env``` file in the root directory and modify these settings:

    SECRET_KEY = Your Django secret key here
    DEBUG = True
    DB_NAME = Your Database name
    DB_USER = Database username
    DB_PASSWORD = Database password
    DB_HOST = HOST server address

Make migrations:

    python manage.py makemigrations
        
Migrate:

    python manage.py migrate
        
Run Server:

    python manage.py runserver
