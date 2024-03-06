from django.core.management.base import BaseCommand
from books.models import PDFPage


class Command(BaseCommand):
    help = 'Add words to the Word model'

    def handle(self, *args, **options):
        words_array = [    {
        "number": 7,
        "text": "Ein Junge \u00dcberlebt\nMr. und Mrs. Dursley im Ligusterweg Nummer 4 waren stolz\ndarauf, ganz und gar normal zu sein, sehr stolz sogar. Niemand w\u00e4re\nauf die Idee gekommen, sie k\u00f6nnten sich in eine merkw\u00fcrdige und\ngeheimnisvolle Geschichte ver stricken, denn mit solchem Unsinn\nwollten sie nichts zu tun haben.\nMr. Dursley war Direktor einer Firma namens Grun nings, die\nBohrmaschinen herstellte. Er war gro\u00df und bul lig und hatte fast\nkeinen Hals, daf\u00fcr aber einen sehr gro\u00dfen Schnurrbart. Mrs.\nDursley war d\u00fcnn und blond und besa\u00df doppelt so viel Hals, wie\nnotwendig gewesen w\u00e4re, was allerdings sehr n\u00fctzlich war, denn\nso konnte sie den Hals \u00fcber den Gartenzaun recken und zu den\nNachbarn hi n\u00fcbersp\u00e4hen. Die Dursleys hatten einen kleinen Sohn\nnamens Dudle y und in ihren Augen gab es nirgendwo einen\npr\u00e4chtigeren Jungen.\nDie Dursleys besa\u00dfen alles, was sie wollten, doch sie hat ten\nauch ein Geheimnis, und dass es Jemand aufdecken k\u00f6nnte, war\nihre gr\u00f6\u00dfte Sorge. Einfach unertr\u00e4glich w\u00e4re es, wenn die Sache\nmit den Potters herauskommen w\u00fcrde. Mrs. Potter war die\nSchwester von Mrs. Dursley; doch die beiden hatten sich schon\nseit etlichen Jahren nicht mehr gesehen. Mrs. Dursley behauptete\nsogar, dass sie gar keine Schwester h\u00e4tte, denn diese und deren\nNichtsnutz von einem Mann waren so undursleyhaft, wie man es\nsich nur denken konnte. Was w\u00fcrden blo\u00df die Nachbarn sagen,\n5"
    },
    {
        "number": 8,
        "text": "sollten die Potters eines Tages in ihrer Stra\u00dfe aufkreuzen?\nDie Dursleys wussten, dass auch die Potters einen kleinen Sohn\nhatten, doch den hatten sie nie gesehen. Auch dieser Junge war\nein guter Grund, sich von den Potters fernzu halten; mit einem\nsolchen Kind sollte ihr Dudley nicht in Ber\u00fchrung kommen.\nAls Mr. und Mrs. Dursley an dem tr\u00fcben und grauen\nDienstag, an dem unsere Geschichte beginnt, die Augen\naufschlugen, war an dem wolkenverhangenen Himmel drau\u00dfen\nkein Vorzeichen der merkw\u00fcrdigen und ge heimnisvollen Dinge\nzu erkennen, die bald \u00dcberall im Land geschehen sollten. Mr.\nDursley summte vor sich hin und suchte sich f\u00fcr die Arbeit seine\nlangweiligste Krawatte aus, und Mrs. Dursley schwatzte munter\nvor sich hin, w\u00e4h rend sie mit dem schreienden Dudley rangelte\nund ihn in seinen Hochstuhl zw\u00e4ngte.\nKeiner von ihnen sah den riesigen Waldkauz am Fenster\nvorbeifliegen.\nUm halb neun griff Mr. Dursley nach der Aktentasche, gab\nseiner Frau einen Schmatz auf die Wange und ver suchte es auch\nbei Dudley mit einem Abschiedskuss. Der ging Jedoch daneben,\nweil Dudley gerade einen Wutan fall hatte und die W\u00e4nde mit\nseinem Haferbrei bewarf \u00bbKleiner Schlingel\u00ab, gluckste Mt\nDursley, w\u00e4hrend er nach drau\u00dfen ging. Er setzte sich in den\nWagen und fuhr r\u00fcck w\u00e4rts die Einfahrt zu Nummer 4 hinaus.\nAn der Stra\u00dfenecke fiel ihm zum ersten Mal etwas Merk-\nw\u00fcrdiges auf - eine Katze, die eine Stra\u00dfenkarte studierte. Einen\nMoment war Mr. Dursley nicht klar, was er gesehen hatte -\ndann wandte er rasch den Kopf zur\u00fcck, um noch einmal\nhinzuschauen. An der Einbiegung zum Liguster weg stand eine\ngetigerte Katze, aber eine Stra\u00dfenkarte war nicht zu sehen.\nWoran er nur wieder gedacht hatte! Das\n6"
    }]



        words_added = 0

        for word_data in words_array:

            word_instance = PDFPage(
                page_number=word_data["number"],
                text_with_markup=word_data["text"]
            )
            word_instance.save()
            words_added += 1

        print(f"{words_added} words added")
        self.stdout.write(self.style.SUCCESS('Words added successfully!'))










