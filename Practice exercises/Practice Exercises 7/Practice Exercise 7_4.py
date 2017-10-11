def ticker(filename):
    leesTicker = open(filename, 'r')
    inhoud = leesTicker.read()
    leesTicker.close()

    dictinhoud = inhoud.split('\n')

    tickers = {}
    for item in dictinhoud:
        items = item.split(':')
        tickers.update({items[0]:items[1]})

    return tickers

company = input('Enter a Company Name: ')
if company in ticker('ticker.txt'):
    print('Ticker symbol: {}'.format())