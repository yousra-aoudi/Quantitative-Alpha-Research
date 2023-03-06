"""
Portfolio Optimization: Use mathematical optimization techniques to find the optimal combination of assets that
maximizes returns and minimizes risk.
"""

import numpy as np
from scipy.optimize import minimize


class PortfolioOptimization:
    def __init__(self, returns, covariances, risk_aversion):
        self.returns = returns
        self.covariances = covariances
        self.risk_aversion = risk_aversion
        self.num_assets = returns.shape[0]

    def portfolio_risk(self, weights):
        portfolio_variance = np.dot(weights.T, np.dot(self.covariances, weights))
        return np.sqrt(portfolio_variance)

    def portfolio_return(self, weights):
        return np.dot(weights.T, self.returns)

    def objective_function(self, weights):
        portfolio_return = self.portfolio_return(weights)
        portfolio_risk = self.portfolio_risk(weights)
        return -(portfolio_return - self.risk_aversion * portfolio_risk)

    def optimize_portfolio(self):
        initial_weights = np.ones(self.num_assets) / self.num_assets
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = [(0, 1) for i in range(self.num_assets)]
        result = minimize(self.objective_function, initial_weights, method='SLSQP', constraints=constraints,
                          bounds=bounds)
        optimal_weights = result.x
        return optimal_weights

