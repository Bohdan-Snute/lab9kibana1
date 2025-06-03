````markdown
# 🧠 Система моніторингу з Prometheus, Grafana та Telegram-ботом

Цей репозиторій демонструє повноцінне розгортання системи спостереження за допомогою **Prometheus**, **Grafana** та кастомного **Telegram-бота**, який відкриває метрики через HTTP.

---

## ⚙️ Крок 1: Запускаємо Prometheus і Grafana

1. Відкрийте термінал і перейдіть у директорію з `docker-compose.yml`:

   ```bash
   cd ./prometheus-lab/PrometheusLab
````

2. Запускаємо сервіси за допомогою Docker:

   ```bash
   docker compose up
   ```

3. Перевіряємо, що все працює:

   * 🌐 Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090)
   * 📉 Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000)

---

## 🤖 Крок 2: Telegram-бот і метрики

1. Перейдіть до директорії з ботом:

   ```bash
   cd ./telegram_bot
   ```

2. Створіть Python-віртуальне середовище, якщо ще не створене, і активуйте його:

   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   # або
   source venv/bin/activate       # Linux/macOS
   ```

3. Встановіть залежності:

   ```bash
   pip install -r requirements.txt
   ```

4. Запустіть бота:

   ```bash
   python bot.py
   ```

5. Перевірте доступність метрик у браузері:

   * 📊 [http://127.0.0.1:9091/metrics](http://127.0.0.1:9091/metrics)

   Ви побачите щось типу:

   ```
   # HELP received_messages_total Total number of received Telegram messages
   # TYPE received_messages_total counter
   received_messages_total 5.0
   ```

---

## 📊 Крок 3: Додаємо джерело даних у Grafana

1. Відкрийте [Grafana](http://127.0.0.1:3000) в браузері

   * Логін: `admin`
   * Пароль: `admin`

2. У лівому меню натисніть:

   ```
   ☰ → Connections → Data Sources → Add data source
   ```

3. Оберіть тип: **Prometheus**

4. У полі `URL` вкажіть:

   ```
   http://prometheus:9090
   ```

5. Натисніть **Save & test**

---

## 📈 Крок 4: Створюємо дашборд у Grafana

1. Зайдіть у меню:

   ```
   Dashboards → New → Explore
   ```

2. В полі для метрик введіть:

   ```
   received_messages_total
   ```

3. Натисніть **Run Query**, далі:

   ```
   → Add to dashboard → New panel
   ```

4. Дайте панелі назву та збережіть дашборд

---

## 🛑 Крок 5: Завершення роботи

### Зупинити Docker-сервіси (Prometheus + Grafana):

```bash
cd ./prometheus-lab/PrometheusLab
docker compose down
```

### Зупинити Telegram-бота:

1. Натисніть `Ctrl + C` у терміналі, де він запущений
2. Деактивуйте віртуальне середовище:

   ```bash
   deactivate
   ```

---

## 🔗 Корисні посилання

* Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090)
* Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000)
* Метрики Telegram-бота: [http://127.0.0.1:9091/metrics](http://127.0.0.1:9091/metrics)

```
