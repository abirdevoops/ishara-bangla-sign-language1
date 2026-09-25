"""
Ishara - Model Evaluation Metrics

Basic evaluation utilities for the
Bangla Sign Language recognition system.
"""


def safe_divide(numerator, denominator):
    """
    Safely divide two numbers.
    """

    if denominator == 0:
        return 0.0

    return numerator / denominator


def accuracy(correct_predictions, total_predictions):
    """
    Calculate classification accuracy.
    """

    return safe_divide(
        correct_predictions,
        total_predictions
    )


def precision(true_positive, false_positive):
    """
    Calculate precision.

    Precision = TP / (TP + FP)
    """

    return safe_divide(
        true_positive,
        true_positive + false_positive
    )


def recall(true_positive, false_negative):
    """
    Calculate recall.

    Recall = TP / (TP + FN)
    """

    return safe_divide(
        true_positive,
        true_positive + false_negative
    )


def f1_score(precision_value, recall_value):
    """
    Calculate F1 score.

    F1 = 2 * Precision * Recall /
         (Precision + Recall)
    """

    if precision_value + recall_value == 0:
        return 0.0

    return (
        2
        * precision_value
        * recall_value
        / (precision_value + recall_value)
    )


def evaluate_model(
    correct_predictions,
    total_predictions,
    true_positive,
    false_positive,
    false_negative
):
    """
    Calculate the basic evaluation metrics.
    """

    acc = accuracy(
        correct_predictions,
        total_predictions
    )

    prec = precision(
        true_positive,
        false_positive
    )

    rec = recall(
        true_positive,
        false_negative
    )

    f1 = f1_score(
        prec,
        rec
    )

    return {
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1_score": f1
    }


if __name__ == "__main__":

    # Example calculation only.
    # These are NOT Ishara's real AI results.

    results = evaluate_model(
        correct_predictions=90,
        total_predictions=100,
        true_positive=90,
        false_positive=5,
        false_negative=5
    )

    print("Example evaluation:")
    print(f"Accuracy : {results['accuracy']:.2%}")
    print(f"Precision: {results['precision']:.2%}")
    print(f"Recall   : {results['recall']:.2%}")
    print(f"F1 Score : {results['f1_score']:.2%}")

    print("\nThese are example calculations only.")
