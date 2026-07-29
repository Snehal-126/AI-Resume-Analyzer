class ATSAnalyzer:

    def calculate_ats_score(
        self,
        match_score,
        total_resume_skills,
        total_job_skills
    ):

        if total_job_skills == 0:
            return 0

        skill_score = (
            total_resume_skills / total_job_skills
        ) * 100

        ats_score = (
            match_score * 0.7
        ) + (
            skill_score * 0.3
        )

        return round(min(ats_score, 100), 2)