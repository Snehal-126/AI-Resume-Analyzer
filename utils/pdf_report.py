from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


class PDFReport:

    def generate_report(
        self,
        filename,
        match_score,
        ats_score,
        resume_skills,
        matching_skills,
        missing_skills
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>AI Resume Analyzer Report</b>",
                styles["Title"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"<b>Resume Match Score:</b> {match_score}%",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"<b>ATS Score:</b> {ats_score}%",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph("<b>Resume Skills</b>", styles["Heading2"])
        )

        for skill in resume_skills:
            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )

        story.append(Spacer(1, 15))

        story.append(
            Paragraph("<b>Matching Skills</b>", styles["Heading2"])
        )

        for skill in matching_skills:
            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )

        story.append(Spacer(1, 15))

        story.append(
            Paragraph("<b>Missing Skills</b>", styles["Heading2"])
        )

        for skill in missing_skills:
            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "<b>Suggestions</b>",
                styles["Heading2"]
            )
        )

        if missing_skills:
            for skill in missing_skills:
                story.append(
                    Paragraph(
                        f"• Consider learning {skill}",
                        styles["Normal"]
                    )
                )
        else:
            story.append(
                Paragraph(
                    "Excellent! Your resume matches the job description well.",
                    styles["Normal"]
                )
            )

        doc.build(story)