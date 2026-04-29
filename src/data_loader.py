import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split


def load_and_preprocess_data(data_dir, class_config):
    """Load, preprocess, and prepare data for training."""

    # Load dataset
    file_path = os.path.join(data_dir, 'combined_dataset.csv')
    df = pd.read_csv(file_path)

    # Rename label column
    df.rename(columns={'label': 'Attack_Type'}, inplace=True)

    # Split features and labels
    X = df.drop(['Attack_Type'], axis=1)
    y = df['Attack_Type']

    # Clean data (important)
    X.replace([np.inf, -np.inf], np.nan, inplace=True)
    X.fillna(0, inplace=True)

    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    y_categorical = to_categorical(y_encoded)

    # Train/Test split
    X_train, X_test, y_train_categorical, y_test_categorical = train_test_split(
        X, y_categorical, test_size=0.2, random_state=42
    )

    # Validation split
    X_train, X_val, y_train_categorical, y_val_categorical = train_test_split(
        X_train, y_train_categorical, test_size=0.2, random_state=42
    )

    # Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    # Reshape for CNN
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_val = X_val.reshape(X_val.shape[0], X_val.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    return X_train, X_val, X_test, y_train_categorical, y_val_categorical, y_test_categorical, label_encoder