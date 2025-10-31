from prac_06.programming_language import ProgrammingLanguage


def main():
    """Demonstrate the use of the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(visual_basic)
    print(ruby)

    languages = [python, visual_basic, ruby]
    # Display only the dynamically typed languages
    print("The dynamically typed languages are:")
    dynamic_language = [language.name for language in languages if language.is_dynamic()]
    print(dynamic_language)
    for language in dynamic_language:
        print(language)
