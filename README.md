# Notification System

A scalable notification API supporting Email, SMS, and In-app messages.

## Features

- Asynchronous delivery via kafka queue
- Retry on failure
- REST endpoints for sending and retrieving notifications

## Run Locally

Clone the project

```bash
  git clone https://github.com/srinithimitra/Notification_System.git
```

Go to the project directory

```bash
  cd Notification_System
```

Create virtual environment and activate it

```bash
    python -m venv .venv
    source ./.venv/Scripts/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python -m src
```

Access the doc link at

```bash
    http://localhost:8000/docs
```

## Authors

- [@srinithimitra](https://github.com/srinithimitra)

## License

[MIT](https://choosealicense.com/licenses/mit/)
