"""
Black-Scholes期权定价模型
这是随机过程在金融中的经典应用
"""

import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Black-Scholes看涨期权定价公式
    
    参数:
        S: 当前股票价格
        K: 执行价格
        T: 到期时间（年）
        r: 无风险利率
        sigma: 波动率
    
    返回:
        call_price: 看涨期权价格
    """
    # 计算d1和d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Black-Scholes公式
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """
    Black-Scholes看跌期权定价公式
    """
    # 使用看涨-看跌平价关系
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = call_price - S + K * np.exp(-r * T)
    
    return put_price

def monte_carlo_option_pricing(S0, K, T, r, sigma, n_simulations=100000, n_steps=252):
    """
    使用蒙特卡洛方法定价期权（数值方法）
    这展示了如何通过模拟随机过程来定价
    
    参数:
        S0: 初始股票价格
        K: 执行价格
        T: 到期时间
        r: 无风险利率
        sigma: 波动率
        n_simulations: 模拟次数
        n_steps: 时间步数
    
    返回:
        call_price: 看涨期权价格
        put_price: 看跌期权价格
    """
    dt = T / n_steps
    payoffs_call = []
    payoffs_put = []
    
    for _ in range(n_simulations):
        # 模拟股票价格路径（几何布朗运动）
        S = S0
        for _ in range(n_steps):
            dW = np.random.normal(0, np.sqrt(dt))
            S = S * np.exp((r - 0.5*sigma**2)*dt + sigma*dW)
        
        # 计算期权收益
        payoff_call = max(S - K, 0)
        payoff_put = max(K - S, 0)
        
        payoffs_call.append(payoff_call)
        payoffs_put.append(payoff_put)
    
    # 折现到当前时刻
    call_price = np.exp(-r * T) * np.mean(payoffs_call)
    put_price = np.exp(-r * T) * np.mean(payoffs_put)
    
    return call_price, put_price

if __name__ == "__main__":
    # 示例参数
    S = 100      # 当前股价
    K = 105      # 执行价格
    T = 0.25     # 3个月到期
    r = 0.05     # 5%无风险利率
    sigma = 0.2  # 20%波动率
    
    # Black-Scholes公式定价
    bs_call = black_scholes_call(S, K, T, r, sigma)
    bs_put = black_scholes_put(S, K, T, r, sigma)
    
    print("=" * 50)
    print("Black-Scholes期权定价")
    print("=" * 50)
    print(f"当前股价: {S}")
    print(f"执行价格: {K}")
    print(f"到期时间: {T} 年")
    print(f"无风险利率: {r*100}%")
    print(f"波动率: {sigma*100}%")
    print("-" * 50)
    print(f"看涨期权价格 (BS公式): {bs_call:.4f}")
    print(f"看跌期权价格 (BS公式): {bs_put:.4f}")
    
    # 蒙特卡洛方法定价
    mc_call, mc_put = monte_carlo_option_pricing(S, K, T, r, sigma)
    print("-" * 50)
    print(f"看涨期权价格 (蒙特卡洛): {mc_call:.4f}")
    print(f"看跌期权价格 (蒙特卡洛): {mc_put:.4f}")
    print("=" * 50)
    
    # 比较两种方法
    print(f"\n误差分析:")
    print(f"看涨期权误差: {abs(bs_call - mc_call):.4f}")
    print(f"看跌期权误差: {abs(bs_put - mc_put):.4f}")

