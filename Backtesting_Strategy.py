"""
Backtesting: Use historical data to backtest the strategy and validate its performance. This allows for adjustments
to be made to the strategy before it is implemented in live trading.
"""


class Backtesting:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
        self.backtest_results = None

    def run_backtesting(self):
        # Implement the backtesting process
        # Initialize a list to store the results of each trade
        results = []

        # Loop through the historical data and simulate trades based on the strategy
        for i in range(1, len(self.data)):
            # Get the current data and calculate the signals based on the strategy
            current_data = self.data[i]
            signals = self.strategy.calculate_signals(current_data)

            # Based on the signals, determine if a trade should be made
            if signals == "BUY":
                # Open a long position
                pass
            elif signals == "SELL":
                # Close a long position
                pass

            # Calculate the results of the trade and add it to the results list
            trade_results = self.calculate_trade_results(signals)
            results.append(trade_results)

        # Return the results of the backtesting
        return results

    def calculate_trade_results(self, signals):
        # Calculate the results of a trade based on the signals and the data
        pass

    def run(self):
        # Initialize the strategy and portfolio
        self.strategy.initialize()
        portfolio = Portfolio(self.strategy.get_initial_capital())

        # Loop through the data and update the strategy and portfolio
        for index, row in self.data.iterrows():
            self.strategy.update(index, row)
            portfolio.update(row)

        # Save the results of the backtest
        self.backtest_results = portfolio.get_results()

    def plot_results(self):
        # Plot the results of the backtest
        pass