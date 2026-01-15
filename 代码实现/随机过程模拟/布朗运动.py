"""
布朗运动（Brownian Motion）模拟
用于理解随机过程的基本概念
"""

import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(T=1, n=1000, mu=0, sigma=1):
    """
    模拟标准布朗运动
    
    参数:
        T: 时间长度
        n: 时间步数
        mu: 漂移系数（默认0）
        sigma: 波动率（默认1）
    
    返回:
        t: 时间数组
        W: 布朗运动路径
    """
    dt = T / n
    t = np.linspace(0, T, n+1)
    
    # 生成随机增量（正态分布）
    dW = np.random.normal(0, np.sqrt(dt), n)
    
    # 累积求和得到布朗运动路径
    W = np.zeros(n+1)
    W[1:] = np.cumsum(dW)
    
    return t, W

def geometric_brownian_motion(S0=100, T=1, n=1000, mu=0.05, sigma=0.2):
    """
    几何布朗运动（GBM）- 常用于股票价格建模
    
    参数:
        S0: 初始价格
        T: 时间长度
        n: 时间步数
        mu: 期望收益率
        sigma: 波动率
    
    返回:
        t: 时间数组
        S: 价格路径
    """
    dt = T / n
    t = np.linspace(0, T, n+1)
    
    # 生成布朗运动增量
    dW = np.random.normal(0, np.sqrt(dt), n)
    
    # 几何布朗运动：dS = mu*S*dt + sigma*S*dW
    S = np.zeros(n+1)
    S[0] = S0
    
    for i in range(n):
        S[i+1] = S[i] * np.exp((mu - 0.5*sigma**2)*dt + sigma*dW[i])
    
    return t, S

if __name__ == "__main__":
    # 示例1：标准布朗运动
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    for _ in range(5):
        t, W = brownian_motion(T=1, n=1000)
        plt.plot(t, W, alpha=0.7)
    plt.title('标准布朗运动（5条路径）')
    plt.xlabel('时间 t')
    plt.ylabel('W(t)')
    plt.grid(True, alpha=0.3)
    
    # 示例2：几何布朗运动（股票价格）
    plt.subplot(1, 2, 2)
    for _ in range(5):
        t, S = geometric_brownian_motion(S0=100, T=1, n=1000, mu=0.1, sigma=0.3)
        plt.plot(t, S, alpha=0.7)
    plt.title('几何布朗运动（股票价格模拟）')
    plt.xlabel('时间 t')
    plt.ylabel('价格 S(t)')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('brownian_motion_example.png', dpi=150)
    print("图像已保存为 brownian_motion_example.png")
    plt.show()

