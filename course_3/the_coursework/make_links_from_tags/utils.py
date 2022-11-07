def wrap_to_link(tag):
    """
    Оборачивает тег в ссылку
    """
    return f"<a href='/tag/{tag}'>#{tag}</a>"

def get_tags(content):
    """
    Превращает текст с хештегами в текст со ссылками
    :param content: текст
    :return: текст со ссылками
    """
    words = []

    for word in content.split(" "):
        if word[0] == "#":
            words.append(wrap_to_link(word[1:]))
        else:
            words.append(word)

    return " ".join(words)

