# DevTrack

## Overview

DevTrack is a Django-based backend API for tracking engineering issues. Reporters can create issues, assign priorities, and track status updates.

---

## Setup Instructions

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Django

```bash
pip install django
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## API Endpoints

### Reporter APIs

* POST /api/reporters/
* GET /api/reporters/
* GET /api/reporters/?id=1

### Issue APIs

* POST /api/issues/
* GET /api/issues/
* GET /api/issues/?id=1
* GET /api/issues/?status=open

---

## OOP Concepts Used

* Abstract Base Class (BaseEntity)
* Inheritance
* Method Overriding
* Validation Methods
* Object Serialization using to_dict()

---

## Design Decision

I stored data in JSON files (reporters.json and issues.json) instead of a database because the assignment explicitly required file-based storage. This approach keeps the project lightweight while demonstrating API design, object-oriented programming concepts, validation, inheritance, and Django routing.

---

## Screenshots

### Reporter APIs

#### Create Reporter (POST)

![Reporter POST Success](screenshots/1)%20reporter_post_success.png)


#### Get All Reporters (GET)

![Reporter GET All Success](screenshots/2)%20reporter_get_all_success.png)


#### Get Reporter By ID (GET)

![Reporter GET By ID Success](screenshots/3)%20reporter_get_by_id_success.png)


#### Reporter Not Found (404)

![Reporter Not Found Error](screenshots/4)%20reporter_get_not_found_error.png)



### Issue APIs

#### Create Critical Issue (POST)

![Issue POST Critical Success](screenshots/5)%20issue_post_critical_success.png)


#### Get All Issues (GET)

![Issue GET All Success](screenshots/6)%20issue_get_all_success.png)


#### Get Issue By ID (GET)

![Issue GET By ID Success](screenshots/7)%20issue_get_by_id_success.png)


#### Issue Not Found (404)

![Issue Not Found Error](screenshots/8)%20issue_get_not_found_error.png)


#### Filter Issues By Status (GET)

![Issue Status Filter Success](screenshots/9)%20issue_get_by_status_success.png)
