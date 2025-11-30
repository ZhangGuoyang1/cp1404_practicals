import wikipedia


def main():
    """Receive page titles in a loop and display the corresponding Wikipedia page abstracts and links"""
    print("Enter page titles (blank to quit)")

    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, autosuggest=False)
            print(page.title)
            print(page.summary[:500], "...")
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()
