def generate_recommendations(missing_skills):
    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Add {skill.title()} to your learning roadmap or project experience."
        )

    return recommendations


def generate_summary(score, matched_skills, missing_skills):
    if matched_skills:
        matched_text = ", ".join(matched_skills)
    else:
        matched_text = "no matching skills"

    summary = f"Candidate demonstrates experience in {matched_text}. "

    if score >= 70:
        summary += "The resume is strongly aligned with the target role. "
    elif score >= 50:
        summary += "The resume is partially aligned with the target role. "
    else:
        summary += "The resume has limited alignment with the target role. "

    if missing_skills:
        missing_text = ", ".join(missing_skills)
        summary += f"Key skill gaps include {missing_text}."

    return summary
