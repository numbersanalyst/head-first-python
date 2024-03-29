from flask import Flask, render_template, request, escape, session

from vsearch import search4letters

from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

from time import sleep

app = Flask(__name__)

app.config['dbconfig'] = {'username': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB',
                          'host': '127.0.0.1'}

app.secret_key = 'NigdyNieZgadnieszMojegoTajnegoKlucza'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Teraz jesteś zalogowany.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Teraz jesteś wylogowany.'


def log_request(req: 'flask_request', res: str) -> None:
    """Loguje szczegóły żądania sieciowego oraz wynik."""
    sleep(15)
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values (%s, %s, %s, %s, %s)"""

        user_agent = str(req.user_agent).split()
        user_agent_browser = user_agent[-1]
        # because req.user_agent.browser
        # don't work :/

        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              user_agent_browser,
                              res))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto wyniki twojego wyszukiwania:'
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logowanie się nie powiodło; wystąpił błąd:', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Witamy na stronie internetowej search4letters!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Wyświetla zawartość pliku logu w postaci tabeli HTML."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from logerror"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        # raise Exception('Jakiś nieznany wyjątek.')
        titles = ('Fraza', 'Litery', 'Adres klienta',
                  'Agent użytkownika', 'Wyniki')
        return render_template('viewlog.html',
                               the_title='Widok logu',
                               the_row_titles=titles,
                               the_data=contents)
    except ConnectionError as err:
        print('Czy twoja baza danych jest włączona? Błąd:', str(err))
    except CredentialsError as err:
        print('Problemy z identyfikatorem użytkownika lub hasłem dostępu. Błąd:', str(err))
    except SQLError as err:
        print('Czy Twoje zapytanie jest poprawne? Błąd:', str(err))
    except Exception as err:
        print('Coś poszło źle:', str(err))
    return 'Błąd'


if __name__ == '__main__':
    app.run(debug=True)
