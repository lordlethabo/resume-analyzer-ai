from parser import find_skills
from scorer import (
    calculate_weighted_score,
    get_ats_rating,
    get_candidate_rank,
)
from recommendations import (
    generate_recommendations,
    generate_summary,
)


def analyze_resume(resume_text, job_text):
    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_text)

    matched = []
    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = calculate_weighted_score(matched, job_skills)
    rating = get_ats_rating(score)
    rank, recommendation = get_candidate_rank(score)

    summary = generate_summary(score, matched, missing)
    recommendations = generate_recommendations(missing)

    return {
        "score": score,
        "rating": rating,
        "rank": rank,
        "recommendation": recommendation,
        "resume_skills_found": resume_skills,
        "job_skills_found": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "summary": summary,
        "recommendations": recommendations,
  }
