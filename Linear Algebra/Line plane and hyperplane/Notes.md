
# **📘Geometric Intuition in Machine Learning: Hyperplanes & Dot Product**

---

## 🔹 1. **Equations of Decision Boundaries Across Dimensions**

### 🧮 1.1 Equation in 2D
- **General form:**  
  $$
  ax + by + c = 0
  $$
- **Represents:** A line in 2D space.
- **Use in ML:** Linear separator between two classes in 2D feature space.

---

### 🧮 1.2 Equation in 3D
- **General form:**  
  $$
  ax + by + cz + d = 0
  $$
- **Represents:** A plane in 3D space.
- **Use in ML:** Separates space into two parts using a flat surface.

---

### 🧮 1.3 Equation in d-Dimensions
- **General form:**  
  $$
  w^\top x + w_0 = 0
  $$
- **Where:**
  - $ w \in \mathbb{R}^d $: weight (normal) vector
  - $ x \in \mathbb{R}^d $: input vector
  - $ w_0 \in \mathbb{R} $: bias/intercept
- **Represents:** A **hyperplane** in d-dimensional space.
- **Use in ML:** Decision boundary used in SVMs, Logistic Regression, Perceptrons, etc.

---

## 🔹 2. **Understanding Hyperplanes in ML**

### 📐 2.1 Definition of Hyperplane
- A hyperplane is a flat, (d−1)-dimensional subspace dividing $ \mathbb{R}^d $.
- **Equation:**  
  $$
  \Pi^d: w^\top x + w_0 = 0
  $$

### 📌 2.2 Classification Interpretation
- $ w^\top x + w_0 > 0 $: Point lies on one side (class +1)
- $ w^\top x + w_0 < 0 $: Point lies on the other side (class -1)
- $ w^\top x + w_0 = 0 $: Point lies exactly on the decision boundary

---

## 🔹 3. **Geometric Meaning of the Dot Product**

### 🧠 3.1 Dot Product Formula
$$
w^\top x = ||w|| \cdot ||x|| \cdot \cos\theta
$$
- **$ ||w|| $:** Magnitude (Euclidean norm) of weight vector
- **$ ||x|| $:** Magnitude of input vector
- **$ \theta $:** Angle between $ w $ and $ x $

### 📌 3.2 Interpretations
| Angle (θ)     | Cos(θ) | Meaning                        |
|---------------|--------|--------------------------------|
| 0°            | 1      | Same direction (perfectly aligned) |
| 90°           | 0      | Orthogonal (perpendicular)     |
| 180°          | -1     | Opposite direction             |

---

## 🔹 4. **Example: Dot Product, Angle, and Similarity**

### 🧮 4.1 Given Vectors
- $ x_1 = [2, 3] $
- $ x_2 = [3, 4] $

### 🔢 4.2 Calculations

#### ➤ Dot Product
$$
x_1^\top x_2 = 2 \cdot 3 + 3 \cdot 4 = 6 + 12 = \boxed{18}
$$

#### ➤ Norms (Magnitudes)
$$
||x_1|| = \sqrt{2^2 + 3^2} = \sqrt{13}
$$
$$
||x_2|| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5
$$

#### ➤ Cosine of Angle
$$
\cos \theta = \frac{18}{\sqrt{13} \cdot 5} = \frac{18}{5\sqrt{13}} \approx 0.9985
$$

#### ➤ Angle (θ)
$$
\theta = \cos^{-1}(0.9985) \approx \boxed{3.03^\circ}
$$

### ✅ Conclusion:
- Vectors $ x_1 $ and $ x_2 $ are very **closely aligned**.
- **Small angle** → **high similarity** → **high dot product**

---

## 🔹 5. **Margin and Distance from Hyperplane**

### 🧮 5.1 Distance from point $ x $ to hyperplane:
$$
\text{Distance} = \frac{|w^\top x + w_0|}{||w||}
$$

- **Used in SVM** to compute margin and confidence.
- Larger distance → higher confidence in prediction.
- Sign of $ w^\top x + w_0 $ → class label.

---

## 🔹 6. **Vector Norm Clarification**

### 🔍 Scalar vs Vector
- $ |x| $: For scalar values
- $ ||x|| $: For vectors, defined as:
  $$
  ||x|| = \sqrt{x_1^2 + x_2^2 + \dots + x_d^2}
  $$

---

## 🔹 7. **Special Case: Orthogonality**

### 🎯 Definition:
- $ x_1 \perp x_2 $ ⇔ $ x_1 \cdot x_2 = 0 $

### 🧠 Implications:
- $ \cos \theta = 0 $
- $ \theta = 90^\circ $
- Vectors are completely uncorrelated

---

## 🔹 8. **Table of Concepts**

| Concept                 | Meaning                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| $ w^\top x $           | Dot product → scalar similarity                                         |
| $ \theta $             | Angle between two vectors                                               |
| $ w^\top x + w_0 $     | Signed distance from the hyperplane (classification function)          |
| $ \cos \theta $        | Cosine similarity between vectors                                       |
| $ w^\top x + w_0 = 0 $ | Hyperplane equation (decision boundary)                                 |
| Distance to hyperplane  | Used in SVM to define **margin** and **confidence**                     |

---
