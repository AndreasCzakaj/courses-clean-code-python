from typing import Callable, Optional

def print_address_line1(
        employee, 
        translation_provider: Callable[[str, str], Optional[str]], 
        language: str, 
        print_consumer: Callable[[str], None]
    ):
    position_key = employee.get_position()
    sb = [employee.get_name()]

    translation = translation_provider(language, position_key)
    if translation:
        sb.append(f" - {translation}")

    # Pass the concatenated string to the consumer
    print_consumer(''.join(sb))



class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name

# Mock translation provider
def translation_provider(language, key):
    translations = {
        "en": {"manager": "Manager", "developer": "Developer"},
        "de": {"manager": "Manager", "developer": "Entwickler"}
    }
    return translations.get(language, {}).get(key)

# Mock print consumer
def print_consumer(value):
    print(value)



def create_address_line_printer(
        translation_provider: Callable[[str, str], Optional[str]], 
        language: str, 
        print_consumer: Callable[[str], None]) -> Callable:
    def print_address_line1(employee):
        position_key = employee.get_position()
        sb = [employee.get_name()]  # Use a list for efficient string concatenation

        # Append translation if available
        translation = translation_provider(language, position_key)
        if translation:
            sb.append(f" - {translation}")

        # Pass the concatenated string to the consumer
        print_consumer(''.join(sb))

    return print_address_line1

