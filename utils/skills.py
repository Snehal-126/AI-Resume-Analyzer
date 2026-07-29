import pandas as pd


class SkillExtractor:

    def __init__(self):

        self.skills = pd.read_csv("data/skills.csv")

        self.skill_list = (
            self.skills["Skill"]
            .dropna()
            .str.lower()
            .tolist()
        )

    def extract_skills(self, processed_text):

        found_skills = []

        text = processed_text.lower()

        for skill in self.skill_list:

            if skill.lower() in text:

                found_skills.append(skill.title())

        return sorted(list(set(found_skills)))