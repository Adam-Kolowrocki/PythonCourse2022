# Sprawdź jak wygląda kod modułu antigravity.
# Korzystając z tego samego sposobu otwarcia dowolnego url
# pozwól użytkownikowi podać adres www.
# Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:
#     https://
#     http://
#     www
#     bez www
# Może się kończyć za pomocą:
#     .pl
#     .com
#
# Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował,
# że url jest nieprawidłowy.
# Nie masz dość? Swietnie! Przepisz to zadanie za pomocą wyrażeń regularnych (RegEx)

import webbrowser

class URLError(Exception)
    """Custom Error for URL"""

def is_url(url):
    url = input('Podaj adres internetowy ->')
    prefixes = ('http://', 'https://', 'www')


suffixes = ('.pl', '.com')
if not url.startswith(prefixes)
raise URLError('Prefix incorrect')
if not url.endswith(suffixes)
    raise URLError('Suffixe incorrect')

def open_url(url_addres):
    try
        webbrowser.open(url)
    except URLError:
        print('URL incorrect')



def main():
    url = input('Podaj adres ->')
    open_url(url)




if __name__ == "__main__":
    main()
def url_check():
    correct_beginning = ['www', 'http', 'https']
    correct_endings = ['.com', '.pl']
    try:
        url(0, 2) == 'www'
    except TypeError
        print('Niepoprawny adres, ')
        url(0, 3) == 'http'
    except TypeError
        url(0, 4) == 'https'
    except TypeError
        url(-1, -4) == '.com'
    except TypeError
        url(-1, -3) == '.pl'
    except TypeError
    else:
        return url

# http , https , www
# .com / .pl
webbrowser.open(url)

def main():
    url_check()



main()