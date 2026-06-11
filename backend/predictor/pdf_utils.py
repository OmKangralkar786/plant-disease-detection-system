
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(
    filename,
    disease,
    confidence,
    description,
    treatment
):

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "Plant Disease Detection Report",
            styles["Title"]
        ),

        Spacer(1, 20),

        Paragraph(
            f"Disease: {disease}",
            styles["Normal"]
        ),

        Paragraph(
            f"Confidence: {confidence}%",
            styles["Normal"]
        ),

        Paragraph(
            f"Description: {description}",
            styles["Normal"]
        ),

        Paragraph(
            f"Treatment: {treatment}",
            styles["Normal"]
        ),
    ]

    pdf.build(content)

