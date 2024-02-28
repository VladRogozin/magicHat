from django.core.management.base import BaseCommand
from words.models import Word


class Command(BaseCommand):
    help = 'Add words to the Word model'

    def handle(self, *args, **options):
        words_array = [
  {
    "origin_word": "die Leute",
    "rus_translation": "люди",
    "support_word": {
      "Bürger": "граждане",
      "Familien": "семьи",
      "Freunde": "друзья",
      "mit den Händen": "с руками"
    }
  },
  {
    "origin_word": "der Mensch",
    "rus_translation": "человек",
    "support_word": {
      "Person": "персона",
      "Wesen": "существо",
      "Lebewesen": "живое существо",
      "mit dem Verstand": "с разумом"
    }
  },
  {
    "origin_word": "der Mann",
    "rus_translation": "мужчина; муж",
    "support_word": {
      "Herr": "господин",
      "Ehemann": "супруг",
      "Bruder": "брат",
      "mit dem Bart": "с бородой"
    }
  },
  {
    "origin_word": "die Frau",
    "rus_translation": "женщина; жена",
    "support_word": {
      "Dame": "дама",
      "Ehefrau": "супруга",
      "Schwester": "сестра",
      "mit dem Kleid": "в платье"
    }
  },
  {
    "origin_word": "das Kind",
    "rus_translation": "ребенок",
    "support_word": {
      "Baby": "младенец",
      "Junge": "мальчик",
      "Mädchen": "девочка",
      "mit dem Spielzeug": "с игрушкой"
    }
  },
  {
    "origin_word": "der Junge",
    "rus_translation": "мальчик",
    "support_word": {
      "Knabe": "юноша",
      "Sohn": "сын",
      "Bruder": "брат",
      "mit dem Ball": "с мячом"
    }
  },
  {
    "origin_word": "das Mädchen",
    "rus_translation": "девочка",
    "support_word": {
      "Mädel": "девчонка",
      "Tochter": "дочь",
      "Schwester": "сестра",
      "mit der Puppe": "с куклой"
    }
  },
  {
    "origin_word": "der Freund",
    "rus_translation": "друг",
    "support_word": {
      "Kumpel": "приятель",
      "Partner": "партнер",
      "Gefährte": "спутник",
      "mit dem Lächeln": "с улыбкой"
    }
  },
  {
    "origin_word": "der Gast",
    "rus_translation": "гость",
    "support_word": {
      "Besucher": "посетитель",
      "Kunde": "клиент",
      "Reisender": "путешественник",
      "mit dem Koffer": "с чемоданом"
    }
  },
  {
    "origin_word": "die Familie",
    "rus_translation": "семья",
    "support_word": {
      "Verwandte": "родственники",
      "Haushalt": "домохозяйство",
      "Gruppe": "группа",
      "mit dem Stammbaum": "с родословной"
    }
  },
  {
    "origin_word": "die Eltern",
    "rus_translation": "родители",
    "support_word": {
      "Vater": "отец",
      "Mutter": "мать",
      "Erziehungsberechtigte": "опекуны",
      "mit dem Kind": "с ребенком"
    }
  },
  {
    "origin_word": "der Vater",
    "rus_translation": "отец",
    "support_word": {
      "Papa": "папа",
      "Sohn": "сын",
      "Onkel": "дядя",
      "mit dem Schnurrbart": "с усами"
    }
  },
  {
    "origin_word": "die Mutter",
    "rus_translation": "мать",
    "support_word": {
      "Mama": "мама",
      "Tochter": "дочь",
      "Tante": "тетя",
      "mit dem Schal": "с шарфом"
    }
  },
  {
    "origin_word": "der Sohn",
    "rus_translation": "сын",
    "support_word": {
      "Kind": "ребенок",
      "Bruder": "брат",
      "Neffe": "племянник",
      "mit dem Fahrrad": "на велосипеде"
    }
  },
  {
    "origin_word": "die Tochter",
    "rus_translation": "дочь",
    "support_word": {
      "Kind": "ребенок",
      "Schwester": "сестра",
      "Nichte": "племянница",
      "mit dem Buch": "с книгой"
    }
  },
  {
    "origin_word": "der Großvater",
    "rus_translation": "дед...",
    "support_word": {
      "Opa": "дедушка",
      "Vater": "отец",
      "Großonkel": "дядя",
      "mit dem Stock": "с тростью"
    }
  },
  {
    "origin_word": "der Schwiegervater",
    "rus_translation": "тесть/свекор....",
    "support_word": {
      "Vater": "отец",
      "Schwiegersohn": "зять",
      "Schwager": "шурин",
      "mit dem Hut": "с шляпой"
    }
  },
  {
    "origin_word": "der Onkel",
    "rus_translation": "дядя",
    "support_word": {
      "Bruder": "брат",
      "Vetter": "кузен",
      "Schwager": "шурин",
      "mit dem Bart": "с бородой"
    }
  },
  {
    "origin_word": "die Tante",
    "rus_translation": "тетя",
    "support_word": {
      "Schwester": "сестра",
      "Kusine": "кузина",
      "Schwägerin": "свояченица",
      "mit dem Kuchen": "с тортом"
    }
  },
  {
    "origin_word": "der Bruder",
    "rus_translation": "брат",
    "support_word": {
      "Sohn": "сын",
      "Onkel": "дядя",
      "Vetter": "кузен",
      "mit dem Hund": "с собакой"
    }
  },
  {
    "origin_word": "die Schwester",
    "rus_translation": "сестра",
    "support_word": {
      "weibliche Verwandte": "женский родственник",
      "Tochter der Eltern": "дочь родителей",
      "Schwesterherz": "сестренка",
      "mit demselben Blut": "с одной кровью"
    }
  },
  { "origin_word": "die Kusine", "rus_translation": "двоюродная сестра", "support_word": { "Tochter des Onkels": "дочь дяди", "Tochter der Tante": "дочь тети", "Verwandte zweiten Grades": "родственник второй степени", "mit demselben Großeltern": "с одними дедушкой и бабушкой" } }, { "origin_word": "die Arbeit", "rus_translation": "работа", "support_word": { "Tätigkeit": "деятельность", "Beruf": "профессия", "Lohn": "заработок", "mit dem Ziel": "с целью" } }, { "origin_word": "der Geschäftsmann", "rus_translation": "бизнесмен", "support_word": { "Unternehmer": "предприниматель", "Handel": "торговля", "Geld": "деньги", "mit dem Anzug": "в костюме" } }, { "origin_word": "der Lehrer", "rus_translation": "учитель", "support_word": { "Pädagoge": "педагог", "Schule": "школа", "Wissen": "знания", "mit den Schülern": "с учениками" } }, { "origin_word": "der Fahrer", "rus_translation": "водитель", "support_word": { "Lenker": "рулевой", "Auto": "автомобиль", "Fahrt": "поездка", "mit dem Führerschein": "с водительским удостоверением" } }, { "origin_word": "der Arbeiter", "rus_translation": "рабочий", "support_word": { "Handwerker": "ремесленник", "Fabrik": "фабрика", "Produktion": "производство", "mit den Werkzeugen": "с инструментами" } }, { "origin_word": "der Ingenieur", "rus_translation": "инженер", "support_word": { "Techniker": "техник", "Konstruktion": "конструкция", "Projekt": "проект", "mit dem Diplom": "с дипломом" } }, { "origin_word": "der Arzt", "rus_translation": "врач", "support_word": { "Mediziner": "медик", "Krankenhaus": "больница", "Gesundheit": "здоровье", "mit dem Stethoskop": "со стетоскопом" } }, { "origin_word": "die Krankenschwester", "rus_translation": "медсестра", "support_word": { "Pflegerin": "сиделка", "Arzt": "врач", "Patienten": "пациенты", "mit der Uniform": "в форме" } }, { "origin_word": "der Verkäufer", "rus_translation": "продавец", "support_word": { "Händler": "торговец", "Geschäft": "магазин", "Ware": "товар", "mit dem Lächeln": "с улыбкой" } }, { "origin_word": "der Buchhalter", "rus_translation": "бухгалтер", "support_word": { "Rechner": "калькулятор", "Firma": "фирма", "Buchführung": "бухгалтерский учет", "mit den Zahlen": "с цифрами" } }, { "origin_word": "der Maler", "rus_translation": "художник", "support_word": { "Künstler": "искусствовед", "Bild": "картина", "Farbe": "цвет", "mit dem Pinsel": "с кистью" } }, { "origin_word": "der Journalist", "rus_translation": "журналист", "support_word": { "Reporter": "репортер", "Zeitung": "газета", "Nachrichten": "новости", "mit dem Mikrofon": "с микрофоном" } }, { "origin_word": "der Kellner", "rus_translation": "официант", "support_word": { "Bedienung": "обслуживание", "Restaurant": "ресторан", "Speise": "блюдо", "mit dem Tablett": "с подносом" } }, { "origin_word": "der Musiker", "rus_translation": "музыкант", "support_word": { "Klangkünstler": "звуковой художник", "Musik": "музыка", "Instrument": "инструмент", "mit dem Talent": "с талантом" } }, { "origin_word": "der Schauspieler", "rus_translation": "актер", "support_word": { "Darsteller": "исполнитель", "Theater": "театр", "Rolle": "роль", "mit dem Applaus": "с аплодисментами" } }, { "origin_word": "der Schüler", "rus_translation": "школьник, ученик", "support_word": { "Lerner": "учащийся", "Lehrer": "учитель", "Schule": "школа", "mit dem Rucksack": "с рюкзаком" } }, { "origin_word": "der Student", "rus_translation": "студент", "support_word": { "Hochschüler": "высшеклассник", "Professor": "профессор", "Universität": "университет", "mit dem Diplom": "с дипломом" } }, { "origin_word": "das Land", "rus_translation": "страна; сельская местность", "support_word": { "Staat": "государство", "Flagge": "флаг", "Hauptstadt": "столица", "mit der Grenze": "с границей" } }, { "origin_word": "Deutschland", "rus_translation": "Германия", "support_word": { "Bundesrepublik": "федеративная республика", "Berlin": "Берлин", "Bier": "пиво", "mit dem Adler": "с орлом" } }, { "origin_word": "das Tier", "rus_translation": "животное", "support_word": { "Lebewesen": "живое существо", "Fell": "шерсть", "Pfote": "лапа", "mit dem Schwanz": "с хвостом" } }, { "origin_word": "die Katze", "rus_translation": "кошка", "support_word": { "Haustier": "домашнее животное", "Maus": "мышь", "Miau": "мяу", "mit den Schnurrhaaren": "с усами" } }, { "origin_word": "der Hund", "rus_translation": "собака", "support_word": { "Haustier": "домашнее животное", "Knochen": "кость", "Wau": "гав", "mit der Leine": "с поводком" } }, { "origin_word": "der Vogel", "rus_translation": "птица", "support_word": { "Flieger": "летун", "Flügel": "крыло", "Zwitschern": "чирикать", "mit dem Schnabel": "с клювом" } }
  , { "origin_word": "die Kuh", "rus_translation": "корова", "support_word": { "Milch": "молоко", "Gras": "трава", "Muh": "му-му", "mit den Hörnern": "с рогами" } }, { "origin_word": "das Pferd", "rus_translation": "лошадь", "support_word": { "Reiten": "езда верхом", "Hufe": "копыта", "Wiehern": "ржать", "mit dem Schweif": "с хвостом" } }, { "origin_word": "der Bär", "rus_translation": "медведь", "support_word": { "Wald": "лес", "Honig": "мёд", "Brummen": "бурчать", "mit dem Fell": "с шерстью" } }, { "origin_word": "die Maus", "rus_translation": "мышь", "support_word": { "Käse": "сыр", "Katze": "кошка", "Piepsen": "пищать", "mit den Ohren": "с ушами" } }, { "origin_word": "das Schwein", "rus_translation": "свинья", "support_word": { "Schlamm": "грязь", "Wurst": "колбаса", "Grunzen": "хрюкать", "mit dem Ringelschwanz": "с крючковатым хвостом" } }, { "origin_word": "die Stadt", "rus_translation": "город", "support_word": { "Häuser": "дома", "Menschen": "люди", "Lärm": "шум", "mit dem Rathaus": "с ратушей" } }, { "origin_word": "die Schule", "rus_translation": "школа", "support_word": { "Lehrer": "учитель", "Schüler": "ученик", "Lernen": "учиться", "mit dem Klassenzimmer": "с классной комнатой" } }, { "origin_word": "das Theater", "rus_translation": "театр", "support_word": { "Schauspieler": "актер", "Zuschauer": "зритель", "Vorstellung": "спектакль", "mit der Bühne": "со сценой" } }, { "origin_word": "die Straße", "rus_translation": "улица; дорога", "support_word": { "Auto": "автомобиль", "Ampel": "светофор", "Fahren": "ездить", "mit dem Zebrastreifen": "с пешеходным переходом" } }, { "origin_word": "der Platz", "rus_translation": "площадь; место", "support_word": { "Denkmal": "памятник", "Brunnen": "фонтан", "Treffen": "встречаться", "mit dem Baum": "с деревом" } }, { "origin_word": "das Haus", "rus_translation": "дом", "support_word": { "Wohnen": "жить", "Familie": "семья", "Dach": "крыша", "mit der Tür": "с дверью" } }, { "origin_word": "die Kirche", "rus_translation": "церковь", "support_word": { "Gott": "бог", "Gebet": "молитва", "Glocke": "колокол", "mit dem Kreuz": "с крестом" } }, { "origin_word": "der Fluss", "rus_translation": "река", "support_word": { "Wasser": "вода", "Brücke": "мост", "Fließen": "течь", "mit dem Ufer": "с берегом" } }, { "origin_word": "das Cafe", "rus_translation": "кафе", "support_word": { "Kaffee": "кофе", "Kuchen": "торт", "Plaudern": "болтать", "mit dem Tisch": "со столом" } }, { "origin_word": "das Hotel", "rus_translation": "гостиница", "support_word": { "Zimmer": "номер", "Rezeption": "рецепция", "Übernachten": "ночевать", "mit dem Bett": "с кроватью" } }, { "origin_word": "der Garten", "rus_translation": "сад", "support_word": { "Blume": "цветок", "Baum": "дерево", "Pflanzen": "сажать", "mit dem Zaun": "с забором" } }, { "origin_word": "der Park", "rus_translation": "парк", "support_word": { "Gras": "трава", "Bank": "скамейка", "Spazieren": "гулять", "mit dem Teich": "с прудом" } }, { "origin_word": "die Bank", "rus_translation": "банк", "support_word": { "Geld": "деньги", "Konto": "счет", "Zinsen": "проценты", "mit dem Schalter": "с кассой" } }, { "origin_word": "die Haltestelle", "rus_translation": "остановка", "support_word": { "Bus": "автобус", "Straßenbahn": "трамвай", "Warten": "ждать", "mit dem Fahrplan": "с расписанием" } }, { "origin_word": "das Kino", "rus_translation": "кинотеатр", "support_word": { "Film": "фильм", "Popcorn": "попкорн", "Anschauen": "смотреть", "mit dem Sitz": "с креслом" } }, { "origin_word": "die Brücke", "rus_translation": "мост", "support_word": { "Fluss": "река", "Überqueren": "переходить", "Verbinden": "соединять", "mit dem Geländer": "с перилами" } }, { "origin_word": "die Kreuzung", "rus_translation": "перекрёсток", "support_word": { "Straße": "улица", "Ampel": "светофор", "Abbiegen": "поворачивать", "mit dem Schild": "с указателем" } }, { "origin_word": "der Wald", "rus_translation": "лес", "support_word": { "Baum": "дерево", "Tier": "животное", "Wandern": "ходить по лесу", "mit dem Pilz": "с грибом" } }, { "origin_word": "das Krankenhaus", "rus_translation": "больница", "support_word": { "Arzt": "врач", "Patient": "пациент", "Heilen": "лечить", "mit dem Krankenwagen": "со скорой помощью" } }, { "origin_word": "der Markt", "rus_translation": "рынок", "support_word": { "Ware": "товар", "Verkäufer": "продавец", "Kaufen": "покупать", "mit dem Stand": "с ларьком" } }, { "origin_word": "die Polizei", "rus_translation": "полиция", "support_word": { "Gesetz": "закон", "Verbrecher": "преступник", "Festnehmen": "задерживать", "mit der Pistole": "с пистолетом" } }, { "origin_word": "die Post", "rus_translation": "почта", "support_word": { "Brief": "письмо", "Marke": "марка", "Schicken": "отправлять", "mit dem Briefkasten": "с почтовым ящиком" } }
  ,{ "origin_word": "der Bahnhof", "rus_translation": "станция, вокзал", "support_word": { "Zug": "поезд", "Gleis": "путь", "Fahrplan": "расписание", "mit dem Bahnsteig": "с платформой" } }, { "origin_word": "das Zentrum", "rus_translation": "центр", "support_word": { "Stadt": "город", "Hauptstraße": "главная улица", "Einkaufen": "шопинг", "mit dem Rathaus": "с ратушей" } }, { "origin_word": "das Geschäft", "rus_translation": "магазин", "support_word": { "Verkaufen": "продавать", "Kunden": "покупатели", "Regal": "полка", "mit der Kasse": "с кассой" } }, { "origin_word": "der Berg", "rus_translation": "гора", "support_word": { "Höhe": "высота", "Wandern": "поход", "Aussicht": "вид", "mit dem Gipfel": "с вершиной" } }, { "origin_word": "die Wohnung", "rus_translation": "квартира", "support_word": { "Mieten": "снимать", "Zimmer": "комната", "Balkon": "балкон", "mit der Tür": "с дверью" } }, { "origin_word": "die Küche", "rus_translation": "кухня", "support_word": { "Essen": "еда", "Kochen": "готовить", "Herd": "плита", "mit dem Schrank": "с шкафом" } }, { "origin_word": "der Balkon", "rus_translation": "балкон", "support_word": { "Blumen": "цветы", "Terrasse": "терраса", "Erholen": "отдыхать", "mit dem Geländer": "с перилами" } }, { "origin_word": "das Badezimmer", "rus_translation": "ванная", "support_word": { "Baden": "купаться", "Wasser": "вода", "Spiegel": "зеркало", "mit der Dusche": "с душем" } }, { "origin_word": "die Dusche", "rus_translation": "душ", "support_word": { "Duschen": "принимать душ", "Wasser": "вода", "Seife": "мыло", "mit dem Vorhang": "с занавеской" } }, { "origin_word": "die Toilette", "rus_translation": "туалет", "support_word": { "WC": "унитаз", "Papier": "бумага", "Spülen": "смывать", "mit dem Deckel": "с крышкой" } }, { "origin_word": "der Fußboden", "rus_translation": "пол", "support_word": { "Boden": "поверхность", "Teppich": "ковер", "Wischen": "мыть", "mit den Fliesen": "с плиткой" } }, { "origin_word": "die Etage", "rus_translation": "этаж", "support_word": { "Stockwerk": "уровень", "Treppe": "лестница", "Aufzug": "лифт", "mit der Nummer": "с номером" } }, { "origin_word": "der Flur", "rus_translation": "коридор", "support_word": { "Gang": "проход", "Schuh": "обувь", "Garderobe": "гардероб", "mit dem Spiegel": "с зеркалом" } }, { "origin_word": "das Schlafzimmer", "rus_translation": "спальня", "support_word": { "Schlafen": "спать", "Bett": "кровать", "Wecker": "будильник", "mit dem Schrank": "с шкафом" } }, { "origin_word": "das Wohnzimmer", "rus_translation": "зал", "support_word": { "Wohnen": "жить", "Sofa": "диван", "Fernseher": "телевизор", "mit dem Tisch": "со столом" } }, { "origin_word": "die Tür", "rus_translation": "дверь", "support_word": { "Öffnen": "открывать", "Schließen": "закрывать", "Klingel": "звонок", "mit dem Griff": "с ручкой" } }, { "origin_word": "das Fenster", "rus_translation": "окно", "support_word": { "Sehen": "смотреть", "Licht": "свет", "Vorhang": "штора", "mit dem Glas": "со стеклом" } }, { "origin_word": "der Schlüssel", "rus_translation": "ключ", "support_word": { "Schloss": "замок", "Aufschließen": "отпирать", "Anhänger": "брелок", "mit dem Bart": "с зубцами" } }, { "origin_word": "das Bett", "rus_translation": "кровать", "support_word": { "Liegen": "лежать", "Decke": "одеяло", "Kissen": "подушка", "mit dem Laken": "с простыней" } }, { "origin_word": "die Decke", "rus_translation": "одеяло; cкатерть; потолок", "support_word": { "Zudecken": "накрывать", "Stoff": "ткань", "Warm": "теплый", "mit dem Muster": "с узором" } }, { "origin_word": "das Kissen", "rus_translation": "подушка", "support_word": { "Kopf": "голова", "Schlafen": "спать", "Weich": "мягкий", "mit dem Bezug": "с наволочкой" } }, { "origin_word": "der Tisch", "rus_translation": "стол", "support_word": { "Essen": "есть", "Arbeiten": "работать", "Holz": "дерево", "mit den Beinen": "с ножками" } }, { "origin_word": "der Stuhl", "rus_translation": "стул", "support_word": { "Sitzen": "сидеть", "Lehne": "спинка", "Polster": "подушка", "mit den Armen": "с подлокотниками" } }, { "origin_word": "der Sessel", "rus_translation": "кресло", "support_word": { "Sitzen": "сидеть", "Lesen": "читать", "Bequem": "удобный", "mit der Fußstütze": "с подножкой" } }, { "origin_word": "der Kühlschrank", "rus_translation": "холодильник", "support_word": { "Kühlen": "охлаждать", "Lebensmittel": "продукты", "Tür": "дверь", "mit dem Licht": "со светом" } }, { "origin_word": "das Sofa", "rus_translation": "диван", "support_word": { "Liegen": "лежать", "Erholen": "отдыхать", "Kissen": "подушка", "mit der Decke": "с одеялом" } }, { "origin_word": "der Spiegel", "rus_translation": "зеркало", "support_word": { "Spiegeln": "отражать", "Gesicht": "лицо", "Rahmen": "рамка", "mit dem Glas": "со стеклом" } }, { "origin_word": "das Essen", "rus_translation": "еда", "support_word": { "Essen": "есть", "Hunger": "голод", "Geschmack": "вкус", "mit dem Teller": "с тарелкой" } }
]



        for word_data in words_array:
            word_instance = Word(
                origin_word=word_data["origin_word"],
                rus_translation=word_data["rus_translation"],
                support_word=word_data["support_word"],
            )
            word_instance.save()
        print(len(words_array))
        self.stdout.write(self.style.SUCCESS('Words added successfully!'))










