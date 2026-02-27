# 随机过程及其在金融领域的应用 - 学习项目

## 学习建议

根据学习经验，建议采用以下学习方法：

### 1. 动手计算例题
- **重要性**：很多概念光看文字理解不深，动手算能帮你理清逻辑
- **方法**：把书中的例题亲手算一遍，不要只看答案
- **工具**：可以使用Python/MATLAB等工具辅助计算，但核心步骤要自己完成

### 2. 先应用后推导
- **策略**：遇到抽象的定理（如中心极限定理在随机过程里的应用），可以先跳过复杂推导
- **重点**：先搞懂它在金融里的具体用法
- **后续**：等基础扎实了再回头补推导，这样不会被难住

## 项目结构

```
random/
├── README.md
├── chapter-01-financial-math-models/
│   └── chapter-01-financial-math-models.md
├── chapter-02-probability-space/
│   ├── chapter-02-probability-space.md
│   └── chapter-02-supplement-sigma-algebra-and-measurable-space.md
├── chapter-03-stochastic-processes/
│   └── chapter-03-stochastic-processes.md
├── chapter-04-poisson-process/
│   └── chapter-04-poisson-process.md
├── chapter-05-discrete-time-markov-chain/
│   └── chapter-05-discrete-time-markov-chain.md
├── chapter-06-continuous-time-markov-chain/
│   └── chapter-06-continuous-time-markov-chain.md
├── chapter-07-brownian-motion/
│   └── chapter-07-brownian-motion.md
├── chapter-08-martingale-and-applications/
│   └── chapter-08-martingale-and-applications.md
└── chapter-09-stochastic-differential-equations/
    └── chapter-09-stochastic-differential-equations.md
```

## 快速开始

1. **先看总览**：阅读本 README，了解学习方法和章节顺序
2. **按章节学习**：从 `chapter-01` 到 `chapter-09` 依次推进
3. **重点回顾**：优先掌握条件期望、Poisson 过程、Markov 链、Brown 运动、Ito 公式
4. **实践巩固**：每章补充自己的例题推导与总结

## 学习路径

### 第一阶段：基础（第1-2章）
- 第1章：金融数学模型基础
- 第2章：概率空间（重点：条件期望）

### 第二阶段：随机过程基础（第3-4章）
- 第3章：随机过程基本概念
- 第4章：Poisson过程（重点：4.1节要亲手算）

### 第三阶段：Markov链（第5-6章）
- 第5章：离散参数Markov链（重点：5.6节随机游走到Black-Scholes）
- 第6章：连续时间Markov链

### 第四阶段：Brown运动（第7章）
- 第7章：Brown运动（核心章节！重点：7.2, 7.3, 7.5节）

### 第五阶段：鞅理论（第8章）
- 第8章：鞅及其应用（先理解应用）

### 第六阶段：随机微分方程（第9章）
- 第9章：随机微分方程与Black-Scholes（全书高潮！重点：Ito公式、Black-Scholes）

## 工具推荐

- **Python**: NumPy, SciPy, Matplotlib, pandas
- **金融库**: QuantLib, yfinance
- **可视化**: Plotly, Seaborn

