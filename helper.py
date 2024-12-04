import sklearn as skl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def compute_confusion_matrix_metrics(y_true, y_pred):
    tn, fp, fn, tp = skl.metrics.confusion_matrix(y_true, y_pred).ravel()

    # accuracy
    accuracy = (tn + tp) / (tn + tp + fn + fp)
    sensitivity =  tp / (tp + fn)
    specificity = tn / (tn + fp)
    precision = tp / (tp + fp)
    f1_score = 2 * precision * sensitivity / (precision + sensitivity)
    return {'accuracy': accuracy,
            'sensitivity': sensitivity,
            "specificity": specificity,
            "precision": precision,
            "f1_score": f1_score}


# handles 2 side by side bars
def show_values_on_bar(bars, ax=plt):
    for bar in bars:
        height = bar.get_height()  # Get the height of the bar
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # X-coordinate
            height,                             # Y-coordinate (on top of the bar)
            f'{np.round(height, 2)}',           # The value to display
            ha='center',                        # Horizontal alignment
            va='bottom'                         # Vertical alignment
        )

        

def inverse_model(x, a, b):
    return a / (x + b)

def find_model_params(X, y, initial_guess=[15,5]):
    params, covariance = curve_fit(inverse_model, X, y, p0=initial_guess)
    a_fit, b_fit = params
    return a_fit, b_fit

def noise(scale=4, size=1):
    return np.random.normal(scale=scale, size=size)

def impute_age(X):
    dropped = X[['Age', 'SibSp']].dropna()
    sibsp = dropped['SibSp']
    age = dropped['Age']

    a, b = find_model_params(sibsp, age)
    print(f"Fitted Params: {a:.1f} / x + {b:.1f}")

    # fill in missing data, add a bit of randomness
    x_mask = X['Age'].isna()
    sibsp_masked = X['SibSp'][x_mask]
    predicted_ages = [(inverse_model(x, a, b) + noise()).round() for x in sibsp_masked]

    X.loc[x_mask, 'Age'] = predicted_ages
    return X, sibsp, age, sibsp_masked, predicted_ages, a, b


def average_fares_by_pclass(X):
    all_pclass_values = X['Pclass'].value_counts().keys()
    fare_by_pclass = {} # empty dict to populate

    for pclass in all_pclass_values:
        selected_x = X[X['Pclass'] == pclass]
        avg_fare = selected_x['Fare'].sum() / selected_x['Fare'].shape[0]
        fare_by_pclass[pclass] = avg_fare
    
    return fare_by_pclass


# use Pclass. average the fares for the given Pclass for imputation
def impute_fare(X):
    dropped = X[['Pclass', 'Fare']].dropna()
    pclass = dropped['Pclass']
    fare = dropped['Fare']

    x_mask = X['Fare'].isna()
    pclass_masked = X['Pclass'][x_mask]
    avg_fares = average_fares_by_pclass(X)

    predicted_fares = [avg_fares[pc] for pc in pclass_masked]
    X.loc[x_mask, 'Fare'] = predicted_fares
    return X