import os
import telebot
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для выбора специалиста в медицинской сфере. Опишите свои симптомы, и я помогу вам найти подходящего врача.")

class MedicalBot:
    def __init__(self):
        self.specialty_map = {
            "терапевт": ["головная боль", "кашель", "температура"],
            "хирург": ["повреждение", "резкая боль"],
            "лор": ["насморк", "боль в горле", "потеря слуха"],
            "офтальмолог": ["покраснение глаз", "смазанный зрительный образ"],
            "стоматолог": ["зубная боль", "кровоточащие десны"],
            "дерматолог": ["сыпь", "зуд", "покраснение кожи"],
            "гинеколог": ["менструальные боли", "выделения"],
            "уролог": ["боль при мочеиспускании", "изменения в моче"],
            "невролог": ["головная боль", "потеря сознания", "паралич"],
            "педиатр": ["гиперактивность", "рвота", "высокая температура"],
            "кардиолог": ["затруднение дыхания", "боль в груди", "аритмия"],
            "пульмонолог": ["кашель с мокротой", "хрипы в груди"],
            "гастроэнтеролог": ["жжение в области желудка", "вздутие живота"],
            "эндокринолог": ["изменения веса", "чрезмерная жажда"],
            "ревматолог": ["боли в суставах", "утренняя скованность"],
            "онколог": ["необъяснимая потеря веса", "узлы на теле"],
            "аллерголог": ["чихание", "насморк", "кожные высыпания"],
            "психиатр": ["депрессия", "панические атаки"],
            "психотерапевт": ["стресс", "травмы прошлого"],
            "фтизиатр": ["кашель кровью", "потеря веса"],
            "массажист": ["напряжение в мышцах", "боль в спине"]
        }

    def recommend_doctor(self, symptoms):
        found_specialties = []
        for specialty, symptom_list in self.specialty_map.items():
            if any(symptom in symptoms.lower() for symptom in symptom_list):
                found_specialties.append(specialty)

        if found_specialties:
            return f"Вам следует обратиться к: {', '.join(found_specialties)}."
        return "К сожалению, не удалось найти подходящего врача."

medibot = MedicalBot()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    symptoms = message.text
    recommendation = medibot.recommend_doctor(symptoms)
    bot.send_message(message.chat.id, recommendation)

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
