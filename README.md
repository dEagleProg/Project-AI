# Project-AI

A Telegram bot project developed using the aiogram 3.x framework. The bot features a modular structure with separate user and admin interfaces.

## Technologies

- Python 3.x
- aiogram 3.17.0
- SQLAlchemy 2.0.37
- OpenAI API
- Docker

## Installation and Setup

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Project-AI.git
cd Project-AI
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/MacOS
# or
venv\Scripts\activate  # for Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `config.py` file and add your bot token:
```python
TOKEN = "your_bot_token"
```

5. Run the bot:
```bash
python run.py
```

### Docker Setup

1. Build the Docker image:
```bash
docker build -t project-ai .
```

2. Run the container:
```bash
docker run -d --name project-ai project-ai
```

## Project Structure

```
Project-AI/
├── app/
│   ├── admin/         # Admin commands
│   ├── user/          # User commands
│   └── database/      # Database models
├── dockerfile
├── requirements.txt
└── run.py
```

## License

MIT

## 👤 Author

[dEagleProg](https://github.com/dEagleProg)
