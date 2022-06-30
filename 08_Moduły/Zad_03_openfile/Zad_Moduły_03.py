# Stwórz moduł, który zajmuje się jedynie otwieraniem plików.
# Oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw, czy dany plik istnieje
# oraz, czy jest niepusty. Funkcja zapisująca do pliku chroni
# przed nadpisaniem istniejącego pliku.
from safeopen import open_file, write_file


def main():
    content = open_file("inwokacja.txt")
    print(content)

    text_to_save = "Lalalal\n123"
    write_file('text.txt', text_to_save)


if __name__ == "__main__":
    main()
