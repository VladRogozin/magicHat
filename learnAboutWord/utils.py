import g4f


def request_fo_g4(message):

    context = f"Что ты можешь рассказать про это слово: '{message}'.Ответ на русском"
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": context}],
        stream=True,
    )

    answer = ''
    for message in response:
        answer += message

    print(answer)
    return check_and_trim_result(answer)


def check_and_trim_result(result):

    # Проверка на наличие "Source:" или "Источник:" и обрезка строки результата
    source_index = result.find('Source:')
    if source_index != -1:
        result = result[:source_index]
    source_index_russian = result.find('Источник:')
    if source_index_russian != -1:
        result = result[:source_index_russian]
    return result
