
<div class="alert alert-info">

## **Time Series Forecasting**


### **Problem Statement**

* Company: **MobiPlus** (mobile manufacturing).
* Task: Forecast **future sales**.

**Agendas**:

1. Detect demand patterns → better planning (factory maintenance, staffing).
2. Accuracy requirement → **MAPE ≤ 5%**.
3. Provide **range forecasts** along with point forecasts.

---

### **Why Forecast?**

* **Under-forecasting** → shortages, lost sales, unhappy customers.
* **Over-forecasting** → overproduction, excess inventory, wasted resources.

---

### **Time Series Data**

A “signal” indexed by time (yearly, monthly, daily, hourly).

**Example dataset:**

| DATE       | Sales |
| ---------- | ----- |
| 2001-01-01 | 6519  |
| 2001-02-01 | 6654  |
| 2001-03-01 | 7332  |
| 2001-04-01 | 7332  |
| 2001-05-01 | 8240  |

---

### **Machine Learning Setup**

* **Regression** → Predict numerical future values.
* **Classification** → Predict categories (rare in forecasting).
* **Clustering** → Group similar series (used in demand segmentation).

**Forecasting setup:**

* Train: $y₁, y₂, …, yₜ$
* Predict: $y_{t+1}, y_{t+2}, …$

---

### **Dataset Overview**

* 18 years of monthly data + 1 month (2019).
* Total = **217 months**.
* Verified by: `df.date.nunique()`

---

### **EDA – Exploratory Data Analysis**

Steps:

1. Set **date index**.
2. Plot time series.
3. Identify anomalies or missing values.

**Challenges:**

* Anomalies (sudden spikes, drops).
* Missing values.

---

### **Handling Anomalies & Missing Values**

* **Detection:**

  * Percentile / IQR-based detection works.
* **Do not delete anomalies** → breaks continuity.

**Imputation methods:**

1. **Simple:** mean, median, zero.
2. **Interpolation:** straight-line between neighbors.
3. **Moving Averages (MA):** smoothen fluctuations.

---

### **Moving Average (MA)**

Smooths data by averaging over a fixed window.

**Formula:**

$$
\hat{y}_t = \frac{1}{m}\sum_{i=t-m}^{t} y_i
$$

**Example (MA(3)):**

$$
\hat{y}_t = \frac{y_{t-2} + y_{t-1} + y_t}{3}
$$

---

### **Centered Moving Average (CMA)**

Balances before and after values. Used to extract trend.

**Formula:**

$$
\hat{y}_t = \frac{1}{2m+1} \sum_{j=t-m}^{t+m} y_j
$$

**Example (window=2):**

$$
\hat{y}_t = \frac{y_{t-2}+y_{t-1}+y_t+y_{t+1}+y_{t+2}}{5}
$$

---

### **Weighted Moving Average (WMA)**

Recent points are given higher weights.

**Formula:**

$$
\hat{y}_{t+1} = \sum_{i=t-m}^t \alpha_i y_i
\quad \text{where } \sum \alpha_i = 1
$$

**Example (weights 0.5, 0.3, 0.2):**

$$
\hat{y}_{t+1} = 0.5y_t + 0.3y_{t-1} + 0.2y_{t-2}
$$

---

### **Components of Time Series**

1. **Trend (b(t))** → long-term direction.
2. **Seasonality (s(t))** → repeating cycles (e.g., winters, weekends).
3. **Residual (c(t))** → random irregular noise.

**Models:**

* Additive:

  $$
  y(t) = b(t) + s(t) + c(t)
  $$
* Multiplicative:

  $$
  y(t) = b(t) \cdot s(t) \cdot c(t)
  $$

---

### **Decomposition Process**

1. Extract **trend** using moving average.
2. Remove trend → isolate seasonality.
3. Estimate **seasonality** using group means.
4. Compute **residuals**.

---

### **Forecasting Basics**

* **Naive forecast:** last observed value.
* **Mean forecast:** average of history.
* **Moving average:** rolling mean.

---

### **Exponential Smoothing**

#### **1. Simple Exponential Smoothing (SES)**

$$
\hat{y}_{t+1} = \alpha y_t + (1-\alpha)\hat{y}_t
$$

* Small $\alpha$: smoother, close to mean.
* Large $\alpha$: reacts faster, close to naive.

---

#### **2. Double Exponential Smoothing (Holt’s method)**

$$
\begin{aligned}
\hat{y}_{t+h} &= l_t + hb_t \\
l_t &= \alpha y_t + (1-\alpha)(l_{t-1}+b_{t-1}) \\
b_t &= \beta(l_t-l_{t-1}) + (1-\beta)b_{t-1}
\end{aligned}
$$

Captures **trend**.

---

#### **3. Triple Exponential Smoothing (Holt-Winters)**

$$
\begin{aligned}
l_t &= \alpha(y_t-s_{t-m}) + (1-\alpha)(l_{t-1}+b_{t-1}) \\
b_t &= \beta(l_t-l_{t-1}) + (1-\beta)b_{t-1} \\
s_t &= \gamma(y_t-l_t) + (1-\gamma)s_{t-m} \\
\hat{y}_{t+h} &= l_t + hb_t + s_{t+h-m}
\end{aligned}
$$

Captures **trend + seasonality**.

---

### **Stationarity**

A time series is **stationary** if:

* Mean is constant.
* Variance is constant.
* No changing trend or seasonality.

**Check:** Dickey-Fuller test → if $p \leq 0.05$, series is stationary.

**Make stationary:**

* Differencing: $y'_t = y_t - y_{t-1}$
* Seasonal differencing: $y'_t = y_t - y_{t-m}$
* Decomposition to remove trend/season.

---

### **ACF & PACF**

* **ACF:** correlation between $y_t$ and past lags.
* **PACF:** correlation at lag $k$ after removing influence of shorter lags.

**Use case:** Identify AR (from PACF) and MA (from ACF) terms in ARIMA.

---

### **ARIMA Models**

* **AR (AutoRegressive):** uses past values.
* **MA (Moving Average):** uses past errors.
* **ARIMA(p,d,q):**

  * $p$: AR order
  * $d$: differencing
  * $q$: MA order

**For financial data:**

* Often stationary.
* No strong trend/seasonality.
* ARIMA captures autocorrelation in returns.

---

✅ These notes now cover:

* Problem framing
* Handling missing values & anomalies
* MA, CMA, WMA
* Decomposition (trend, seasonality, residual)
* Smoothing (SES, Holt, Holt-Winters)
* Stationarity (ADF, differencing)
* ACF/PACF
* ARIMA

</div>



https://mrmaheshrajput.medium.com/neural-networks-and-llms-for-time-series-forecasting-db604e6bbf2e

https://medium.com/@aditib259/predicting-stock-prices-using-lstms-time-series-forecasting-a-step-by-step-guide-a70ebb04bbb8

https://medium.com/data-science-collective/mastering-time-series-forecasting-with-lightgbm-a-practical-guide-2dff8d1a72bb

https://freedium.cfd/https://medium.com/code-applied/the-one-tool-you-need-to-master-time-series-forecasting-bedf0fb2264d 

https://freedium.cfd/https://ai.plainenglish.io/when-llms-meet-crypto-time-series-build-a-tsaia-style-agent-for-btc-that-actually-respects-8ef865f15b8ds
