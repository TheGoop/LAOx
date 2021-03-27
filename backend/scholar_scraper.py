#!/usr/bin/env python

from scraper_api import ScraperAPIClient

def query_scholar(keywords, mock=True):
        '''Search Google Scholar for keywords, returning HTML.

        For now, `keywords` must be a url-escaped string.
        If `mock` is set, don't actually search google scholar.
        '''

        if mock:
            with open('../test/fixtures/mock-scholar-page.html', 'r') as f:
                return f.read()

        with open ('api_key', 'r') as f:
            api_key = f.read().strip()

        client = ScraperAPIClient(api_key)
        query_url = ('http://scholar.google.com/scholar?'
                + '&hl=en' # in english, dammit
                + '&as_sdt=0%2C5'
                + '&btnG='
                + f'&q={keywords}') # keyword search
                # + '&as_epq=%(phrase)' # phrase search
                # + '&as_oq=%(words_some)'
                # + '&as_eq=%(words_none)'
                # + '&as_sauthors=%(authors)' # author search
                # + '&as_publication=%(pub)' # pub
                # + '&as_ylo=%(ylo)'
                # + '&as_yhi=%(yhi)'
                # + '&as_vis=%(citations)'

        return client.get(query_url).text


if __name__ == '__main__':
    print(query_scholar('tanenbaum'))