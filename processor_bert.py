import joblib
from sentence_transformers import SentenceTransformer

model_embedding = None
model_classification = None


def load_models():
    global model_embedding
    global model_classification

    if model_embedding is None:
        model_embedding = SentenceTransformer("all-MiniLM-L6-v2")

    if model_classification is None:
        model_classification = joblib.load("models/log_classifier.joblib")


def classify_with_bert(log_message):

    load_models()

    embedding = model_embedding.encode([log_message])

    probabilities = model_classification.predict_proba(embedding)[0]

    if max(probabilities) < 0.5:
        return "Unclassified"

    return model_classification.predict(embedding)[0]


if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - API returned 404",
        "Server crashed",
        "User login failed"
    ]

    for log in logs:
        print(classify_with_bert(log))