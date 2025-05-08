
### Geometric Intuition in Machine Learning: Hyperplanes, Dot Product, and Angle Derivations

#### 1. Hyperplane Definitions and Equations

##### 1.1 General Form of a Hyperplane
The equation of a hyperplane in $\mathbb{R}^d$ is:
$$
\mathbf{w}^\top \mathbf{x} + w_0 = 0
$$
- $\mathbf{w} \in \mathbb{R}^d$: Normal vector.
- $\mathbf{x} \in \mathbb{R}^d$: Input vector.
- $w_0 \in \mathbb{R}$: Bias term.
- **Interpretation**: Defines a $(d-1)$-dimensional hyperplane, where $\mathbf{w}^\top \mathbf{x}$ is the dot product determining the position of $\mathbf{x}$.

##### 1.2 Multiple Hyperplanes
- Parallel: $\Pi_1: \mathbf{w}^\top \mathbf{x} + w_{0_1} = 0$, $\Pi_2: \mathbf{w}^\top \mathbf{x} + w_{0_2} = 0$ (same $\mathbf{w}$).
- Intersecting: $\Pi_2: \mathbf{w}_2^\top \mathbf{x} + w_{0_2} = 0$ (different $\mathbf{w}_2$).
- **Context**: 2D lines with a red dot as a critical point (intersection or boundary).

#### 2. Dot Product and Geometric Foundation

##### 2.1 Dot Product Definition
The dot product between $\mathbf{w}$ and $\mathbf{x}$ is:
$$
\mathbf{w}^\top \mathbf{x} = \sum_{i=1}^d w_i x_i
$$
Geometrically:
$$
\mathbf{w}^\top \mathbf{x} = \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta
$$
- $\|\mathbf{w}\| = \sqrt{\sum_{i=1}^d w_i^2}$: Magnitude of $\mathbf{w}$.
- $\|\mathbf{x}\| = \sqrt{\sum_{i=1}^d x_i^2}$: Magnitude of $\mathbf{x}$.
- $\theta$: Angle between $\mathbf{w}$ and $\mathbf{x}$.
- **Insight**: The dot product encodes the projection of $\mathbf{x}$ onto $\mathbf{w}$.

#### 3. Derivation of Angle Conditions from Hyperplane Equation

##### 3.1 Starting Point
Start with the hyperplane equation:
$$
\mathbf{w}^\top \mathbf{x} + w_0 = 0
$$
Substitute the dot product formula:
$$
\|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta + w_0 = 0
$$

##### 3.2 Isolate the Cosine Term
Rearrange to solve for $\cos\theta$:
$$
\|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta = -w_0
$$
Assuming $\mathbf{w}$ and $\mathbf{x}$ are non-zero (i.e., $\|\mathbf{w}\| \neq 0$, $\|\mathbf{x}\| \neq 0$), divide by $\|\mathbf{w}\| \cdot \|\mathbf{x}\|$:
$$
\cos\theta = \frac{-w_0}{\|\mathbf{w}\| \cdot \|\mathbf{x}\|}
$$

##### 3.3 Analyze the Sign of $\cos\theta$
- The value of $\cos\theta$ depends on $-w_0$ and the magnitudes.
- $\cos\theta$ ranges from $-1$ to $1$.
- **Case 1: $w_0 > 0$**
  - $-w_0 < 0$, so $\cos\theta < 0$ if the magnitudes are positive.
  - This implies $\theta$ is in the second or third quadrant (obtuse, $\theta > 90^\circ$).
- **Case 2: $w_0 < 0$**
  - $-w_0 > 0$, so $\cos\theta > 0$ if the magnitudes are positive.
  - This implies $\theta$ is in the first or fourth quadrant (acute, $\theta < 90^\circ$).
- **Case 3: $w_0 = 0$**
  - $\cos\theta = 0$, so $\theta = 90^\circ$ (orthogonal vectors, hyperplane through origin).

##### 3.4 Specific Condition from Image
The image notes $\cos\theta < 0$, suggesting $w_0 > 0$ in the context, leading to $\theta > 90^\circ$ (e.g., $\approx 97^\circ$ as an illustrative example).
- **Reason**: When $\mathbf{w}^\top \mathbf{x}$ is negative relative to $w_0$, the angle exceeds $90^\circ$, indicating $\mathbf{x}$ lies on the opposite side of the normal’s direction.

##### 3.5 Trigonometric Identity Derivation
Consider the supplementary angle:
- If $\theta$ is the angle between $\mathbf{w}$ and $\mathbf{x}$, the angle $180^\circ - \theta$ is supplementary.
- Using the cosine identity:
  $$
  \cos(180^\circ - \theta) = -\cos\theta
  $$
- **Derivation**: Expand using the angle subtraction formula:
  $$
  \cos(180^\circ - \theta) = \cos 180^\circ \cdot \cos\theta + \sin 180^\circ \cdot \sin\theta
  $$
  - $\cos 180^\circ = -1$, $\sin 180^\circ = 0$.
  - Thus, $\cos(180^\circ - \theta) = -1 \cdot \cos\theta + 0 = -\cos\theta$.
- **Relevance**: When $\theta > 90^\circ$, $180^\circ - \theta < 90^\circ$, and the negative sign reflects the opposite direction, consistent with $\cos\theta < 0$.

#### 4. Vector Projections and Distance Derivations

##### 4.1 Projection onto Normal Vector
The projection of $\mathbf{x}$ onto the unit normal $\hat{\mathbf{w}} = \frac{\mathbf{w}}{\|\mathbf{w}\|}$ is:
$$
\text{proj}_{\hat{\mathbf{w}}}(\mathbf{x}) = (\hat{\mathbf{w}}^\top \mathbf{x}) \cdot \hat{\mathbf{w}}
$$
Since $\hat{\mathbf{w}}^\top \mathbf{x} = \frac{\mathbf{w}^\top \mathbf{x}}{\|\mathbf{w}\|}$:
$$
\text{proj}_{\hat{\mathbf{w}}}(\mathbf{x}) = \frac{\mathbf{w}^\top \mathbf{x}}{\|\mathbf{w}\|^2} \cdot \mathbf{w}
$$
Using $\mathbf{w}^\top \mathbf{x} = \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta$:
$$
\text{proj}_{\hat{\mathbf{w}}}(\mathbf{x}) = \|\mathbf{x}\| \cdot \cos\theta \cdot \hat{\mathbf{w}}
$$

##### 4.2 Signed Distance to Hyperplane
The signed distance from $\mathbf{x}$ to $\mathbf{w}^\top \mathbf{x} + w_0 = 0$ is:
$$
\text{distance} = \frac{\mathbf{w}^\top \mathbf{x} + w_0}{\|\mathbf{w}\|}
$$
Substitute $\mathbf{w}^\top \mathbf{x} = \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta$:
$$
\text{distance} = \frac{\|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta + w_0}{\|\mathbf{w}\|}
$$
- Positive/negative sign depends on the side relative to $\mathbf{w}$.

##### 4.3 Distance Between Parallel Hyperplanes
For $\Pi_1: \mathbf{w}^\top \mathbf{x} + w_{0_1} = 0$ and $\Pi_2: \mathbf{w}^\top \mathbf{x} + w_{0_2} = 0$:
- Point $\mathbf{x}_1$ on $\Pi_1$: $\mathbf{w}^\top \mathbf{x}_1 + w_{0_1} = 0 \Rightarrow \mathbf{w}^\top \mathbf{x}_1 = -w_{0_1}$.
- Point $\mathbf{x}_2$ on $\Pi_2$: $\mathbf{w}^\top \mathbf{x}_2 + w_{0_2} = 0 \Rightarrow \mathbf{w}^\top \mathbf{x}_2 = -w_{0_2}$.
- Difference vector $\mathbf{x}_2 - \mathbf{x}_1$ projected onto $\hat{\mathbf{w}}$:
  $$
  (\mathbf{x}_2 - \mathbf{x}_1)^\top \hat{\mathbf{w}} = \frac{\mathbf{w}^\top (\mathbf{x}_2 - \mathbf{x}_1)}{\|\mathbf{w}\|} = \frac{(-w_{0_2}) - (-w_{0_1})}{\|\mathbf{w}\|} = \frac{w_{0_1} - w_{0_2}}{\|\mathbf{w}\|}
  $$
- Distance $d = \left| \frac{w_{0_1} - w_{0_2}}{\|\mathbf{w}\|} \right| = \frac{|w_{0_2} - w_{0_1}|}{\|\mathbf{w}\|}$.

##### 4.4 Opposite Normals
If $\mathbf{w}_2 = -\mathbf{w}_1$:
- $\Pi_1: \mathbf{w}_1^\top \mathbf{x} + w_{0_1} = 0$
- $\Pi_2: -\mathbf{w}_1^\top \mathbf{x} + w_{0_2} = 0$
- Distance: $d = \frac{|w_{0_2} - w_{0_1}|}{\|\mathbf{w}_1\|}$, but the sign convention reverses.

##### 4.5 Intersection Derivation
Solve:
$$
\mathbf{w}_1^\top \mathbf{x} + w_{0_1} = 0
$$
$$
\mathbf{w}_2^\top \mathbf{x} + w_{0_2} = 0
$$
- In 2D (e.g., $\mathbf{w}_1 = [a, b]$, $\mathbf{w}_2 = [c, d]$), form a system:
  $$
  a x + b y = -w_{0_1}
  $$
  $$
  c x + d y = -w_{0_2}
  $$
- Solution via determinants or substitution yields $\mathbf{x}$ (e.g., $(-0.5, 1.5)$ for given example).

#### 5. Geometric Visualization

##### 5.1 Diagram Elements
- $\Pi_1$ (right slope), $\Pi_2$ (left slope), red dot (intersection).
- $\mathbf{w}$ (red), $\mathbf{x}_1$, $\mathbf{x}_2$ (blue), $\theta$ marked.
- "-ve ~ the" suggests negative vector or sign.

##### 5.2 Observations
- Parallel: Perpendicular $\mathbf{w}$, distance $d$.
- Intersection: Red dot as boundary.
- $\theta = 0^\circ$ to $180^\circ$ with yellow curve for angle variation.

#### 6. Negative Vector Relationship

##### 6.1 Interpretation
- "-ve ~ the" implies $\mathbf{w}_2 = -\mathbf{w}_1$ or negative distance.
- **Effect**: Opposite normals invert classification sides.

##### 6.2 Signed Distance
$$
\text{distance} = \frac{\mathbf{w}^\top \mathbf{x} + w_0}{\|\mathbf{w}\|}
$$
- Negative when $\mathbf{x}$ is on the opposite side.

#### 7. Example Applications with Steps

##### 7.1 Hyperplane Distance
- $\mathbf{w} = [1, 0]$, $\Pi_1: x + 2 = 0$ ($w_{0_1} = 2$), $\Pi_2: x + 5 = 0$ ($w_{0_2} = 5$).
- $d = \frac{|5 - 2|}{\sqrt{1^2}} = 3$.

##### 7.2 Intersection
- $\Pi_1: x + y - 1 = 0$, $\Pi_2: -x + y - 2 = 0$.
- $x + y = 1$, $-x + y = 2$.
- $2y = 3 \Rightarrow y = 1.5$, $x = -0.5$.
- Point: $(-0.5, 1.5)$, "-ve" for opposite $x$-component.

##### 7.3 Angle and Projection
- $\mathbf{w} = [1, 0]$, $\mathbf{x} = [1, 1]$, $w_0 = -1$, $\theta = 97^\circ$, $\cos(97^\circ) \approx -0.122$.
- $\mathbf{w}^\top \mathbf{x} = 1$.
- Distance: $\frac{1 + (-1)}{1} = 0$ (on plane), adjusts off-plane.

#### 8. Summary of Key Concepts

| Concept                    | Description                                      |
|----------------------------|--------------------------------------------------|
| $\mathbf{w}^\top \mathbf{x} + w_0 = 0$ | Hyperplane equation                             |
| $\mathbf{w}^\top \mathbf{x} = \|\mathbf{w}\| \cdot \|\mathbf{x}\| \cdot \cos\theta$ | Dot product                                    |
| $\cos\theta = \frac{-w_0}{\|\mathbf{w}\| \cdot \|\mathbf{x}\|}$ | Angle condition                                |
| $\cos(180^\circ - \theta) = -\cos\theta$ | Supplementary angle                            |
| $d = \frac{|w_{0_2} - w_{0_1}|}{\|\mathbf{w}\|}$ | Parallel distance                             |
| $\mathbf{w}_2 = -\mathbf{w}_1$ | Opposite normals                              |
| Intersection              | $\mathbf{x}$ from system of equations          |
| Signed distance           | $\frac{\mathbf{w}^\top \mathbf{x} + w_0}{\|\mathbf{w}\|}$ |

---



Let:
- $ \pi_1, \pi_2 $ be planes in 3D.
- $ w_1 \perp \pi_2 $ means $ w_1 $ is perpendicular (normal) to $ \pi_2 $.
- $ w_2 \perp \pi_1 $ means $ w_2 $ is perpendicular to $ \pi_1 $.
- A line $ x \parallel \pi_2 $ lies along plane $ \pi_2 $.


- A **vector perpendicular to a plane** is called its **normal vector**.
- If $ w \perp \pi_2 $ and $ w \parallel \pi_1 $, then:
  - $ w $ lies in $ \pi_1 $
  - $ w $ is orthogonal to $ \pi_2 $

---

## 📏 Section 2: Unit Vectors

Let $ \vec{w} $ be a vector with magnitude $ \| \vec{w} \| = 10 $.  
Then the **unit vector** in the direction of $ \vec{w} $ is:

$$
\hat{w} = \frac{\vec{w}}{\| \vec{w} \|}
$$

**Properties:**
- Direction: same as $ \vec{w} $
- Magnitude: $ \| \hat{w} \| = 1 $

---

### 🔹 Generalizing to $ d $-dimensions

Let:

$$
\vec{w} = 
\begin{bmatrix}
w_1 \\
w_2 \\
\vdots \\
w_d
\end{bmatrix}, \quad 
\| \vec{w} \| = l = \sqrt{w_1^2 + w_2^2 + \cdots + w_d^2}
$$

Then:

$$
\hat{w} = \frac{\vec{w}}{\| \vec{w} \|} = 
\begin{bmatrix}
\frac{w_1}{l} \\
\frac{w_2}{l} \\
\vdots \\
\frac{w_d}{l}
\end{bmatrix}
$$

To verify:

$$
\| \hat{w} \| = \sqrt{ \sum_{i=1}^d \left( \frac{w_i}{l} \right)^2 } = \sqrt{ \frac{l^2}{l^2} } = \sqrt{1} = 1
$$

---

## 🎯 Section 3: Vector Projection

Let vectors $ x_1, x_2 \in \mathbb{R}^d $, and $ \theta $ be the angle between them.

### 🔹 Unit Vector Form

$$
\hat{x}_2 = \frac{x_2}{\|x_2\|}
$$

### 🔹 Projection of $ x_1 $ onto $ x_2 $

$$
\text{Proj}_{x_2}(x_1) = x_1' = \|x_1\| \cos \theta \cdot \hat{x}_2
$$

✅ Same direction as $ x_2 $  
✅ Length is $ \|x_1\| \cos \theta $

### 🔹 Alternate form using dot product

$$
\text{Length of projection} = \|x_1\| \cos \theta = x_1 \cdot \frac{x_2}{\|x_2\|}
$$

$$
\cos \theta = \frac{x_1 \cdot x_2}{\|x_1\| \|x_2\|}, \quad \Rightarrow \quad \theta = \cos^{-1}(\hat{x}_1 \cdot \hat{x}_2)
$$

---

## 📐 Section 4: Vector Addition & Subtraction

### 🔹 Geometric Interpretation

Let:
- $ O = (0, 0) $, $ P = (2, 1) $, $ Q = (3, 4) $

Then:

$$
\vec{OQ} = \vec{OP} + \vec{PQ}
$$

$$
\vec{PQ} = \vec{OQ} - \vec{OP} = 
\begin{bmatrix}
3 \\
4
\end{bmatrix}
-
\begin{bmatrix}
2 \\
1
\end{bmatrix}
=
\begin{bmatrix}
1 \\
3
\end{bmatrix}
$$

---

### 🔹 Vector Subtraction in $ \mathbb{R}^d $

Let:

$$
x_1 =
\begin{bmatrix}
x_{11} \\
x_{21} \\
\vdots \\
x_{d1}
\end{bmatrix}, \quad
x_2 =
\begin{bmatrix}
x_{12} \\
x_{22} \\
\vdots \\
x_{d2}
\end{bmatrix}
$$

Then:

$$
x_1 - x_2 =
\begin{bmatrix}
x_{11} - x_{12} \\
x_{21} - x_{22} \\
\vdots \\
x_{d1} - x_{d2}
\end{bmatrix}
$$

✅ **Addition and subtraction are component-wise**

---

## 🚫 Section 5: Dimensional Mismatch

Let:

- $ x_1 \in \mathbb{R}^d $
- $ x_2 \in \mathbb{R}^k $ where $ d \ne k $

Then:

$$
x_1 + x_2 \text{ is not defined.}
$$

Vectors must be in the **same dimension** to be added or subtracted.

---

## 🧠 Section 6: Dot Product and Cosine Similarity

Let $ \hat{x}_1, \hat{x}_2 $ be unit vectors.

### 🔹 Dot Product and Angle

$$
\hat{x}_1 \cdot \hat{x}_2 = \cos \theta \quad \Rightarrow \quad \theta = \cos^{-1}(\hat{x}_1 \cdot \hat{x}_2)
$$

### 🔹 Non-Unit Vectors

$$
\cos \theta = \frac{x_1 \cdot x_2}{\|x_1\| \|x_2\|}
$$

### 🔹 Projection Length Again

$$
\text{Length of projection of } x_1 \text{ on } x_2 = \|x_1\| \cos \theta = x_1 \cdot \hat{x}_2
$$

---
