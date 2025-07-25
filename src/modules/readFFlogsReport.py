from requests_html import HTML, HTMLSession

class fflogsReader:
    def __init__(self, job):

        self.job = job

        if job == 'Scholar':
            self.ability_id = '17870' #cast ID for Ruin II
        else:
            print("Invalid job: Please input 'Scholar' as the first argument")
            raise ValueError

        ## add cases for Sage's E. Prog, Toxikon, and Phlegma
            


    def getSpellTimeline(self, url):
        print('Reading FFlogs report...')
        full_url = url+'&type=casts&view=events&ability='+self.ability_id

        session = HTMLSession()

        page = session.get(full_url)
        page.html.render(timeout = 40)

        times = [element.text for element in page.html.find('.main-table-number')]

        print('Done!')
        return times