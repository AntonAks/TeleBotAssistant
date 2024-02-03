# TeleBotAssistant

TeleBotAssistant is a simple yet powerful Telegram bot which connects to ChatGPT to provide engaging and dynamic chat interactions.

## Configuration

You can configure the bot using environment variables. These can be provided either through a `.env` file, or a `.env.local` file for local-specific settings.

The following environment variables are required:

- `API_TELEGRAM_KEY`: Your Telegram API key. You can get this from BotFather on Telegram.

- `API_LLM_KEY`: Your API key for Language Model. Currently, only OpenAI API keys are supported.

- `ADMIN_KEY`: Your personal Telegram key. This is used to restrict who can interact with the bot.

Ensure these variables are properly set before running the bot.

## Running the Application

TeleBotAssistant is packaged as a Docker application. If you have Docker and Docker Compose installed, you can run the bot with the following commands:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Run the application:

   ```bash
   docker-compose up
   ```

By default, the bot will run in the foreground and log to the console. You can stop the bot by pressing `Ctrl+C`.

We hope you enjoy using the TeleBotAssistant and are excited to see what you will do with it!