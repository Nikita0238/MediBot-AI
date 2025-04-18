
# 🤖 MediBot-AI – ИИ-бот для медицинских рекомендаций  

**MediBot-AI** – это умный Telegram-бот на Python, который анализирует симптомы пользователей и рекомендует подходящих медицинских специалистов.  

## 🚀 Функционал  

- 🏥 **Распознавание симптомов** и подбор врача.  
- 🎯 **Использование алгоритмов ИИ** для персонализированных рекомендаций.  
- 🔄 **Интерактивный диалог** с пользователем.  
- 📊 **Обработка физического состояния пациента** для более точных советов.  
- 📝 **Поддержка широкого списка специалистов** (терапевт, хирург, ЛОР, стоматолог, кардиолог и др.).  
- ❗ **Важно!** Данные в коде являются примером и не являются подробной и точной информацией. 

## 🛠 Установка и запуск  

### 1️⃣ Клонирование репозитория  
```

git clone https://github.com/yourusername/MediBot-AI.git
```

``
### 2️⃣ Установка зависимостей  
```

pip install -r requirements.txt
```

``
### 3️⃣ Настройка и запуск бота  

#### Открываем config.py и вставляем свой Telegram Token
```
nano config.py  
```
### Добавляем в файл:
```
TELEGRAM_BOT_TOKEN = "твой_секретный_токен"
```
# Запускаем бота
```
python bot.py
```
## 🔒 Безопасность
Перед запуском создайте .env файл и добавьте в него ваш Telegram Bot API Token:
```
TELEGRAM_BOT_TOKEN=твой_секретный_токен
```
### 🛠 Установите python-dotenv, чтобы загружать токен из .env:
```
pip install python-dotenv
```
## 📌 Требования  

Python 3.8+  
telebot  
python-telegram-bot  
Telegram API Token  


## 📜 Лицензия  

Проект распространяется под MIT License – свободное использование с указанием авторства.


---

✉ **Контакты:**  

Email: golubn602@gmail.com  
Telegram: @nikita227228
