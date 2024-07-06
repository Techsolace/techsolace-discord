# TECHSOLACE DISCORD

This project is a Discord bot that uses Google Generative AI, `discord.py`, and `jishaku`. Follow the instructions below to set up and run the bot.

## Prerequisites

Make sure you have the following installed:

- Python 3.11 or higher
- A Discord account with a bot token

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Techsolace/techsolace-discord.git
   cd techsolace-discord
   ```

2. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the project root directory and add your Discord bot token and any other necessary environment variables:

   ```env
   TOKEN=""
   GEMINI_API_KEY=""
   ```

## Running the Bot

1. **Run the bot:**

   ```sh
   python app.py
   ```

2. **Invite the bot to your server:**

   Use the OAuth2 URL Generator in the Discord Developer Portal to create an invite link for your bot. Make sure to give it the necessary permissions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or need help, feel free to open an issue or contact the project maintainers.
