from processor_regex import classify_with_regex
from processor_llm import classify_with_llm


def classify(logs):
    labels = []

    for source, log_msg in logs:
        labels.append(classify_log(source, log_msg))

    return labels


def classify_log(source, log_msg):

    # LegacyCRM logs go to LLM
    if source == "LegacyCRM":
        return classify_with_llm(log_msg)

    # Try regex first
    label = classify_with_regex(log_msg)

    if label:
        return label

    # Import BERT only when required
    from processor_bert import classify_with_bert

    return classify_with_bert(log_msg)


def classify_csv(input_file):
    import pandas as pd

    df = pd.read_csv(input_file)

    df["target_label"] = classify(
        list(zip(df["source"], df["log_message"]))
    )

    output_file = "output.csv"
    df.to_csv(output_file, index=False)

    return output_file


if __name__ == "__main__":
    classify_csv("test.csv")