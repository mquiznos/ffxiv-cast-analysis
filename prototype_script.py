from requests_html import HTML, HTMLSession

session = HTMLSession()

URL = 'https://www.fflogs.com/reports/P61L2rqMpYRQJjfW?fight=196&type=casts&view=events&ability=17870'

r = session.get(URL)
r.html.render(timeout = 40)

result = r.html.find('.main-table-number', first = True).text

times = [element.text for element in r.html.find('.main-table-number')]

print(times)
