# Rover Frame Transformation — Forward Kinematics

> Transforming camera-frame object coordinates into world-frame coordinates using rigid body transformation chains.

---

## Problem Statement

A planetary rover equipped with an onboard camera detects objects in its camera frame, relative to the camera lens. The goal is to determine the world frame coordinates of a detected object, given the camera mount details and the rover pose in the world.

The transformation follows a two-step rigid body chain:

$$\text{Camera Frame} \xrightarrow{T_{\text{rover}}^{\text{cam}}} \text{Rover Frame} \xrightarrow{T_{\text{world}}^{\text{rover}}} \text{World Frame}$$

---

## Inputs and Output

**Inputs**

| Parameter | Description |
|---|---|
| `(x_cam, y_cam, z_cam)` | Object coordinates in camera frame |
| `(x, y, z)` | Rover position in world frame |
| `(x_angle, y_angle, z_angle)` | Rover rotation angles in degrees |

**Output**

| Parameter | Description |
|---|---|
| `(x_world, y_world, z_world)` | Object coordinates in world frame |

---

## Method

This is a **forward kinematics** problem — configuration is known, find where the object ends up in world frame. Not inverse kinematics, which solves backwards from a desired world position.

**Some linear algebra related stuff:**
### Transformation Matrix

Rigid body motion is affine, not linear. To express rotation and translation as a single matrix multiplication, coordinates are embedded into 4D homogeneous form by appending 1:

$$\mathbf{p}_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$

This encodes both rotation $R$ and translation $\mathbf{t}$ into one $4 \times 4$ matrix:

$$T = \begin{bmatrix} R & \mathbf{t} \\ \mathbf{0}^T & 1 \end{bmatrix} \in SE(3)$$

---

## Equations

### Rotation Matrices (Fixed Axis / Extrinsic — ZYX Convention)

$$R_x(\alpha) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\alpha & -\sin\alpha \\ 0 & \sin\alpha & \cos\alpha \end{bmatrix}$$

$$R_y(\beta) = \begin{bmatrix} \cos\beta & 0 & \sin\beta \\ 0 & 1 & 0 \\ -\sin\beta & 0 & \cos\beta \end{bmatrix}$$

$$R_z(\gamma) = \begin{bmatrix} \cos\gamma & -\sin\gamma & 0 \\ \sin\gamma & \cos\gamma & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

Combined:

$$R_{\text{rover}} = R_z(\gamma) \cdot R_y(\beta) \cdot R_x(\alpha)$$

### Transform Matrices

Camera to rover frame:

$$T_{\text{rover}}^{\text{cam}} = \begin{bmatrix} R_{\text{mount}} & \mathbf{t}_{\text{mount}} \\ \mathbf{0}^T & 1 \end{bmatrix}$$

Rover to world frame:

$$T_{\text{world}}^{\text{rover}} = \begin{bmatrix} R_{\text{rover}} & \mathbf{t}_{\text{rover}} \\ \mathbf{0}^T & 1 \end{bmatrix}$$

### Chain Formula

$$\mathbf{p}_{\text{world}} = T_{\text{world}}^{\text{rover}} \cdot T_{\text{rover}}^{\text{cam}} \cdot \mathbf{p}_{\text{cam}}$$

Expanded:

$$\mathbf{p}_{\text{rover}} = R_{\text{mount}} \cdot \mathbf{p}_{\text{cam}} + \mathbf{t}_{\text{mount}}$$

$$\boxed{\mathbf{p}_{\text{world}} = R_{\text{rover}} \cdot \mathbf{p}_{\text{rover}} + \mathbf{t}_{\text{rover}}}$$

## Sketches

![Frame Chain Diagram](sketch_frame_chain.jpg)

![Vector Decomposition](sketch_vectors.jpg)

---
## Key Takeaways

*Here are a few things that I learnt from this project, listed out:*

### Forward Kinematics
- Forward kinematics solves **known configuration to find end position**,

### Linear algebra in transformaton:
- Homogeneous coordinates embed affine transforms into linear matrix multiplication
  by appending 1 to the coordinate vector
- Forward direction: $R \cdot p + t$
- Inverse direction: $R^T \cdot (p - t)$

### Learnt about Rotation Matrices
- Rotation matrices are **orthogonal** — columns are unit vectors, mutually perpendicular
- This gives the property $R^T = R^{-1}$, making inversion just a transpose
- Extrinsic (fixed axis) and intrinsic (Euler) rotations produce different results
  for the same angles — convention must be consistent throughout
- Here we use extrinsic matrix.

### NumPy
- `np.array` stores vectors and matrices efficiently as contiguous memory blocks
- `@` operator performs matrix multiplication — cleaner than `np.dot` for chaining
- `np.radians()` converts degrees cleanly without manual multiplication by $\pi/180$
- Rotation matrices can be composed with `@` directly: `Rz @ Ry @ Rx`
- Transpose is simply `.T` — no copy, just a view of the same memory
- Always verify rotation matrix validity: `np.allclose(R @ R.T, np.eye(3))` should be True

## Resources:
- Youtube - Rotation matirces, Linear Transformations (3blue 1 brown)
- Google
