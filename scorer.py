import config
import questions as qs

def load_scorer():
    """Return this module's judge function for compatibility with the starter."""
    return judge


def judge(question: str, expects: str, answer: str, results) -> bool:
    """Return whether an answer is supported, correct, and sourced.
    The expected phrase must occur in both a retrieved chunk and the answer.
    The answer must also name one of the retrieved source files.
    """
    expected = expects.strip().casefold()
    answer_text = answer.casefold()

    if not expected or expected not in answer_text:
        return False

    retrieved_text = "\n".join(result.text.casefold() for result in results)
    if expected not in retrieved_text:
        return False

    return any(result.source.casefold() in answer_text for result in results)
