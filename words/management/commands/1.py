from g4f.client import Client
from django.core.management.base import BaseCommand
from words.models import Word
from g4f.Provider import RetryProvider, Phind, FreeChatgpt, Liaobots, OpenaiChat, Raycast, Gemini, Poe


class Command(BaseCommand):
  help = 'Populate explanations field by using usage_in_context function'
  print(f"start")

  def handle(self, *args, **options):
    print(f"start")
    count_sasses = 0
    count_bat_request = 0
    words_without_explanations = Word.objects.filter(explanations__isnull=True) | Word.objects.filter(explanations='') # Получаем слова без заполненных explanations
    print(words_without_explanations)
    for word in words_without_explanations:
      print(f"start")
      try:
        explanation = usage_in_context(word.origin_word)
        count_sasses += 1
        print(explanation)
        print(f"{count_sasses} // {count_bat_request} ")
        if explanation:
          word.explanations = explanation
          word.save()
          self.stdout.write(self.style.SUCCESS(f"Successfully populated explanations for word: {word.origin_word}"))
        else:
          self.stdout.write(self.style.WARNING(f"No explanation found for word: {word.origin_word}"))
      except Exception as e:
        count_bat_request += 1
        self.stdout.write(self.style.ERROR(f"Failed to populate explanations for word: {word.origin_word}. Error: {e}"))


def usage_in_context(message):
    form_message = f"Как используется слово(с примерами): '{message}', в контексте в немецком языке. Ответ на русском"
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