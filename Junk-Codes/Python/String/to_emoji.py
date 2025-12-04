import emoji


def text_to_emoji(text):
    return emoji.emojize(text, language="alias")


test = "I love Python :snake: :thumbs_up:"
print(text_to_emoji(test))
