import numpy as np


def initialize_weights(n_features, seed=42):
    """
    Initialize weights with small random values and bias to zero.

    Note: zero-initialization is usually fine for logistic regression,
    but it fails on perfectly symmetric datasets (e.g. balanced XOR-type
    data). With weights=0, the initial predictions are all 0.5, and by
    symmetry the gradient can sum to exactly zero -- gradient descent
    gets stuck on a saddle point and never learns. Small random values
    break that symmetry so training can proceed normally.

    Parameters:
        n_features (int): number of input features
        seed (int): random seed for reproducibility

    Returns:
        weights (np.ndarray): shape (n_features,), small random values
        bias (float): initialized to 0
    """
    rng = np.random.RandomState(seed)
    weights = rng.normal(loc=0.0, scale=0.01, size=n_features)
    bias = 0.0
    return weights, bias


def sigmoid(z):
    """
    Compute the sigmoid activation function, numerically stable.

    sigma(z) = 1 / (1 + e^(-z))

    Parameters:
        z (np.ndarray or float): linear combination (X.w + b)

    Returns:
        np.ndarray or float: sigmoid(z), values in (0, 1)
    """
    # Clip z to avoid overflow in np.exp for very large negative/positive values
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))


def forward(X, weights, bias):
    """
    Compute the linear combination and pass it through sigmoid
    to get predicted probabilities.

    Parameters:
        X (np.ndarray): shape (n_samples, n_features)
        weights (np.ndarray): shape (n_features,)
        bias (float)

    Returns:
        np.ndarray: predicted probabilities, shape (n_samples,)
    """
    z = np.dot(X, weights) + bias
    return sigmoid(z)


def compute_cost(y_true, y_pred):
    """
    Compute binary cross-entropy (log-loss) cost.

    Cost = -(1/m) * sum( y*log(y_hat) + (1-y)*log(1-y_hat) )

    Parameters:
        y_true (np.ndarray): true labels, shape (n_samples,)
        y_pred (np.ndarray): predicted probabilities, shape (n_samples,)

    Returns:
        float: average cost over all samples
    """
    m = len(y_true)
    epsilon = 1e-15  # avoid log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    cost = -(1 / m) * np.sum(
        y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
    )
    return cost


def compute_gradients(X, y_true, y_pred):
    """
    Compute gradients of the cost function with respect to
    weights and bias.

    dW = (1/m) * X^T . (y_pred - y_true)
    db = (1/m) * sum(y_pred - y_true)

    Parameters:
        X (np.ndarray): shape (n_samples, n_features)
        y_true (np.ndarray): shape (n_samples,)
        y_pred (np.ndarray): shape (n_samples,)

    Returns:
        dw (np.ndarray): gradient w.r.t weights, shape (n_features,)
        db (float): gradient w.r.t bias
    """
    m = X.shape[0]
    error = y_pred - y_true
    dw = (1 / m) * np.dot(X.T, error)
    db = (1 / m) * np.sum(error)
    return dw, db


def train(X, y, iterations=1000, lr=0.1, verbose=False, verbose_step=100):
    """
    Train logistic regression using batch gradient descent.

    Parameters:
        X (np.ndarray): training features, shape (n_samples, n_features)
        y (np.ndarray): training labels, shape (n_samples,)
        iterations (int): number of gradient descent steps
        lr (float): learning rate
        verbose (bool): if True, print cost periodically
        verbose_step (int): how often (in iterations) to print cost

    Returns:
        weights (np.ndarray): learned weights, shape (n_features,)
        bias (float): learned bias
        cost_history (list): cost value recorded at each iteration
    """
    n_features = X.shape[1]
    weights, bias = initialize_weights(n_features)
    cost_history = []

    for i in range(iterations):
        y_pred = forward(X, weights, bias)
        cost = compute_cost(y, y_pred)
        cost_history.append(cost)

        dw, db = compute_gradients(X, y, y_pred)

        weights -= lr * dw
        bias -= lr * db

        if verbose and (i % verbose_step == 0 or i == iterations - 1):
            print(f"Iteration {i}: cost = {cost:.6f}")

    return weights, bias, cost_history


def predict_proba(X, weights, bias):
    """
    Predict probabilities for input samples.

    Parameters:
        X (np.ndarray): shape (n_samples, n_features)
        weights (np.ndarray): shape (n_features,)
        bias (float)

    Returns:
        np.ndarray: predicted probabilities, shape (n_samples,)
    """
    return forward(X, weights, bias)


def predict(X, weights, bias, threshold=0.5):
    """
    Predict binary class labels for input samples.

    Parameters:
        X (np.ndarray): shape (n_samples, n_features)
        weights (np.ndarray): shape (n_features,)
        bias (float)
        threshold (float): decision boundary for class 1

    Returns:
        np.ndarray: predicted class labels (0 or 1), shape (n_samples,)
    """
    probabilities = predict_proba(X, weights, bias)
    return (probabilities >= threshold).astype(int)


def accuracy(y_true, y_pred):
    """
    Compute classification accuracy.

    Parameters:
        y_true (np.ndarray): true labels, shape (n_samples,)
        y_pred (np.ndarray): predicted labels, shape (n_samples,)

    Returns:
        float: accuracy as a fraction between 0 and 1
    """
    return np.mean(y_true == y_pred)


class LogisticRegression:
    """
    Reusable Logistic Regression classifier.

    Wraps the functional building blocks above into a familiar
    fit/predict style class, matching the required project structure.
    """

    def __init__(self, iterations=1000, lr=0.1):
        """
        Parameters:
            iterations (int): number of gradient descent steps
            lr (float): learning rate
        """
        self.iterations = iterations
        self.lr = lr
        self.weights = None
        self.bias = None
        self.cost_history = None

    def fit(self, x_train, y_train, verbose=False):
        """
        Train the model on the given data.

        Parameters:
            x_train (np.ndarray): shape (n_samples, n_features)
            y_train (np.ndarray): shape (n_samples,)
            verbose (bool): if True, print cost during training
        """
        self.weights, self.bias, self.cost_history = train(
            x_train, y_train,
            iterations=self.iterations,
            lr=self.lr,
            verbose=verbose,
        )

    def predict(self, x_test, threshold=0.5):
        """
        Predict class labels for new data.

        Parameters:
            x_test (np.ndarray): shape (n_samples, n_features)
            threshold (float): decision threshold

        Returns:
            np.ndarray: predicted labels (0 or 1)
        """
        return predict(x_test, self.weights, self.bias, threshold)

    def predict_proba(self, x_test):
        """
        Predict probabilities for new data.

        Parameters:
            x_test (np.ndarray): shape (n_samples, n_features)

        Returns:
            np.ndarray: predicted probabilities
        """
        return predict_proba(x_test, self.weights, self.bias)

    def score(self, x_test, y_test):
        """
        Compute accuracy on test data.

        Parameters:
            x_test (np.ndarray): shape (n_samples, n_features)
            y_test (np.ndarray): shape (n_samples,)

        Returns:
            float: accuracy
        """
        y_pred = self.predict(x_test)
        return accuracy(y_test, y_pred)
