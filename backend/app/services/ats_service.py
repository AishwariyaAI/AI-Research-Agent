def calculate_ats_score(
        resume_text,
        job_text
):

    resume_words = set(
        resume_text.lower().split()
    )

    job_words = set(
        job_text.lower().split()
    )

    matched = len(
        resume_words.intersection(
            job_words
        )
    )

    total = len(job_words)

    score = (
        matched / total
    ) * 100

    return round(score, 2)