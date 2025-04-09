from detoxify import Detoxify

class TextAnalyzer:
    def __init__(self):
        self.model = Detoxify('unbiased')

    def analyze_text(self, text):
        results = self.model.predict(text)
        is_appropriate = results['toxicity'] < 0.5
        return {
            'is_appropriate': is_appropriate,
            'scores': results
        }
