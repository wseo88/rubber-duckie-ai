# Rubber Duckie 🦆

A FastAPI-based chatbot that uses OpenAI's GPT models with Redis for conversation memory storage. Like a rubber duck for debugging, this chatbot remembers your conversations and helps you think through problems. The project includes both a REST API backend and a Streamlit frontend for easy interaction.

## Features

- 🦆 **Rubber Duck Debugging**: Your AI companion for thinking through problems
- 🤖 **OpenAI Integration**: Uses GPT-4o-mini for intelligent responses
- 💾 **Redis Memory**: Stores conversation history in Redis with in-memory fallback
- 🚀 **FastAPI Backend**: High-performance REST API
- 🎨 **Streamlit Frontend**: User-friendly web interface
- 🔄 **Conversation Context**: Maintains conversation history for better responses
- ⚡ **Scalable**: Redis-based storage allows for horizontal scaling

## Project Structure

```
rubber-duckie/
├── app/
│   ├── main.py          # FastAPI application
│   ├── chat.py          # Chat logic and OpenAI integration
│   ├── memory.py        # Redis and in-memory storage
│   └── config.py        # Configuration management
├── frontend/
│   └── app.py           # Streamlit frontend
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## Prerequisites

- Python 3.8+
- Redis server (optional - falls back to in-memory storage)
- OpenAI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wseo88/rubber-duckie-ai.git
   cd rubber-duckie
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPEN_API_KEY=your_openai_api_key_here
   REDIS_HOST=localhost
   REDIS_PORT=6379
   ```

5. **Start Redis (optional)**
   ```bash
   # Using Docker
   docker run -d -p 6379:6379 redis:alpine
   
   # Or install Redis locally
   # Ubuntu/Debian: sudo apt install redis-server
   # macOS: brew install redis
   # Windows: Download from https://redis.io/download
   ```

## Usage

### Backend API

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

**API Endpoints:**
- `POST /chat` - Send a message to the chatbot
  ```json
  {
    "user_id": "user123",
    "message": "Hello, how are you?"
  }
  ```

### Frontend Interface

Start the Streamlit frontend:
```bash
streamlit run frontend/app.py
```

The web interface will be available at `http://localhost:8501`

## Configuration

The application can be configured through environment variables:

- `OPEN_API_KEY`: Your OpenAI API key (required)
- `REDIS_HOST`: Redis server host (default: localhost)
- `REDIS_PORT`: Redis server port (default: 6379)

## Memory System

The chatbot uses a dual storage approach:

1. **Redis Storage** (preferred): Stores conversation history in Redis for persistence and scalability
2. **In-Memory Fallback**: If Redis is unavailable, falls back to in-memory storage

Each user's conversation history is stored separately and limited to the last 5 messages for context.

## API Documentation

When the FastAPI server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Troubleshooting

### Common Issues

1. **Redis Connection Error**
   - Ensure Redis is running on the specified host/port
   - The app will fall back to in-memory storage if Redis is unavailable

2. **OpenAI API Error**
   - Verify your API key is correct and has sufficient credits
   - Check your internet connection

3. **Port Already in Use**
   - Change the port in the uvicorn command: `uvicorn app.main:app --reload --port 8001`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions, please [create an issue](link-to-issues) in the repository.
