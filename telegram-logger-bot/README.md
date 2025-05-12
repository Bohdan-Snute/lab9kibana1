##  How to Run and Stop the EFK Stack and Telegram Bot

###  1. How to Safely Stop the EFK Stack:

1. Navigate to the directory with the `docker-compose.yml` file:

   ```bash
   cd ./EFK-stack
   ```
2. Stop all services:

   ```bash
   docker compose down
   ```

   > This will gracefully shut down all EFK components and remove the containers while preserving data in volumes.

---

###  2. How to Start the EFK Stack Again:

1. Ensure you're in the `EFK-stack` directory:

   ```bash
   cd ./EFK-stack
   ```
2. Launch the services in the background:

   ```bash
   docker compose up -d
   ```
3. Check container status:

   ```bash
   docker compose ps
   ```
4. Open Kibana in your browser:

   ```
   http://localhost:5601
   ```
5. **(Required after every restart)** Add an index pattern in Kibana:

   * Go to **Stack Management → Index Patterns**
   * Click **Create index pattern**
   * In the pattern field, enter:

     ```
     fluentd-*
     ```
   * Click **Next step**
   * Choose the time field:

     ```
     @timestamp
     ```
   * Click **Create index pattern**

---

###  3. How to Run the Telegram Bot:

1. Navigate to the bot’s directory:

   ```bash
   cd ../telegram-logger-bot
   ```
2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

   > If not created yet, run:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the bot:

   ```bash
   python bot.py
   ```
4. Test the bot by sending a message to it via Telegram.

---

###  4. How to Stop the Bot:

1. Press `Ctrl + C` in the terminal running the bot.
2. Deactivate the virtual environment:

   ```bash
   deactivate
   ```

---

###  Final Check:

1. Go to Kibana:

   ```
   http://localhost:5601
   ```
2. Confirm that new logs appear after sending a message to the bot.

---