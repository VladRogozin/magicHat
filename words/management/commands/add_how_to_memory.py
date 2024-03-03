from g4f.client import Client
from django.core.management.base import BaseCommand
from words.models import Word
from g4f.Provider import RetryProvider, Phind, FreeChatgpt, Liaobots, OpenaiChat, Raycast, Gemini, Poe


class Command(BaseCommand):
    help = 'Populate how_to_memorize field by using usage_in_context function'

    def handle(self, *args, **options):
        try:
            words_without_how_to_memorize = Word.objects.filter(how_to_memorize='')
            for word in words_without_how_to_memorize:
                print(f"------------------------start")
                explanation = usage_in_context(word.origin_word)
                if explanation:
                    print(explanation)
                    word.how_to_memorize = explanation
                    word.save()
                    self.stdout.write(self.style.SUCCESS(f"Successfully populated how_to_memorize for word: {word.origin_word}"))
                else:
                    self.stdout.write(self.style.WARNING(f"No explanation found for word: {word.origin_word}"))
            if not words_without_how_to_memorize:
                self.stdout.write(self.style.WARNING("No words without how_to_memorize found"))
        except Exception as e:
            print(f"------------------------WRONG")
            self.stdout.write(self.style.ERROR(f"Failed to populate how_to_memorize for word. Error: {e}"))



def usage_in_context(message):
    form_message = f"Помоги мне запомнить это конкретное немецкое слово:'{message}'."
    return request_fo_g4(form_message)


def request_fo_g4(message):
    context = message
    client = Client(
        provider=RetryProvider([RetryProvider, Phind, FreeChatgpt, Liaobots, OpenaiChat, Raycast, Gemini, Poe], shuffle=False)
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": context}],
    )
    print(response.choices[0].message.content)
    return check_and_trim_result(response.choices[0].message.content)


def check_and_trim_result(result):

    # Проверка на наличие "Source:" или "Источник:" и обрезка строки результата
    source_index = result.find('Source:')
    if source_index != -1:
        result = result[:source_index]
    source_index_russian = result.find('Источник:')
    if source_index_russian != -1:
        result = result[:source_index_russian]
    return result





















