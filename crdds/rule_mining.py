from sklearn.base import BaseEstimator, ClassifierMixin


class CRDDS(BaseEstimator, ClassifierMixin):
    """Main class responsible for implementing Causal Rule Discovery from Data Streams.
    It assumes that the dataset provided has already been discretized with one of the provided Discretizers.
    """

    def __init__(self, params=None):
        pass

    def fit(self, X, y):
        return self

    def predict(self, X):
        return None
