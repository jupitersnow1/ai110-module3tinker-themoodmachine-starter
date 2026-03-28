# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    _ASCII_EMOTICONS = {
        ":)": "EMOJI_HAPPY", ":-)": "EMOJI_HAPPY",
        ":(": "EMOJI_SAD",   ":-(": "EMOJI_SAD",
        ":d": "EMOJI_LAUGH", ":-d": "EMOJI_LAUGH",
    }

    _TOKEN_PATTERN = re.compile(
        r':-[)(d]|:[)(d]'            # ASCII emoticons (matched after lowercasing)
        r'|[\U00010000-\U0010ffff]'   # Unicode emojis, passed through as-is
        r'|[a-z0-9]+'                 # words and numbers
    )

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        - Strips leading and trailing whitespace
        - Converts everything to lowercase
        - Handles ASCII emoticons (mapped to labels) and Unicode emojis (passed through)
        - Removes punctuation implicitly via tokenization
        - Normalizes repeated characters ("soooo" -> "soo")
        """
        tokens = []
        for match in self._TOKEN_PATTERN.findall(text.strip().lower()):
            if match in self._ASCII_EMOTICONS:
                tokens.append(self._ASCII_EMOTICONS[match])
            else:
                tokens.append(re.sub(r'(.)\1{2,}', r'\1\1', match))
        return tokens


    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        # TODO: Implement this method.
        #   1. Call self.preprocess(text) to get tokens.
        tokens = self.preprocess(text)
        score = 0 # * start at 0

        # Hint: if you implement negation, you may want to look at pairs of tokens,
        # like ("not", "happy") or ("never", "fun").
        negations = ("not", "never", "no", "don't", "doesn't", "didn't", "isn't", "wasn't")

        #   2. Loop over the tokens.
        for i, token in enumerate(tokens):
            is_negated = i>0 and tokens[i-1] in negations
            
        #   3. Increase the score for positive words, decrease for negative words.
            if token in self.positive_words:
                score += -1 if is_negated else 1 # * if Positive signal -> add point (add -1 if its a negation)

            elif token in self.negative_words:
                score += 1 if is_negated else -1. # * elif Negative signal -> subtract points

        #   4. Return the total score.
        return score


    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        score = self.score_text(text)

        pos_hits = sum(1 for t in self.preprocess(text) if t in self.positive_words)
        neg_hits = sum(1 for t in self.preprocess(text) if t in self.negative_words)

        if pos_hits>0 and neg_hits > 0:
            return "mixed"

        #   2. Return "positive" if the score is above 0.
        if score > 0:
            return "positive"
        
        #   3. Return "negative" if the score is below 0.
        elif score < 0:
            return "negative"
        
        #   4. Return "neutral" otherwise.
        else: 
            return "neutral"
            # return "mixed"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )

# if __name__ == "__main__":

    # (1) testing out `preprocess()` function
    # from dataset import SAMPLE_POSTS
    # analyzer = MoodAnalyzer()
    # for post in SAMPLE_POSTS:
    #     tokens = analyzer.preprocess(post)
    #     print(f"Input : {post}")
    #     print(f"Tokens: {tokens}")
    #     print()

