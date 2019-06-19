def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}", name="{name}", value2="{value2}"')


def main():
    text = input("prompt: ")
    unicode_test(text)


if __name__ == "__main__":
    main()
