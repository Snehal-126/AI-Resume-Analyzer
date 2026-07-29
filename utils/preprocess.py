import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


class ResumePreprocessor:

    def clean_text(self, text):
        """
        Clean resume text by removing URLs, emails,
        phone numbers, labels, special characters,
        and extra spaces.
        """

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", "", text)

        # Remove Email IDs
        text = re.sub(r"\S+@\S+", "", text)

        # Remove Phone Numbers
        text = re.sub(r"\+?\d[\d\s\-]{8,}\d", "", text)

        # Remove common labels
        text = re.sub(
            r"\b(email|phone|mobile|contact|skills|skill|education|projects|project|experience|objective|summary)\b",
            "",
            text,
            flags=re.IGNORECASE
        )

        # Keep only letters and spaces
        text = re.sub(r"[^a-zA-Z\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def preprocess(self, text):
        """
        Perform NLP preprocessing.
        Returns:
            cleaned_text (str)
            tokens (list)
        """

        text = self.clean_text(text)

        doc = nlp(text)

        tokens = []

        for token in doc:
            if (
                not token.is_stop
                and not token.is_punct
                and not token.is_space
            ):
                tokens.append(token.lemma_.lower())

        cleaned_text = " ".join(tokens)

        return cleaned_text, tokens