SKILL_WEIGHTS = {
    "python": 10,
    "sql": 8,
    "azure": 10,
    "aws": 10,
    "oracle cloud": 10,
    "oci": 10,
    "docker": 8,
    "terraform": 9,
    "linux": 8,
    "git": 5,
    "github": 5,
    "html": 3,
    "css": 3,
    "javascript": 4,
    "fastapi": 7,
    "api": 6,
    "postgresql": 8,
    "firebase": 6,
    "vercel": 5,
    "cloud": 7,
    "devops": 8,
}


def calculate_weighted_score(matched_skills, job_skills):
    total_weight = 0
    matched_weight = 0

    for skill in job_skills:
        total_weight += SKILL_WEIGHTS.get(skill, 1)

    for skill in matched_skills:
        matched_weight += SKILL_WEIGHTS.get(skill, 1)

    if total_weight == 0:
        return 0

    return round((matched_weight / total_weight) * 100, 0)


def get_ats_rating(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Fair"
    else:
        return "Needs Improvement"


def get_candidate_rank(score):
    if score >= 85:
        return "Top Candidate", "Interview Recommended"
    elif score >= 70:
        return "Strong Candidate", "Interview Recommended"
    elif score >= 50:
        return "Average Candidate", "Improve Resume Before Applying"
    else:
        return "Weak Candidate", "Additional Skills Required"
