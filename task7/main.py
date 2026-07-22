import numpy as np
from logistic_regression import LogisticRegression, accuracy


def build_xor_dataset():
    """
    Build the 4D XOR truth table dataset (16 samples, 4 binary features).

    Returns:
        X (np.ndarray): shape (16, 4)
        y (np.ndarray): shape (16,)
    """
    X = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ])
    y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0])
    return X, y


def add_xor_features(X):
    """
    Engineer extra features that make 4-input XOR (parity) linearly
    separable for logistic regression.

    Important: 4-bit XOR is a DEGREE-4 interaction. In +/-1 encoding,
    XOR(a,b,c,d) is exactly the single monomial (2a-1)(2b-1)(2c-1)(2d-1).
    This means pairwise (degree-2) products alone are NOT enough --
    we need the full set of monomials: all individual features, all
    pairwise products, all triple products, and the full 4-way product.
    This gives the complete 2^4 - 1 = 15 non-constant monomial basis,
    which is guaranteed to make the data linearly separable.

    Parameters:
        X (np.ndarray): shape (n_samples, 4), original binary features

    Returns:
        np.ndarray: shape (n_samples, 15), full monomial feature set
    """
    a, b, c, d = X[:, 0], X[:, 1], X[:, 2], X[:, 3]
    features = np.stack([
        a, b, c, d,                                  # degree 1
        a * b, a * c, a * d, b * c, b * d, c * d,     # degree 2
        a * b * c, a * b * d, a * c * d, b * c * d,   # degree 3
        a * b * c * d,                                # degree 4
    ], axis=1)
    return features


def main():
    X, y = build_xor_dataset()

    print("=" * 50)
    print("Part 1: Plain Logistic Regression on raw XOR features")
    print("=" * 50)
    model_plain = LogisticRegression(iterations=5000, lr=0.1)
    model_plain.fit(X, y, verbose=True)
    y_pred_plain = model_plain.predict(X)
    acc_plain = accuracy(y, y_pred_plain)
    print(f"\nPredictions: {y_pred_plain}")
    print(f"True labels: {y}")
    print(f"Accuracy: {acc_plain * 100:.2f}%")
    print("(Expected to be poor/near chance since XOR is not linearly separable)\n")

    print("=" * 50)
    print("Part 2: Logistic Regression with engineered interaction features")
    print("=" * 50)
    X_features = add_xor_features(X)
    model_features = LogisticRegression(iterations=20000, lr=0.5)
    model_features.fit(X_features, y, verbose=True)
    y_pred_features = model_features.predict(X_features)
    acc_features = accuracy(y, y_pred_features)
    print(f"\nPredictions: {y_pred_features}")
    print(f"True labels: {y}")
    print(f"Accuracy: {acc_features * 100:.2f}%")
    print("(Should reach 100% since the added features make the data separable)")


if __name__ == "__main__":
    main()
