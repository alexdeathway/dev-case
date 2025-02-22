
![alt text](README/logo-final.png?raw=true)

Privacy friendly CMS, Blog and Portfolio made with Python & Django.

**Important note**: Release of the first stable version for production is planned on 10th August 2022.

![GitHub](https://img.shields.io/github/license/rob32/dev-case)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![Test-Lint Action](https://github.com/rob32/dev-case/actions/workflows/test-lint.yml/badge.svg)

---

# Features

- Responsive and uniqe Design
- Configuration via Django-Admin
- Blog
- Portfolio & Project Showcase
- Social Media Links/Icons
- About Me with Skills (optional with downloadable Resume)
- Markdown Support with Syntaxhighlight and TOC
- Contact-Form
- RSS
- Search
- Dynamic Pages (Footer)
- Dark Django-Admin Theme
- Favicon
- Optimized for good SEO
- Dynamic sitemap.xml and robots.txt
- Settings for S3 compatible-storage (optional)
- Email Notification (optional WIP)
- Comments (optional WIP)

# Table of contents

- [Features](#features)
- [Table of contents](#table-of-contents)
- [Screenshots](#screenshots)
- [Quick-Start (Docker)](#quick-start-docker)
- [Local Development](#local-development)
  - [Setup](#setup)
  - [Frontend](#frontend)
  - [Tests](#tests)
- [Settings & Example .env](#settings--example-env)
- [Deployment Notes](#deployment-notes)
  - [S3 Storage](#s3-storage)
  - [Admin Location](#admin-location)
  - [Sitemap.xml](#sitemapxml)
  - [Robots.txt](#robotstxt)
- [Contribution](#contribution)
- [Todo/Roadmap](#todoroadmap)
- [Acknowledgements](#acknowledgements)
- [License](#license)

# Screenshots

Home

![alt text](README/screenshots/home-2.png?raw=true)

About

![About Page - Example](README/screenshots/about-1.png?raw=true)

Blogpost with Image

![Post with Image - Example](README/screenshots/post-with-image-1.png?raw=true)

Blogpost without Image

![Post without Image - Example](README/screenshots/post-without-image-1.png?raw=true)

Contact Page

![Contact Page](README/screenshots/contact-1.png?raw=true)

Admin Dashboard

![Admin Dashboard](README/screenshots/admin-1.png?raw=true)


Admin - About Config

![Admin Page - About Config](README/screenshots/admin-about-settings.png?raw=true)


# Quick-Start (Docker)

The fastest and easiest way to test dev-case:

```
git clone git@github.com:rob32/dev-case.git
cd dev-case
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

Important:

create a new .env file with the following content:

```
DEBUG=True
DATABASE_URL=psql://postgres:postgres@db:5432/postgres
```

Go to  `http://127.0.0.1:8000/` and check if all worked.

# Local Development

Development environment with Python (venv) and Node (optional).

## Setup

Tested with GNU/Linux & Mac:

```
git clone git@github.com:rob32/dev-case.git
cd dev-case
python3 -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
python3 manage.py migrate
pre-commit install
```

create a .env file with at least the following content:

```
DEBUG=True
# only if postgres is used, uncomend the next line (example):
# DATABASE_URL=psql://postgres:postgres@db:5432/postgres
```

Start the Development-Server with `python3 manage.py runserver`

Go to  `http://127.0.0.1:8000/`

## Frontend

```
# Install dependecies with:
npm install

# Build "Fronted" manually (uses `rm -rf` for cleaning):
npm run build
```

Optional: Start Backend-Server and Esbuild in watch-mode at the same time with `npm start`.


## Tests

```
# Unit/Integration Tests:
python3 manage.py test

# Code Quality with the help of pre-commit
pre-commit run -a -v
```

# Settings & Example .env

Possible settings via environment variables:

```
SECRET_KEY=insecure-secretkey12345
DEBUG=FALSE
ALLOWED_HOSTS=my-domain-name.com
DATABASE_URL=psql://postgres:postgres@db:5432/postgres
ADMIN_LOCATION=dev-case/
ROBOTS_DISALLOW=/contact/,/private-file.html`

FEED_TITLE="My Feed Title"
FEED_DESCRIPTION="My feed description"
```

# Deployment Notes

**WIP**

Example Security-Settings for production (via environment variables):

```
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## S3 Storage

Make sure that `USE_S3_STORAGE` is set to `True`.

Possible settings for S3 compatible storage (via environment variables):

```
USE_S3_STORAGE
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME
AWS_S3_ENDPOINT_URL
AWS_S3_CUSTOM_DOMAIN
AWS_LOCATION
AWS_IS_GZIPPED (Boolean)
AWS_S3_FILE_OVERWRITE (Boolean)
AWS_DEFAULT_ACL
```

## Admin Location

You can change the location for the admin area using the `ADMIN_LOCATION` environment variable. Default is `admin/`.

## Sitemap.xml

Change *DOMAIN NAME* and *DISPLAY NAME* via Admin-Panel (Sites App) to your actual domain name. Default is set to "example.com".

## Robots.txt

To add *Disallow* rules, use the `ROBOTS_DISALLOW` environment variable. For a valid Sitemap entry change your domain name as described in [Sitemap.xml](#sitemapxml).

Example: `ROBOTS_DISALLOW=/contact/,/private-file.html`

# Contribution

Contributions, Feedback and Feature-Requests are always welcome. To learn more, see the [Contributor Guide](https://github.com/rob32/dev-case/blob/main/CONTRIBUTING.md)

# Todo/Roadmap

- ~~CI for Tests & Code Quality~~
- tweak default security & caching (settings)
- ~~tweak SEO~~
- add/finish comments for Blog
- add captchas
- refactor views (queries)
- add docker-compose for production

# Acknowledgements

A big thanks to the following great projects:

- [django](https://github.com/django/django)
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- [django-extensions](https://github.com/django-extensions/django-extensions)
- [django-solo](https://github.com/lazybird/django-solo/)
- [django-environ](https://github.com/joke2k/django-environ)
- [Python-Markdown](https://github.com/Python-Markdown/markdown)
- [pygments](https://github.com/pygments/pygments)
- [esbuild](https://github.com/evanw/esbuild)

# License

The project is available under [GNU GPLv3](https://github.com/rob32/dev-case/blob/main/LICENSE.md) Licence.

---

If you like the project, please give it a star ⭐
