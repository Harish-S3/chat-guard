# chatguard.py

import joblib

class ChatGuard:
    """
    The AI-powered engine to detect scam/spam messages.
    """
    def __init__(self, model_path='chatguard_model.pkl'):
        """
        Loads the pre-trained model from the given path.
        """
        try:
            self.model = joblib.load(model_path)
            print("ChatGuard engine loaded successfully.")
        except FileNotFoundError:
            print(f"Error: Model file not found at '{model_path}'.")
            print("Please run 'train_model.py' first to create the model.")
            self.model = None

    def analyze_message(self, message):
        """
        Analyzes a single message and returns a risk assessment.

        Args:
            message (str): The text message to analyze.

        Returns:
            dict: A dictionary containing the prediction and a risk score.
        """
        if not self.model:
            return {
                'prediction': 'Error',
                'risk_score': -1,
                'explanation': 'Model not loaded.'
            }

        # The model expects a list of documents, so we pass the message in a list
        prediction = self.model.predict([message])[0]
        
        # Get the probability scores for each class (0 for ham, 1 for spam)
        probabilities = self.model.predict_proba([message])[0]
        risk_score = probabilities[1] # The probability of being a scam

        if prediction == 1:
            is_scam = True
        else:
            is_scam = False

        return {
            'is_scam': is_scam,
            'risk_score': float(f"{risk_score:.4f}") # Format to 4 decimal places
        }

# This part allows you to test the engine directly
if __name__ == '__main__':
    print("--- Testing ChatGuard Engine ---")
    guard = ChatGuard()

    if guard.model:
        # Test with a few sample messages
        safe_message = "Hey, are we still on for lunch tomorrow?"
        scam_message = "Congratulations! You've won a free iPhone. Click here to claim now http://bit.ly/scamlink"

        print(f"\nAnalyzing: '{safe_message}'")
        result1 = guard.analyze_message(safe_message)
        print(f"Result: {result1}")

        print(f"\nAnalyzing: '{scam_message}'")
        result2 = guard.analyze_message(scam_message)
        print(f"Result: {result2}")