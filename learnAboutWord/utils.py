from g4f.client import Client
from g4f.Provider import RetryProvider, Phind, FreeChatgpt, Liaobots, OpenaiChat, Raycast, Gemini, Poe


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
