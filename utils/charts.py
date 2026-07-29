import matplotlib.pyplot as plt


class ChartGenerator:

    def score_chart(self, match_score, ats_score):

        fig, ax = plt.subplots(figsize=(5, 3))

        labels = ["Resume Match", "ATS Score"]
        values = [match_score, ats_score]

        ax.bar(labels, values)

        ax.set_ylim(0, 100)
        ax.set_ylabel("Score (%)")
        ax.set_title("Resume Analysis Scores")

        return fig

    def skill_chart(self, matching_count, missing_count):

        fig, ax = plt.subplots(figsize=(4, 4))

        labels = ["Matching", "Missing"]
        values = [matching_count, missing_count]

        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Skill Analysis")

        return fig