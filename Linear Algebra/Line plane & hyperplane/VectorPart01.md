### Geometric Intuition in Machine Learning: Hyperplanes & Dot Product

---

### 1. Equations of Decision Boundaries Across Dimensions

#### 1.1 Equation in 2D
**General form:**
$$
ax + by + c = 0
$$
**Represents:** A line in 2D space.
**Use in ML:** Linear separator between two classes in 2D feature space.

---

#### 1.2 Equation in 3D
**General form:**
$$
ax + by + cz + d = 0
$$
**Represents:** A plane in 3D space.
**Use in ML:** Separates space into two parts using a flat surface.

---

#### 1.3 Equation in $d$-Dimensions
**General form:**
$$
\mathbf{w}^\top \mathbf{x} + w_0 = 0
$$
**Where:**
- $\mathbf{w} \in \mathbb{R}^d$: weight (normal) vector
- $\mathbf{x} \in \mathbb{R}^d$: input vector
- $w_0 \in \mathbb{R}$: bias or intercept

**Represents:** A hyperplane in $\mathbb{R}^d$.
**Use in ML:** Decision boundary used in models like SVMs, Logistic Regression, and Perceptrons.

---

### Proof of Orthogonality to the Normal Vector

If a point $\mathbf{x}$ lies on the plane:
$$
\pi_d: \mathbf{w}^\top \mathbf{x} = 0
$$
Then the angle $\theta$ between $\mathbf{x}$ and $\mathbf{w}$ is 90°, i.e., $\cos(\theta) = 0$.

**Let:**
- $\mathbf{w}$: normal vector
- Plane passes through the origin
- $\mathbf{x}$: any point on the plane

Then:
$$
\mathbf{w}^\top \mathbf{x} = 0
$$

**Dot Product Formula:**
$$
\mathbf{w}^\top \mathbf{x} = \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos(\theta)
$$

Since both $\|\mathbf{w}\| \neq 0$ and $\|\mathbf{x}\| \neq 0$, it follows:
$$
\cos(\theta) = 0 \Rightarrow \theta = 90^\circ \Rightarrow \mathbf{w} \perp \mathbf{x}
$$

**Conclusion:**
$$
\boxed{
\mathbf{x} \in \pi_d \text{ and } \pi_d: \mathbf{w}^\top \mathbf{x} = 0 \Rightarrow \mathbf{x} \perp \mathbf{w}
}
$$
The plane $\pi_d$ contains all points $\mathbf{x}$ orthogonal to the normal vector $\mathbf{w}$.

---

### General Dot Product Interpretation

For vectors $\mathbf{a}$ and $\mathbf{b}$:
$$
\mathbf{a}^\top \mathbf{b} = \sum_{i=1}^n a_i b_i = \|\mathbf{a}\| \cdot \|\mathbf{b}\| \cdot \cos(\theta)
$$

If $\mathbf{a}^\top \mathbf{b} = 0$, then $\theta = 90^\circ \Rightarrow \mathbf{a} \perp \mathbf{b}$.

---

### 2. Understanding Hyperplanes in ML

#### 2.1 Definition of Hyperplane
A hyperplane is a flat, $(d-1)$-dimensional subspace in $\mathbb{R}^d$.
**Equation:**
$$
\Pi_d: \mathbf{w}^\top \mathbf{x} + w_0 = 0
$$

#### 2.2 Classification Interpretation
- $\mathbf{w}^\top \mathbf{x} + w_0 > 0$: Point on one side (class +1)
- $\mathbf{w}^\top \mathbf{x} + w_0 < 0$: Point on other side (class -1)
- $\mathbf{w}^\top \mathbf{x} + w_0 = 0$: Point on decision boundary

---

### 3. Geometric Meaning of the Dot Product

#### 3.1 Dot Product Formula
$$
\mathbf{w}^\top \mathbf{x} = \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta
$$
- $\|\mathbf{w}\|$: magnitude of weight vector
- $\|\mathbf{x}\|$: magnitude of input vector
- $\theta$: angle between $\mathbf{w}$ and $\mathbf{x}$

#### 3.2 Interpretations

| Angle $\theta$ | $\cos(\theta)$ | Interpretation            |
|----------------|----------------|---------------------------|
| 0°             | 1              | Same direction            |
| 90°            | 0              | Orthogonal                |
| 180°           | -1             | Opposite direction        |

---

### 4. Example: Dot Product, Angle, and Similarity

#### 4.1 Given Vectors
- $\mathbf{x}_1 = [2, 3]$
- $\mathbf{x}_2 = [3, 4]$

#### 4.2 Calculations

**Dot Product:**
$$
\mathbf{x}_1^\top \mathbf{x}_2 = 2 \cdot 3 + 3 \cdot 4 = 6 + 12 = 18
$$

**Norms:**
$$
\|\mathbf{x}_1\| = \sqrt{2^2 + 3^2} = \sqrt{13}, \quad \|\mathbf{x}_2\| = \sqrt{3^2 + 4^2} = 5
$$

**Cosine of Angle:**
$$
\cos \theta = \frac{18}{\sqrt{13} \cdot 5} \approx 0.9985
$$

**Angle:**
$$
\theta = \cos^{-1}(0.9985) \approx 3.03^\circ
$$

**Conclusion:**
Small angle implies high similarity and large dot product.

---

### 5. Margin and Distance from Hyperplane

#### 5.1 Distance from Point $\mathbf{x}$ to Hyperplane
$$
\text{Distance} = \frac{|\mathbf{w}^\top \mathbf{x} + w_0|}{\|\mathbf{w}\|}
$$
Used in SVMs to compute margin and confidence.

#### 5.2 Geometric Insight: Projection onto the Normal Vector
The dot product relates to the **projection** of a point onto the normal vector, which determines the signed distance to the hyperplane.

**Projection Interpretation:**
Given a unit normal vector $\hat{\mathbf{w}} = \frac{\mathbf{w}}{\|\mathbf{w}\|}$, the projection of $\mathbf{x}$ onto $\hat{\mathbf{w}}$ gives the signed distance from the origin along the normal:
$$
\text{proj}_{\hat{\mathbf{w}}}(\mathbf{x}) = (\hat{\mathbf{w}}^\top \mathbf{x}) \cdot \hat{\mathbf{w}}
$$

**Signed Distance to Hyperplane:**
For a hyperplane $\Pi_d: \mathbf{w}^\top \mathbf{x} + w_0 = 0$, the signed distance from point $\mathbf{x}$ to the hyperplane is:
$$
d = \frac{\mathbf{w}^\top \mathbf{x} + w_0}{\|\mathbf{w}\|}
$$
- Positive $d$: Point lies on the side of the normal vector.
- Negative $d$: Point lies opposite the normal vector.
- Zero $d$: Point lies on the hyperplane.

This projection is critical in SVMs for maximizing the margin between classes.

---

### 6. Vector Norm Clarification

#### Scalar vs. Vector
- $|x|$: scalar absolute value
- $\|\mathbf{x}\|$: vector magnitude
$$
\|\mathbf{x}\| = \sqrt{x_1^2 + x_2^2 + \dots + x_d^2}
$$

---

### 7. Special Case: Orthogonality

#### Definition:
$$
\mathbf{x}_1 \perp \mathbf{x}_2 \Leftrightarrow \mathbf{x}_1 \cdot \mathbf{x}_2 = 0
$$

#### Implications:
$$
\cos \theta = 0 \Rightarrow \theta = 90^\circ \Rightarrow \text{Uncorrelated vectors}
$$

---

### 8. Table of Concepts

| Concept                    | Meaning                                              |
|----------------------------|------------------------------------------------------|
| $\mathbf{w}^\top \mathbf{x}$ | Dot product (scalar similarity)                     |
| $\theta$                   | Angle between vectors                               |
| $\mathbf{w}^\top \mathbf{x} + w_0$ | Signed distance from hyperplane                     |
| $\cos \theta$              | Cosine similarity                                   |
| $\mathbf{w}^\top \mathbf{x} + w_0 = 0$ | Hyperplane equation                                 |
| Distance to hyperplane     | Used for margin and confidence in classification    |

---

### Plane through Origin

Given:
$$
\pi_d: \mathbf{w}^\top \mathbf{x} + w_0 = 0
$$

If the plane passes through the origin, then $w_0 = 0$. So:
$$
\pi_d: \mathbf{w}^\top \mathbf{x} = 0 \Rightarrow \mathbf{w} \perp \mathbf{x}
$$

---

### Vector Form:

$$
\mathbf{w} = 
\begin{bmatrix}
w_1 \\
w_2 \\
\vdots \\
w_d
\end{bmatrix},
\quad
\mathbf{x} = 
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_d
\end{bmatrix}
\Rightarrow 
\mathbf{w}^\top \mathbf{x} = \sum_{i=1}^d w_i x_i = 0
$$

---

### Final Conclusion:
$$
\boxed{
\mathbf{w}^\top \mathbf{x} = 0 \Rightarrow \mathbf{w} \perp \mathbf{x}
}
$$

Any point in the plane is orthogonal to the normal vector $\mathbf{w}$.

---

### Geometric Interpretation of a Plane and Distance from Origin

#### General Plane Equation:
$$
\Pi_d: \mathbf{w}^\top \mathbf{x} + w_0 = 0
$$

#### Key Properties:

1. $\mathbf{w} \perp \Pi_d$
2. If $\mathbf{0} \in \Pi_d \Rightarrow w_0 = 0$
3. Distance from origin:
$$
\text{dist}(0, \Pi_d) = \frac{|w_0|}{\|\mathbf{w}\|}
$$

---

### From Diagram (Top View):

$$
a = \|\mathbf{x}\| \cos(\theta)
\Rightarrow \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos(\theta) + w_0 = 0
\Rightarrow a = -\frac{w_0}{\|\mathbf{w}\|}
\Rightarrow \text{distance} = \left| \frac{w_0}{\|\mathbf{w}\|} \right|
$$

---

### Dot Product: Vector vs. Plane

#### 1. Core Concept
Plane is not a vector $\Rightarrow \mathbf{v} \cdot \Pi$ is invalid.

#### 2. Valid Operations
- $\mathbf{n} \cdot \mathbf{v}$: valid
- $\mathbf{n}^\top \mathbf{x} + w_0 = 0$: plane equation
- $\mathbf{n} \cdot (\mathbf{x}_1 - \mathbf{x}_2) = 0$: if both points on the plane

---

#### 3. Invalid Dot Product
| Operation                  | Valid | Reason                      |
|----------------------------|-------|-----------------------------|
| $\mathbf{v} \cdot \Pi$    | No    | Plane is not a vector       |
| $\mathbf{n} \cdot \mathbf{v}$ | Yes   | Vector is on the plane      |

---

### Vector Example from Points

Given:
- $O = (0, 0)$
- $P = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$
- $Q = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$

**Define Vectors:**
$$
\vec{OP} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad
\vec{OQ} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}
\Rightarrow \vec{PQ} = \vec{OQ} - \vec{OP} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}
$$

---

### Final Note

In ML, the hyperplane equation is:
$$
\mathbf{w}^\top \mathbf{x} + w_0 = 0
$$

If two points $\mathbf{x}_1$ and $\mathbf{x}_2$ lie on the same plane:
$$
\mathbf{w}^\top \mathbf{x}_1 + w_0 = 0 \quad \text{and} \quad \mathbf{w}^\top \mathbf{x}_2 + w_0 = 0
$$

Then the difference vector $\vec{\mathbf{x}_1\mathbf{x}_2} = \mathbf{x}_2 - \mathbf{x}_1$ is perpendicular to $\mathbf{w}$, confirming they lie on the same plane.

---
