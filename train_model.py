# train_model.py (Version 3.0 - The Final Fix)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

print("Starting FINAL model training process (addressing class imbalance)...")

# 1. Load the dataset
try:
    df = pd.read_csv('spam.csv', encoding='latin-1')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: spam.csv not found.")
    exit()

# 2. Preprocess the data
df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
print("Data preprocessing complete.")

# 3. Split data
X = df['message']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")

# 4. Create the definitive machine learning pipeline
model_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
    # THE FIX: Add class_weight='balanced' to fight the data imbalance
    ('classifier', LogisticRegression(random_state=42, class_weight='balanced'))
])
print("Definitive model pipeline created with class_weight='balanced'.")

# 5. Train the definitive model
print("Training the definitive model...")
model_pipeline.fit(X_train, y_train)
print("Model training complete.")

# 6. Evaluate the model
print("\n--- Model Evaluation ---")
y_pred = model_pipeline.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['Legitimate', 'Scam/Spam']))
print("------------------------\n")
# Pay attention to the 'recall' score for 'Scam/Spam'. It should be much higher now.

# 7. Save the definitive model
joblib.dump(model_pipeline, 'chatguard_model.pkl')
print("Definitive, balanced model saved as 'chatguard_model.pkl'.")
print("Training process finished successfully!")