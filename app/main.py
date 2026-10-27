def normalize_question(question: str) -> str:
    if not isinstance(question, str):
        raise TypeError("question must be string")
    return question.strip()


def main():
    question = "What is Apache Spark? "
    cleaned_question = normalize_question(question)
    print(cleaned_question)


if __name__ == "__main__":
    main()