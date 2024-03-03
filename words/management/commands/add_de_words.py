from django.core.management.base import BaseCommand
from words.models import Word


class Command(BaseCommand):
    help = 'Add words to the Word model'

    def handle(self, *args, **options):
        words_array = [{
    "origin_word": "die Karte",
    "rus_translation": "карта; открытка",
    "support_word": {
      "Landkarte": "географическая карта",
      "Spielkarte": "игральная карта",
      "Grußkarte": "поздравительная открытка",
      "mit dem Text": "с текстом"
    }
  },
  {
    "origin_word": "der Koffer",
    "rus_translation": "чемодан",
    "support_word": {
      "Gepäck": "багаж",
      "Reise": "путешествие",
      "Griff": "ручка",
      "mit den Rädern": "с колесами"
    }
  },
  {
    "origin_word": "das Geschenk",
    "rus_translation": "подарок",
    "support_word": {
      "Geburtstag": "день рождения",
      "Überraschung": "сюрприз",
      "Schleife": "бант",
      "mit dem Papier": "с бумагой"
    }
  },
  {
    "origin_word": "die Kamera",
    "rus_translation": "фотоаппарат; видеокамера",
    "support_word": {
      "Foto": "фото",
      "Video": "видео",
      "Objektiv": "объектив",
      "mit dem Blitz": "со вспышкой"
    }
  },
  {
    "origin_word": "der Computer",
    "rus_translation": "компьютер",
    "support_word": {
      "Bildschirm": "экран",
      "Tastatur": "клавиатура",
      "Maus": "мышь",
      "mit dem Internet": "с интернетом"
    }
  },
  {
    "origin_word": "der Film",
    "rus_translation": "фильм; плёнка",
    "support_word": {
      "Kino": "кино",
      "Schauspieler": "актёр",
      "Regisseur": "режиссёр",
      "mit dem Ton": "со звуком"
    }
  },
  {
    "origin_word": "die Blume",
    "rus_translation": "цветок",
    "support_word": {
      "Rose": "роза",
      "Tulpe": "тюльпан",
      "Garten": "сад",
      "mit dem Duft": "с ароматом"
    }
  },
  {
    "origin_word": "die Vase",
    "rus_translation": "ваза",
    "support_word": {
      "Glas": "стекло",
      "Porzellan": "фарфор",
      "Blumen": "цветы",
      "mit dem Wasser": "с водой"
    }
  },
  {
    "origin_word": "das Bild",
    "rus_translation": "картина",
    "support_word": {
      "Malerei": "живопись",
      "Rahmen": "рама",
      "Farbe": "цвет",
      "mit dem Pinsel": "с кистью"
    }
  },
  {
    "origin_word": "das Handtuch",
    "rus_translation": "носовой платок",
    "support_word": {
      "Stoff": "ткань",
      "Nase": "нос",
      "Schnupfen": "насморк",
      "mit dem Muster": "с узором"
    }
  },
  {
    "origin_word": "der Ball",
    "rus_translation": "мяч",
    "support_word": {
      "Fußball": "футбол",
      "Basketball": "баскетбол",
      "Tennis": "теннис",
      "mit dem Leder": "с кожей"
    }
  },
  {
    "origin_word": "der Luftballon",
    "rus_translation": "воздушный шар(ик)",
    "support_word": {
      "Helium": "гелий",
      "Geburtstag": "день рождения",
      "Fliegen": "летать",
      "mit dem Faden": "с ниткой"
    }
  },
  {
    "origin_word": "das Spielzeug",
    "rus_translation": "игрушка",
    "support_word": {
      "Puppe": "кукла",
      "Auto": "машина",
      "Lego": "лего",
      "mit dem Knopf": "с кнопкой"
    }
  },
  {
    "origin_word": "die Rechnung",
    "rus_translation": "счёт (для оплаты)",
    "support_word": {
      "Restaurant": "ресторан",
      "Geld": "деньги",
      "Trinkgeld": "чаевые",
      "mit dem Kellner": "с официантом"
    }
  },
  {
    "origin_word": "der Umschlag",
    "rus_translation": "конверт",
    "support_word": {
      "Brief": "письмо",
      "Post": "почта",
      "Marke": "марка",
      "mit dem Kleber": "с клеем"
    }
  },
  {
    "origin_word": "das Papier",
    "rus_translation": "бумага",
    "support_word": {
      "Schreiben": "писать",
      "Lesen": "читать",
      "Drucken": "печатать",
      "mit dem Bleistift": "с карандашом"
    }
  },
  {
    "origin_word": "die Zeitung",
    "rus_translation": "газета",
    "support_word": {
      "Nachrichten": "новости",
      "Journalist": "журналист",
      "Abonnement": "подписка",
      "mit dem Datum": "с датой"
    }
  },
  {
    "origin_word": "der Brief",
    "rus_translation": "письмо",
    "support_word": {
      "Adresse": "адрес",
      "Unterschrift": "подпись",
      "Grüße": "приветы",
      "mit dem Inhalt": "с содержанием"
    }
  },
  {
    "origin_word": "die Fahrkarte",
    "rus_translation": "билет (на поезд)",
    "support_word": {
      "Zug": "поезд",
      "Bahnhof": "вокзал",
      "Schaffner": "кондуктор",
      "mit dem Preis": "с ценой"
    }
  },
  {
    "origin_word": "die Kleidung",
    "rus_translation": "одежда",
    "support_word": {
      "Mode": "мода",
      "Anziehen": "одеваться",
      "Waschen": "стирать",
      "mit dem Stil": "со стилем"
    }
  },
  {
    "origin_word": "die Schuhe",
    "rus_translation": "обувь",
    "support_word": {
      "Fuß": "нога",
      "Laufen": "бегать",
      "Schnürsenkel": "шнурки",
      "mit dem Absatz": "с каблуком"
    }
  },
  {
    "origin_word": "der Mantel",
    "rus_translation": "пальто",
    "support_word": {
      "Winter": "зима",
      "Kälte": "холод",
      "Knopf": "пуговица",
      "mit dem Kragen": "с воротником"
    }
  },
  {
    "origin_word": "das Kleid",
    "rus_translation": "платье",
    "support_word": {
      "Frau": "женщина",
      "Feier": "праздник",
      "Rock": "юбка",
      "mit dem Gürtel": "с поясом"
    }
  },
  {
    "origin_word": "das Hemd",
    "rus_translation": "рубашка",
    "support_word": {
      "Mann": "мужчина",
      "Arbeit": "работа",
      "Kragen": "воротник",
      "mit dem Knopf": "с пуговицей"
    }
  },
  {
    "origin_word": "der Rock",
    "rus_translation": "юбка",
    "support_word": {
      "Frau": "женщина",
      "Bein": "нога",
      "Reißverschluss": "молния",
      "mit dem Stoff": "с тканью"
    }
  },
  {
    "origin_word": "der Handschuh",
    "rus_translation": "перчатка",
    "support_word": {
      "Hand": "рука",
      "Finger": "палец",
      "Wolle": "шерсть",
      "mit dem Futter": "с подкладкой"
    }
  },
  {
    "origin_word": "der Hut",
    "rus_translation": "шляпа",
    "support_word": {
      "Kopf": "голова",
      "Sonne": "солнце",
      "Feder": "перо",
      "mit dem Rand": "с полями"
    }
  },
  {
    "origin_word": "das Sakko",
    "rus_translation": "пиджак",
    "support_word": {
      "Mann": "мужчина",
      "Schulter": "плечо",
      "Tasche": "карман",
      "mit dem Knopf": "с пуговицей"
    }
  },
  {
    "origin_word": "die Jacke",
    "rus_translation": "куртка",
    "support_word": {
      "Körper": "тело",
      "Wind": "ветер",
      "Reißverschluss": "молния",
      "mit dem Kragen": "с воротником"
    }
  },
  {
    "origin_word": "der Schal",
    "rus_translation": "шарф",
    "support_word": {
      "Hals": "шея",
      "Wärme": "тепло",
      "Muster": "узор",
      "mit dem Knoten": "с узлом"
    }
  },
  {
    "origin_word": "die Socke",
    "rus_translation": "носок",
    "support_word": {
      "Fuß": "нога",
      "Schuh": "обувь",
      "Baumwolle": "хлопок",
      "mit dem Loch": "с дыркой"
    }
  },
  {
    "origin_word": "der Pullover",
    "rus_translation": "свитер",
    "support_word": {
      "Brust": "грудь",
      "Winter": "зима",
      "Ärmel": "рукав",
      "mit dem Ausschnitt": "с вырезом"
    }
  },
  {
    "origin_word": "das T-Shirt",
    "rus_translation": "футболка",
    "support_word": {
      "Bauch": "живот",
      "Sommer": "лето",
      "Aufdruck": "надпись",
      "mit dem Rundhals": "с круглым вырезом"
    }
  },
  {
    "origin_word": "die Krawatte",
    "rus_translation": "галстук",
    "support_word": {
      "Hemd": "рубашка",
      "Büro": "офис",
      "Seide": "шелк",
      "mit dem Knoten": "с узлом"
    }
  },
  {
    "origin_word": "die Hose",
    "rus_translation": "брюки",
    "support_word": {
      "Bein": "нога",
      "Gürtel": "ремень",
      "Hosenträger": "подтяжки",
      "mit dem Reißverschluss": "с молнией"
    }
  },
  {
    "origin_word": "der März",
    "rus_translation": "март",
    "support_word": {
      "Frühling": "весна",
      "Ostern": "Пасха",
      "Schnee": "снег",
      "mit dem Löwen": "с львом"
    }
  },
  {
    "origin_word": "der April",
    "rus_translation": "апрель",
    "support_word": {
      "Frühling": "весна",
      "Regen": "дождь",
      "Scherz": "шутка",
      "mit dem Narren": "с дураком"
    }
  },
  {
    "origin_word": "der Mai",
    "rus_translation": "май",
    "support_word": {
      "Frühling": "весна",
      "Blume": "цветок",
      "Feiertag": "праздник",
      "mit dem Kranz": "с венком"
    }
  },
  {
    "origin_word": "der Juni",
    "rus_translation": "июнь",
    "support_word": {
      "Sommer": "лето",
      "Sonne": "солнце",
      "Schule": "школа",
      "mit dem Zeugnis": "с аттестатом"
    }
  },
  {
    "origin_word": "der Juli",
    "rus_translation": "июль",
    "support_word": {
      "Sommer": "лето",
      "Hitze": "жара",
      "Urlaub": "отпуск",
      "mit dem Eis": "с мороженым"
    }
  },
  {
    "origin_word": "der August",
    "rus_translation": "август",
    "support_word": {
      "Sommer": "лето",
      "Ernte": "урожай",
      "Sternschnuppe": "звездопад",
      "mit dem Löwen": "с львом"
    }
  },
  {
    "origin_word": "der September",
    "rus_translation": "сентябрь",
    "support_word": {
      "Herbst": "осень",
      "Blatt": "лист",
      "Schule": "школа",
      "mit dem Ranzen": "с ранцем"
    }
  },
  {
    "origin_word": "der Oktober",
    "rus_translation": "октябрь",
    "support_word": {
      "Herbst": "осень",
      "Kürbis": "тыква",
      "Halloween": "Хэллоуин",
      "mit dem Gespenst": "с привидением"
    }
  },
  {
    "origin_word": "der November",
    "rus_translation": "ноябрь",
    "support_word": {
      "Herbst": "осень",
      "Nebel": "туман",
      "Laterne": "фонарик",
      "mit dem Martin": "с Мартином"
    }
  },
  {
    "origin_word": "der Dezember",
    "rus_translation": "декабрь",
    "support_word": {
      "Winter": "зима",
      "Schnee": "снег",
      "Weihnachten": "Рождество",
      "mit dem Tannenbaum": "с елкой"
    }
  },
  {
    "origin_word": "der Frühling",
    "rus_translation": "весна",
    "support_word": {
      "Jahreszeit": "время года",
      "Blume": "цветок",
      "Vogel": "птица",
      "mit dem Grün": "с зеленью"
    }
  },
  {
    "origin_word": "der Sommer",
    "rus_translation": "лето",
    "support_word": {
      "Jahreszeit": "время года",
      "Sonne": "солнце",
      "Strand": "пляж",
      "mit dem Wasser": "с водой"
    }
  },
  {
    "origin_word": "der Herbst",
    "rus_translation": "осень",
    "support_word": {
      "Jahreszeit": "время года",
      "Blatt": "лист",
      "Wind": "ветер",
      "mit dem Gelb": "с желтым"
    }
  },
  {
    "origin_word": "der Winter",
    "rus_translation": "зима",
    "support_word": {
      "Jahreszeit": "время года",
      "Schnee": "снег",
      "Eis": "лед",
      "mit dem Weiß": "с белым"
    }
  },
  {
    "origin_word": "der Name",
    "rus_translation": "имя, фамилия",
    "support_word": {
      "Person": "персона",
      "Identität": "идентичность",
      "Vorname": "имя",
      "mit dem Nachname": "с фамилией"
    }
  },
  {
    "origin_word": "die Adresse",
    "rus_translation": "адрес",
    "support_word": {
      "Wohnort": "место жительства",
      "Straße": "улица",
      "Hausnummer": "номер дома",
      "mit dem Postleitzahl": "с почтовым индексом"
    }
  },
  {
    "origin_word": "die Nummer",
    "rus_translation": "номер",
    "support_word": {
      "Zahl": "число",
      "Reihenfolge": "порядок",
      "Telefon": "телефон",
      "mit dem Vorwahl": "с кодом"
    }
  },
  {
    "origin_word": "der Geburtstag",
    "rus_translation": "день рождения",
    "support_word": {
      "Datum": "дата",
      "Feier": "праздник",
      "Kuchen": "торт",
      "mit dem Geschenk": "с подарком"
    }
  },
  {
    "origin_word": "verheiratet",
    "rus_translation": "женатый/замужняя",
    "support_word": {
      "Ehe": "брак",
      "Partner": "партнер",
      "Ring": "кольцо",
      "mit dem Trauschein": "с свидетельством о браке"
    }
  },
  {
    "origin_word": "die Sache",
    "rus_translation": "вещь; дело",
    "support_word": {
      "Ding": "предмет",
      "Gegenstand": "объект",
      "Angelegenheit": "задача",
      "mit dem Sinn": "с смыслом"
    }
  },
  {
    "origin_word": "der Kugelschreiber",
    "rus_translation": "ручка",
    "support_word": {
      "Schreiben": "писать",
      "Tinte": "чернила",
      "Mine": "стержень",
      "mit dem Clip": "с зажимом"
    }
  },
  {
    "origin_word": "das Buch",
    "rus_translation": "книга",
    "support_word": {
      "Lesen": "читать",
      "Seite": "страница",
      "Autor": "автор",
      "mit dem Titel": "с названием"
    }
  },
  {
    "origin_word": "das Schach",
    "rus_translation": "шахматы",
    "support_word": {
      "Spiel": "игра",
      "Brett": "доска",
      "Figur": "фигура",
      "mit dem Schachmatt": "с шахом и матом"
    }
  },
  {
    "origin_word": "das Telefon",
    "rus_translation": "телефон",
    "support_word": {
      "Kommunikation": "общение",
      "Anruf": "звонок",
      "Nummer": "номер",
      "mit dem Hörer": "с трубкой"
    }
  },
  {
    "origin_word": "die Uhr",
    "rus_translation": "часы",
    "support_word": {
      "Zeit": "время",
      "Zifferblatt": "циферблат",
      "Zeiger": "стрелка",
      "mit dem Armband": "с ремешком"
    }
  },
  {
    "origin_word": "der Kamm",
    "rus_translation": "расчёска",
    "support_word": {
      "Haar": "волосы",
      "Zahn": "зуб",
      "Friseur": "парикмахер",
      "mit dem Griff": "с ручкой"
    }
  },
  {
    "origin_word": "der Fernseher",
    "rus_translation": "телевизор",
    "support_word": {
      "Bild": "изображение",
      "Ton": "звук",
      "Kanal": "канал",
      "mit dem Fernbedienung": "с пультом"
    }
  },
  {
    "origin_word": "das Bügeleisen",
    "rus_translation": "утюг",
    "support_word": {
      "Bügeln": "гладить",
      "Wäsche": "белье",
      "Hitze": "тепло",
      "mit dem Dampf": "с паром"
    }
  },
  {
    "origin_word": "die Seife",
    "rus_translation": "мыло",
    "support_word": {
      "Waschen": "мыть",
      "Schaum": "пена",
      "Duft": "аромат",
      "mit dem Wasser": "с водой"
    }
  },
  {
    "origin_word": "das Radio",
    "rus_translation": "радио",
    "support_word": {
      "Hören": "слушать",
      "Musik": "музыка",
      "Sender": "станция",
      "mit dem Lautsprecher": "с динамиком"
    }
  },
  {
    "origin_word": "die Tasche",
    "rus_translation": "сумка",
    "support_word": {
      "Tragen": "носить",
      "Sache": "вещь",
      "Reißverschluss": "молния",
      "mit dem Henkel": "с ручкой"
    }
  },
  {
    "origin_word": "gestern",
    "rus_translation": "вчера",
    "support_word": {
      "Tag": "день",
      "Vergangenheit": "прошлое",
      "Erinnerung": "воспоминание",
      "mit dem Datum": "с датой"
    }
  },
  {
    "origin_word": "heute",
    "rus_translation": "сегодня",
    "support_word": {
      "Tag": "день",
      "Gegenwart": "настоящее",
      "Plan": "план",
      "mit dem Wetter": "с погодой"
    }
  },
  {
    "origin_word": "morgen",
    "rus_translation": "завтра",
    "support_word": {
      "Tag": "день",
      "Zukunft": "будущее",
      "Hoffnung": "надежда",
      "mit dem Wecker": "с будильником"
    }
  },
  {
    "origin_word": "das Fest",
    "rus_translation": "праздник",
    "support_word": {
      "Feier": "празднование",
      "Freude": "радость",
      "Gäste": "гости",
      "mit dem Kuchen": "с тортом"
    }
  },
  {
    "origin_word": "das Mal",
    "rus_translation": "раз",
    "support_word": {
      "Zahl": "число",
      "Wiederholung": "повторение",
      "Erfahrung": "опыт",
      "mit dem Beispiel": "с примером"
    }
  },
  {
    "origin_word": "der Tag",
    "rus_translation": "день",
    "support_word": {
      "Zeit": "время",
      "Licht": "свет",
      "Sonne": "солнце",
      "mit dem Morgen": "с утром"
    }
  },
  {
    "origin_word": "der Morgen",
    "rus_translation": "утро",
    "support_word": {
      "Tageszeit": "время суток",
      "Anfang": "начало",
      "Frühstück": "завтрак",
      "mit dem Kaffee": "с кофе"
    }
  },
  {
    "origin_word": "der Abend",
    "rus_translation": "вечер",
    "support_word": {
      "Tageszeit": "время суток",
      "Ende": "конец",
      "Abendessen": "ужин",
      "mit dem Mond": "с луной"
    }
  },
  {
    "origin_word": "die Nacht",
    "rus_translation": "ночь",
    "support_word": {
      "Tageszeit": "время суток",
      "Dunkelheit": "тьма",
      "Schlaf": "сон",
      "mit dem Traum": "со сном"
    }
  },
  {
    "origin_word": "der Montag",
    "rus_translation": "понедельник",
    "support_word": {
      "Wochentag": "день недели",
      "Erster": "первый",
      "Arbeit": "работа",
      "mit dem Stress": "со стрессом"
    }
  },
  {
    "origin_word": "der Dienstag",
    "rus_translation": "вторник",
    "support_word": {
      "Wochentag": "день недели",
      "Zweiter": "второй",
      "Sport": "спорт",
      "mit dem Training": "с тренировкой"
    }
  },
  {
    "origin_word": "der Mittwoch",
    "rus_translation": "среда",
    "support_word": {
      "Wochentag": "день недели",
      "Dritter": "третий",
      "Mitte": "середина",
      "mit dem Kino": "с кино"
    }
  },
  {
    "origin_word": "der Donnerstag",
    "rus_translation": "четверг",
    "support_word": {
      "Wochentag": "день недели",
      "Vierter": "четвертый",
      "Lernen": "учеба",
      "mit dem Test": "с тестом"
    }
  },
  {
    "origin_word": "der Freitag",
    "rus_translation": "пятница",
    "support_word": {
      "Wochentag": "день недели",
      "Fünfter": "пятый",
      "Freizeit": "свободное время",
      "mit dem Freund": "с другом"
    }
  },
  {
    "origin_word": "der Samstag",
    "rus_translation": "суббота",
    "support_word": {
      "Wochentag": "день недели",
      "Sechster": "шестой",
      "Wochenende": "выходные",
      "mit dem Einkauf": "с покупками"
    }
  },
  {
    "origin_word": "der Sonntag",
    "rus_translation": "воскресенье",
    "support_word": {
      "Wochentag": "день недели",
      "Siebter": "седьмой",
      "Wochenende": "выходные",
      "mit dem Buch": "с книгой"
    }
  },
  {
    "origin_word": "der Monat",
    "rus_translation": "месяц",
    "support_word": {
      "Zeit": "время",
      "Kalender": "календарь",
      "Jahreszeit": "время года",
      "mit dem Namen": "с названием"
    }
  },
  {
    "origin_word": "der Januar",
    "rus_translation": "январь",
    "support_word": {
      "Monat": "месяц",
      "Erster": "первый",
      "Winter": "зима",
      "mit dem Schnee": "со снегом"
    }
  },
  {
    "origin_word": "der Februar",
    "rus_translation": "февраль",
    "support_word": {
      "Monat": "месяц",
      "Zweiter": "второй",
      "Winter": "зима",
      "mit dem Valentinstag": "с днем святого Валентина"
    }
  },
  {
    "origin_word": "der Pfirsich",
    "rus_translation": "персик",
    "support_word": {
      "Frucht": "фрукт",
      "Süß": "сладкий",
      "Kern": "косточка",
      "mit dem Flaum": "с пушком"
    }
  },
  {
    "origin_word": "die Tasse",
    "rus_translation": "чашка",
    "support_word": {
      "Geschirr": "посуда",
      "Trinken": "пить",
      "Henkel": "ручка",
      "mit dem Kaffee": "с кофе"
    }
  },
  {
    "origin_word": "das Glas",
    "rus_translation": "стакан",
    "support_word": {
      "Geschirr": "посуда",
      "Trinken": "пить",
      "Glas": "стекло",
      "mit dem Wasser": "с водой"
    }
  },
  {
    "origin_word": "der Teller",
    "rus_translation": "тарелка",
    "support_word": {
      "Geschirr": "посуда",
      "Essen": "есть",
      "Rund": "круглый",
      "mit dem Essen": "с едой"
    }
  },
  {
    "origin_word": "der Löffel",
    "rus_translation": "ложка",
    "support_word": {
      "Besteck": "столовый прибор",
      "Essen": "есть",
      "Löffeln": "ложить",
      "mit dem Suppe": "с супом"
    }
  },
  {
    "origin_word": "die Gabel",
    "rus_translation": "вилка",
    "support_word": {
      "Besteck": "столовый прибор",
      "Essen": "есть",
      "Zinken": "зубцы",
      "mit dem Salat": "с салатом"
    }
  },
  {
    "origin_word": "das Messer",
    "rus_translation": "нож",
    "support_word": {
      "Besteck": "столовый прибор",
      "Essen": "есть",
      "Schneiden": "резать",
      "mit dem Brot": "с хлебом"
    }
  },
  {
    "origin_word": "die Untertasse",
    "rus_translation": "блюдце",
    "support_word": {
      "Geschirr": "посуда",
      "Tasse": "чашка",
      "Klein": "маленький",
      "mit dem Keks": "с печеньем"
    }
  },
  {
    "origin_word": "die Flasche",
    "rus_translation": "бутылка",
    "support_word": {
      "Behälter": "емкость",
      "Trinken": "пить",
      "Korken": "пробка",
      "mit dem Wein": "с вином"
    }
  },
  {
    "origin_word": "die Serviette",
    "rus_translation": "салфетка",
    "support_word": {
      "Stoff": "ткань",
      "Essen": "есть",
      "Wischen": "вытирать",
      "mit dem Mund": "с ртом"
    }
  },
  {
    "origin_word": "das Frühstück",
    "rus_translation": "завтрак",
    "support_word": {
      "Essen": "есть",
      "Morgen": "утро",
      "Brot": "хлеб",
      "mit dem Ei": "с яйцом"
    }
  },
  {
    "origin_word": "das Mittagessen",
    "rus_translation": "обед",
    "support_word": {
      "Essen": "есть",
      "Mittag": "полдень",
      "Fleisch": "мясо",
      "mit dem Kartoffel": "с картошкой"
    }
  },
  {
    "origin_word": "das Abendessen",
    "rus_translation": "ужин",
    "support_word": {
      "Essen": "есть",
      "Abend": "вечер",
      "Käse": "сыр",
      "mit dem Wein": "с вином"
    }
  },
  {
    "origin_word": "das Flugzeug",
    "rus_translation": "самолет",
    "support_word": {
      "Fahrzeug": "транспорт",
      "Fliegen": "летать",
      "Flügel": "крылья",
      "mit dem Pilot": "с пилотом"
    }
  },
  {
    "origin_word": "das Auto",
    "rus_translation": "автомобиль",
    "support_word": {
      "Fahrzeug": "транспорт",
      "Fahren": "ездить",
      "Rad": "колесо",
      "mit dem Lenkrad": "с рулем"
    }
  },
  {
    "origin_word": "die Straßenbahn",
    "rus_translation": "трамвай",
    "support_word": {
      "Fahrzeug": "транспорт",
      "Fahren": "ездить",
      "Schiene": "рельс",
      "mit dem Fahrer": "с водителем"
    }
  },
  {
    "origin_word": "der Bus",
    "rus_translation": "автобус",
    "support_word": {
      "Fahrzeug": "транспорт",
      "Fahren": "ездить",
      "Passagier": "пассажир",
      "mit dem Ticket": "с билетом"
    }
  },
  {
    "origin_word": "der Zug",
    "rus_translation": "поезд",
    "support_word": {
      "Fahrzeug": "транспорт",
      "Fahren": "ездить",
      "Waggon": "вагон",
      "mit dem Schaffner": "с кондуктором"
    }
  },
  {
    "origin_word": "das Fahrrad",
    "rus_translation": "велосипед",
    "support_word": {
      "Fahrzeug": "транспорт",
      "Fahren": "ездить",
      "Pedal": "педаль",
      "mit dem Helm": "с шлемом"
    }
  },
  {
    "origin_word": "die Zeit",
    "rus_translation": "время",
    "support_word": {
      "Dauer": "продолжительность",
      "Uhr": "часы",
      "Kalender": "календарь",
      "mit dem Moment": "с моментом"
    }
  },
  {
    "origin_word": "das Jahr",
    "rus_translation": "год",
    "support_word": {
      "Zeit": "время",
      "Monat": "месяц",
      "Jahreszeit": "время года",
      "mit dem Geburtstag": "с днем рождения"
    }
  },
  {
    "origin_word": "die Woche",
    "rus_translation": "неделя",
    "support_word": {
      "Zeit": "время",
      "Tag": "день",
      "Wochentag": "день недели",
      "mit dem Wochenende": "с выходными"
    }
  },
  {
    "origin_word": "die Stunde",
    "rus_translation": "час",
    "support_word": {
      "Zeit": "время",
      "Minute": "минута",
      "Sekunde": "секунда",
      "mit dem Zeiger": "со стрелкой"
    }
  },
  {
    "origin_word": "die Minute",
    "rus_translation": "минута",
    "support_word": {
      "Zeit": "время",
      "Sekunde": "секунда",
      "Stunde": "час",
      "mit dem Zifferblatt": "с циферблатом"
    }
  },
  {
    "origin_word": "die Nudeln",
    "rus_translation": "лапша",
    "support_word": {
      "Essen": "еда",
      "Teig": "тесто",
      "Kochen": "варить",
      "mit dem Soße": "с соусом"
    }
  },
  {
    "origin_word": "das Rindfleisch",
    "rus_translation": "говядина",
    "support_word": {
      "Essen": "еда",
      "Fleisch": "мясо",
      "Kuh": "корова",
      "mit dem Steak": "с стейком"
    }
  },
  {
    "origin_word": "das Schweinefleisch",
    "rus_translation": "свинина",
    "support_word": {
      "Essen": "еда",
      "Fleisch": "мясо",
      "Schwein": "свинья",
      "mit dem Schnitzel": "с отбивной"
    }
  },
  {
    "origin_word": "das Hähnchen",
    "rus_translation": "курица (мясо)",
    "support_word": {
      "Essen": "еда",
      "Fleisch": "мясо",
      "Huhn": "курица (птица)",
      "mit dem Flügel": "с крылышком"
    }
  },
  {
    "origin_word": "das Kotelett",
    "rus_translation": "котлета",
    "support_word": {
      "Essen": "еда",
      "Fleisch": "мясо",
      "Braten": "жарить",
      "mit dem Brot": "с хлебом"
    }
  },
  {
    "origin_word": "die Zitrone",
    "rus_translation": "лимон",
    "support_word": {
      "Frucht": "фрукт",
      "Gelb": "желтый",
      "Sauer": "кислый",
      "mit dem Saft": "с соком"
    }
  },
  {
    "origin_word": "die Erbse",
    "rus_translation": "горох",
    "support_word": {
      "Gemüse": "овощ",
      "Grün": "зеленый",
      "Rund": "круглый",
      "mit dem Schote": "с стручком"
    }
  },
  {
    "origin_word": "das Brötchen",
    "rus_translation": "булочка",
    "support_word": {
      "Essen": "еда",
      "Brot": "хлеб",
      "Backen": "печь",
      "mit dem Mohn": "с маком"
    }
  },
  {
    "origin_word": "der Fisch",
    "rus_translation": "рыба",
    "support_word": {
      "Tier": "животное",
      "Wasser": "вода",
      "Schwimmen": "плавать",
      "mit dem Gräte": "с костью"
    }
  },
  {
    "origin_word": "die Pirogge",
    "rus_translation": "пирожок",
    "support_word": {
      "Essen": "еда",
      "Teig": "тесто",
      "Füllung": "начинка",
      "mit dem Fleisch": "с мясом"
    }
  },
  {
    "origin_word": "das Konfekt",
    "rus_translation": "конфета",
    "support_word": {
      "Süßigkeit": "сладость",
      "Schokolade": "шоколад",
      "Form": "форма",
      "mit dem Nougat": "с нугой"
    }
  },
  {
    "origin_word": "das Eis",
    "rus_translation": "лёд; мороженое",
    "support_word": {
      "Wasser": "вода",
      "Kälte": "холод",
      "Schmelzen": "таять",
      "mit dem Löffel": "с ложкой"
    }
  },
  {
    "origin_word": "die Nuss",
    "rus_translation": "орех",
    "support_word": {
      "Frucht": "фрукт",
      "Schale": "скорлупа",
      "Kern": "ядро",
      "mit dem Knacken": "с треском"
    }
  },
  {
    "origin_word": "das Ei",
    "rus_translation": "яйцо",
    "support_word": {
      "Essen": "еда",
      "Huhn": "курица",
      "Schale": "скорлупа",
      "mit dem Dotter": "с желтком"
    }
  },
  {
    "origin_word": "die Kartoffeln",
    "rus_translation": "картофель",
    "support_word": {
      "Knolle": "клубень",
      "Erdapfel": "земляной яблоко",
      "Beilage": "гарнир",
      "mit der Schale": "с кожурой"
    }
  },
  {
    "origin_word": "der Salat",
    "rus_translation": "салат",
    "support_word": {
      "Gemüse": "овощи",
      "Blattgemüse": "листовые овощи",
      "Beilage": "гарнир",
      "mit dem Dressing": "с заправкой"
    }
  },
  {
    "origin_word": "die Tomate",
    "rus_translation": "помидор",
    "support_word": {
      "Gemüsefrucht": "овощной плод",
      "Nachtschattengewächs": "паслёновые",
      "mit der Schale": "с кожурой",
      "rot": "красный"
    }
  },
  {
    "origin_word": "die Gurke",
    "rus_translation": "огурец",
    "support_word": {
      "Gemüse": "овощи",
      "Salatgurke": "салатный огурец",
      "mit der Schale": "с кожурой",
      "grün": "зелёный"
    }
  },
  {
    "origin_word": "der Brei",
    "rus_translation": "каша",
    "support_word": {
      "Getreidebrei": "крупяная каша",
      "Frühstück": "завтрак",
      "mit Milch": "с молоком",
      "warm": "тёплый"
    }
  },
  {
    "origin_word": "die Suppe",
    "rus_translation": "суп",
    "support_word": {
      "Eintopf": "однокастрюльное блюдо",
      "Brühe": "бульон",
      "mit Gemüse": "с овощами",
      "heiß": "горячий"
    }
  },
  {
    "origin_word": "das belegte Brötchen",
    "rus_translation": "бутерброд",
    "support_word": {
      "Stulle": "ломтевой хлеб",
      "Brotzeit": "закуска",
      "mit Schinken": "с ветчиной",
      "mit Käse": "с сыром"
    }
  },
  {
    "origin_word": "das Sodawasser",
    "rus_translation": "газировка",
    "support_word": {
      "Sprudel": "газированная вода",
      "Erfrischungsgetränk": "освежающий напиток",
      "mit Zitrone": "с лимоном",
      "kalt": "холодный"
    }
  },
  {
    "origin_word": "das Wasser",
    "rus_translation": "вода",
    "support_word": {
      "Flüssigkeit": "жидкость",
      "Lebenselixier": "жизненный эликсир",
      "kalt": "холодный",
      "klar": "чистый"
    }
  },
  {
    "origin_word": "der Kaffee",
    "rus_translation": "кофе",
    "support_word": {
      "Heißgetränk": "горячий напиток",
      "Wachmacher": "бодрящее средство",
      "mit Milch": "с молоком",
      "schwarz": "чёрный"
    }
  },
  {
    "origin_word": "der Tee",
    "rus_translation": "чай",
    "support_word": {
      "Aufgussgetränk": "настойка",
      "Heißgetränk": "горячий напиток",
      "mit Zitrone": "с лимоном",
      "aromatisch": "ароматный"
    }
  },
  {
    "origin_word": "die Milch",
    "rus_translation": "молоко",
    "support_word": {
      "Kuhmilch": "коровье молоко",
      "Getränk": "напиток",
      "frisch": "свежий",
      "weiß": "белый"
    }
  },
  {
    "origin_word": "der Apfel",
    "rus_translation": "яблоко",
    "support_word": {
      "Obst": "фрукт",
      "Gesundes": "полезное",
      "rot": "красный",
      "saftig": "сочный"
    }
  },
  {
    "origin_word": "die Trauben",
    "rus_translation": "виноград",
    "support_word": {
      "Frucht": "плод",
      "Rebe": "лоза",
      "grün": "зелёный",
      "süß": "сладкий"
    }
  },
  {
    "origin_word": "die Orange (оранже)",
    "rus_translation": "апельсин",
    "support_word": {
      "Zitrusfrucht": "цитрусовый плод",
      "Saft": "сок",
      "orange": "оранжевый",
      "sauer": "кислый"
    }
  },
  {
    "origin_word": "die Ananas",
    "rus_translation": "ананас",
    "support_word": {
      "Tropenfrucht": "тропический фрукт",
      "Konserven": "консервы",
      "gelb": "жёлтый",
      "süß": "сладкий"
    }
  },
  {
    "origin_word": "die Aprikose",
    "rus_translation": "абрикос",
    "support_word": {
      "Frucht": "плод",
      "Steinobst": "косточковый фрукт",
      "orange": "оранжевый",
      "süß": "сладкий"
    }
  },
      {
        "origin_word": "das Brot",
        "rus_translation": "хлеб",
        "support_word": {
            "Backware": "выпечка",
            "Brötchen": "булочка",
            "Knäckebrot": "хрустящий хлеб",
            "mit der Butter": "с маслом"
        }
    },
    {
        "origin_word": "die Butter",
        "rus_translation": "масло",
        "support_word": {
            "Streichfett": "растительное масло",
            "Margarine": "маргарин",
            "Schmalz": "сало",
            "mit dem Brot": "с хлебом"
        }
    },
    {
        "origin_word": "der Käse",
        "rus_translation": "сыр",
        "support_word": {
            "Hartkäse": "твердый сыр",
            "Weichkäse": "мягкий сыр",
            "Schmelzkäse": "плавленый сыр",
            "mit dem Brot": "с хлебом"
        }
    },
    {
        "origin_word": "die Wurst",
        "rus_translation": "колбаса",
        "support_word": {
            "Bratwurst": "жареная колбаса",
            "Schinken": "ветчина",
            "Salami": "салями",
            "auf dem Brot": "на хлебе"
        }
    },
    {
        "origin_word": "das Öl",
        "rus_translation": "растительное масло; нефть",
        "support_word": {
            "Olivenöl": "оливковое масло",
            "Sonnenblumenöl": "подсолнечное масло",
            "Motoröl": "моторное масло",
            "in der Pfanne": "в сковороде"
        }
    },
    {
        "origin_word": "der Pfeffer",
        "rus_translation": "горький перец",
        "support_word": {
            "Schwarzer Pfeffer": "черный перец",
            "Weißer Pfeffer": "белый перец",
            "Roter Pfeffer": "красный перец",
            "in der Gewürzmühle": "в специях"
        }
    },
    {
        "origin_word": "das Salz",
        "rus_translation": "соль",
        "support_word": {
            "Meersalz": "морская соль",
            "Tafelsalz": "столовая соль",
            "Himalayasalz": "гималайская соль",
            "auf dem Essen": "на еде"
        }
    },
    {
        "origin_word": "die Beere",
        "rus_translation": "ягода",
        "support_word": {
            "Himbeere": "малина",
            "Erdbeere": "клубника",
            "Blaubeere": "голубика",
            "in der Fruchtschale": "в фруктовой тарелке"
        }
    },
    {
        "origin_word": "der Honig",
        "rus_translation": "мёд",
        "support_word": {
            "Blütenhonig": "цветочный мед",
            "Waldhonig": "лесной мед",
            "Akazienhonig": "акациевый мед",
            "auf dem Brot": "на хлебе"
        }
    },
    {
        "origin_word": "die Marmelade",
        "rus_translation": "варенье",
        "support_word": {
            "Erdbeermarmelade": "клубничное варенье",
            "Aprikosenmarmelade": "абрикосовое варенье",
            "Himbeermarmelade": "малиновое варенье",
            "auf dem Brot": "на хлебе"
        }
    },
    {
        "origin_word": "der Pilz",
        "rus_translation": "гриб",
        "support_word": {
            "Champignon": "шампиньон",
            "Steinpilz": "белый гриб",
            "Pfifferling": "лисичка",
            "im Wald": "в лесу"
        }
    },
    {
        "origin_word": "die Zwiebel",
        "rus_translation": "лук (репчатый)",
        "support_word": {
            "Rote Zwiebel": "красный лук",
            "Weiße Zwiebel": "белый лук",
            "Schalotte": "шалот",
            "im Salat": "в салате"
        }
    },
    {
        "origin_word": "die Banane",
        "rus_translation": "банан",
        "support_word": {
            "Gelbe Banane": "желтый банан",
            "Grüne Banane": "зеленый банан",
            "Reife Banane": "спелый банан",
            "im Obstsalat": "в фруктовом салате"
        }
    },
    {
        "origin_word": "die Mohrrübe",
        "rus_translation": "морковь",
        "support_word": {
            "Orange Mohrrübe": "оранжевая морковь",
            "Weiße Mohrrübe": "белая морковь",
            "Rote Mohrrübe": "красная морковь",
            "im Gemüsegericht": "в овощном блюде"
        }
    },
    {
        "origin_word": "die Birne",
        "rus_translation": "груша",
        "support_word": {
            "Saftige Birne": "сочная груша",
            "Süße Birne": "сладкая груша",
            "Harte Birne": "жесткая груша",
            "im Obstsalat": "в фруктовом салате"
        }
    },
      {
        "origin_word": "die Zuckerrübe",
        "rus_translation": "свекла",
        "support_word": {
            "Runkelrübe": "буряк",
            "Futterrübe": "кормовая свекла",
            "Zuckerwurzel": "сахарная свекла",
            "im Gemüsebeet": "в огороде"
        }
    },
    {
        "origin_word": "das Obst",
        "rus_translation": "фрукты",
        "support_word": {
            "Apfel": "яблоко",
            "Banane": "банан",
            "Orange": "апельсин",
            "im Obstkorb": "в фруктовой корзине"
        }
    },
    {
        "origin_word": "die Melone",
        "rus_translation": "дыня",
        "support_word": {
            "Honigmelone": "мускусная дыня",
            "Wassermelone": "арбуз",
            "Cantaloupe-Melone": "канталупа",
            "in der Fruchtsalat": "в фруктовом салате"
        }
    },
    {
        "origin_word": "die Wassermelone",
        "rus_translation": "арбуз",
        "support_word": {
            "Riesig Wassermelone": "огромный арбуз",
            "Kernlos Wassermelone": "без косточек арбуз",
            "Gestreift Wassermelone": "полосатый арбуз",
            "im Picknick": "на пикнике"
        }
    },
    {
        "origin_word": "der Kuchen",
        "rus_translation": "торт; пирог",
        "support_word": {
            "Schokoladenkuchen": "шоколадный торт",
            "Obstkuchen": "фруктовый пирог",
            "Käsekuchen": "сырный пирог",
            "auf der Geburtstagsfeier": "на дне рождения"
        }
    },
    {
        "origin_word": "die Schokolade",
        "rus_translation": "шоколад",
        "support_word": {
            "Milchschokolade": "молочный шоколад",
            "Dunkle Schokolade": "темный шоколад",
            "Weiße Schokolade": "белый шоколад",
            "als Nachtisch": "как десерт"
        }
    },
    {
        "origin_word": "das Fleisch",
        "rus_translation": "мясо",
        "support_word": {
            "Rindfleisch": "говядина",
            "Schweinefleisch": "свинина",
            "Hühnerfleisch": "куриное мясо",
            "auf dem Grill": "на гриле"
        }
    },
    {
        "origin_word": "der Zucker",
        "rus_translation": "сахар",
        "support_word": {
            "Brauner Zucker": "коричневый сахар",
            "Puderzucker": "пудра",
            "Rohrzucker": "тростниковый сахар",
            "im Kaffee": "в кофе"
        }
    },
    {
        "origin_word": "der Reis",
        "rus_translation": "рис",
        "support_word": {
            "Basmati-Reis": "басмати",
            "Langkornreis": "длиннозерный рис",
            "Jasminreis": "ясминовый рис",
            "im asiatischen Gericht": "в азиатском блюде"
        }
    }]



        words_added = 0

        for word_data in words_array:
            origin_word = word_data["origin_word"]
            if not Word.objects.filter(origin_word=origin_word).exists():
                word_instance = Word(
                    origin_word=origin_word,
                    rus_translation=word_data["rus_translation"],
                    support_word=word_data["support_word"],
                )
                word_instance.save()
                words_added += 1

        print(f"{words_added} words added")
        self.stdout.write(self.style.SUCCESS('Words added successfully!'))










