import telebot
from telegram.ext import Updater, CommandHandler
from queue import Queue

bot = telebot.TeleBot('6568438533:AAHpKtlnUdztuCW5NcVbNj5T4tCqRNVvEkc')
@bot.message_handler(commands=['start'])
def command_start(message):
  bot.send_message(message.chat.id, "Привет! Я бот для выбора специалиста в медицинской сфере. Опишите свои симптомы, и я помогу вам найти подходящего врача.")
class MedicalBot:
    def __init__(self):
        self.specialty_map = {
            "терапевт": {
                "symptoms": ["головная боль", "кашель", "температура"],
                "doctor_type": "General Practitioner"
            },
            "хирург": {
                "symptoms": ["повреждение", "резкая боль"],
                "doctor_type": "Surgeon"
            },
            "лор": {
                "symptoms": ["насморк", "боль в горле", "потеря слуха"],
                "doctor_type": "ENT Doctor"
            },
            "офтальмолог": {
                "symptoms": ["покраснение глаз", "смазанный зрительный образ"],
                "doctor_type": "Ophthalmologist"
            },
            "стоматолог": {
                "symptoms": ["зубная боль", "кровоточащие десны"],
                "doctor_type": "Dentist"
            },
            "дерматолог": {
                "symptoms": ["сыпь", "зуд", "покраснение кожи"],
                "doctor_type": "Dermatologist"
            },
            "гинеколог": {
                "symptoms": ["менструальные боли", "выделения", "покровытие матки"],
                "doctor_type": "Gynecologist"
            },
            "уролог": {
                "symptoms": ["боль при мочеиспускании", "изменения в моче", "проблемы с почками"],
                "doctor_type": "Urologist"
            },
            "невролог": {
                "symptoms": ["головная боль", "потеря сознания", "паралич"],
                "doctor_type": "Neurologist"
            },
            "педиатр": {
                "symptoms": ["гиперактивность", "рвота", "высокая температура"],
                "doctor_type": "Pediatrician"
            },
            "кардиолог": {
                "symptoms": ["затруднение дыхания", "боль в груди", "аритмия"],
                "doctor_type": "Cardiologist"
            },
            "пульмонолог": {
                "symptoms": ["затруднение дыхания", "кашель с мокротой", "хрипы в груди"],
                "doctor_type": "Pulmonologist"
            },
            "гастроэнтеролог": {
                "symptoms": ["жжение в области желудка", "изменения в стуле", "вздутие живота"],
                "doctor_type": "Gastroenterologist"
            },
            "эндокринолог": {
                "symptoms": ["изменения веса", "чрезмерная жажда", "нерегулярный цикл"],
                "doctor_type": "Endocrinologist"
            },
            "ревматолог": {
                "symptoms": ["боли в суставах", "утренняя скованность", "опухание суставов"],
                "doctor_type": "Rheumatologist"
            },
            "онколог": {
                "symptoms": ["необъяснимая потеря веса", "узлы на теле", "постоянная усталость"],
                "doctor_type": "Oncologist"
            },
            "аллерголог": {
                "symptoms": ["чихание", "насморк", "кожные высыпания"],
                "doctor_type": "Allergist"
            },
            "психиатр": {
                "symptoms": ["депрессия", "панические атаки", "сонные расстройства"],
                "doctor_type": "Psychiatrist"
            },
            "психотерапевт": {
                "symptoms": ["стресс", "травмы прошлого", "неспособность принимать решения"],
                "doctor_type": "Psychotherapist"
            },
            "фтизиатр": {
                "symptoms": ["кашель кровью", "потеря веса", "слабость"],
                "doctor_type": "Pulmonologist"
            },
            "массажист": {
                "symptoms": ["напряжение в мышцах", "боль в спине", "головная боль"],
                "doctor_type": "Massage Therapist"
            },

        }

    def recommend_doctor(self, symptoms):
        recommendation = self.specialty_map.get(symptoms)
        if recommendation:
            return f"При {symptoms} рекомендуется обратиться к {recommendation['doctor_type']}."
        return "К сожалению, не удалось найти подходящего врача."



@bot.message_handler(func=lambda message: True)
def echo(message):
  symptoms = message.text
  recommendation = bot.recommend_doctor(symptoms)
  bot.send_message(message.chat.id, recommendation)
bot = MedicalBot()
queue = Queue()
updater = Updater('6568438533:AAHpKtlnUdztuCW5NcVbNj5T4tCqRNVvEkc',queue)
updater.start_polling()