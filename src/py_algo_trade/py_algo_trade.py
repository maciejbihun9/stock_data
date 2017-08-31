from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed


class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(MyStrategy, self).__init__(feed)
        self.__instrument = instrument

    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())

# Load the yahoo feed from the CSV file
feed = yahoofeed.Feed()
url = '../../resources/google_s_and_p/CAT_data.csv'
feed.addBarsFromCSV("cat", url)

# Evaluate the strategy with the feed's bars.
myStrategy = MyStrategy(feed, "cat")
myStrategy.run()