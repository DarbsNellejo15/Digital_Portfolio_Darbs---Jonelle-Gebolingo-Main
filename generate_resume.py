import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch

def create_resume(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 0.5 inch margins for clean 1-page fit
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    primary_color = colors.HexColor("#1e1b4b")  # Deep indigo
    accent_color = colors.HexColor("#3b82f6")   # Royal blue
    text_dark = colors.HexColor("#1f2937")       # Charcoal
    text_muted = colors.HexColor("#4b5563")      # Medium slate
    border_color = colors.HexColor("#e2e8f0")    # Light border
    badge_bg = colors.HexColor("#eff6ff")        # Soft blue badge

    name_style = ParagraphStyle(
        'ResumeName',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=26,
        textColor=primary_color,
        spaceAfter=2
    )

    title_style = ParagraphStyle(
        'ResumeTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=accent_color,
        spaceAfter=6
    )

    contact_style = ParagraphStyle(
        'ResumeContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_muted
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=3,
        textTransform='uppercase'
    )

    body_style = ParagraphStyle(
        'ResumeBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_dark
    )

    item_title = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=primary_color
    )

    item_subtitle = ParagraphStyle(
        'ItemSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=accent_color
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=text_dark,
        leftIndent=10
    )

    skill_category = ParagraphStyle(
        'SkillCategory',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=primary_color
    )

    skill_desc = ParagraphStyle(
        'SkillDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_dark
    )

    story = []

    # 1. Header
    story.append(Paragraph("JONELLE GEBOLINGO", name_style))
    story.append(Paragraph("Information Technology Student &bull; Web Development &bull; IT Support & Troubleshooting", title_style))
    
    contact_text = (
        "<b>Email:</b> jonellegebolingo15@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Location:</b> Philippines &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>GitHub:</b> github.com/DarbsNellejo15 &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<b>Portfolio:</b> darbs-portfolio"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_color, spaceBefore=2, spaceAfter=6))

    # 2. Professional Summary
    story.append(Paragraph("Professional Summary", section_heading))
    summary_text = (
        "Motivated and detail-oriented Information Technology student at Torres Capitol College with practical expertise "
        "in web development, computer hardware/software troubleshooting, and programming. Experienced in designing responsive "
        "user interfaces, building AI-driven diagnostic solutions (DARBS AI), and delivering reliable IT support. Highly adaptable, "
        "analytical, and passionate about solving complex technical problems while contributing positively to organizational goals."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 4))

    # 3. Education
    story.append(Paragraph("Education", section_heading))
    edu_data = [
        [
            Paragraph("<b>Bachelor of Science in Information Technology (BSIT)</b>", item_title),
            Paragraph("<b>2023 &ndash; Present (3rd Year)</b>", ParagraphStyle('RightDate', parent=body_style, alignment=2, fontName='Helvetica-Bold'))
        ],
        [
            Paragraph("Torres Capitol College &bull; Philippines", item_subtitle),
            Paragraph("Undergraduate Studies", ParagraphStyle('RightSub', parent=body_style, alignment=2, textColor=text_muted))
        ]
    ]
    edu_table = Table(edu_data, colWidths=[380, 160])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Paragraph("&bull; Focused coursework: Web Development, Computer Hardware Troubleshooting, Database Systems, Network Fundamentals, Object-Oriented Programming, and IT Ethics.", bullet_style))
    story.append(Spacer(1, 4))

    # 4. Technical Skills & Abilities
    story.append(Paragraph("Technical Skills & Abilities", section_heading))
    skills_data = [
        [
            Paragraph("<b>Web & Frontend:</b>", skill_category),
            Paragraph("HTML5, CSS3, JavaScript (ES6+), React.js, Responsive UI/UX Design, CSS Grid & Flexbox", skill_desc)
        ],
        [
            Paragraph("<b>Programming & Data:</b>", skill_category),
            Paragraph("Python, SQL, Database Management, Scripting, Algorithm Design, API Integration", skill_desc)
        ],
        [
            Paragraph("<b>IT Support & Hardware:</b>", skill_category),
            Paragraph("Hardware & Software Troubleshooting, System Diagnostics, PC Assembly/Maintenance, OS Optimization", skill_desc)
        ],
        [
            Paragraph("<b>Tools & Platforms:</b>", skill_category),
            Paragraph("Git, GitHub, Firebase, VS Code, Vite, Microsoft Office (Word, Excel), Video Editing Software", skill_desc)
        ],
        [
            Paragraph("<b>Core Strengths:</b>", skill_category),
            Paragraph("Technical Problem Solving, Analytical Thinking, Time Management, Patience, Team Collaboration", skill_desc)
        ],
    ]
    skills_table = Table(skills_data, colWidths=[130, 410])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))

    # 5. Key Projects
    story.append(Paragraph("Projects & Applied Experience", section_heading))
    
    # Project 1: DARBS AI
    p1_data = [
        [
            Paragraph("<b>DARBS AI &ndash; Diagnostic Assistant for Repair, Bugs, and Support</b>", item_title),
            Paragraph("<b>Python &bull; Firebase &bull; AI Diagnostics</b>", ParagraphStyle('ProjTech', parent=body_style, alignment=2, textColor=accent_color, fontName='Helvetica-Bold'))
        ]
    ]
    p1_table = Table(p1_data, colWidths=[350, 190])
    p1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p1_table)
    story.append(Paragraph("&bull; Architected an AI-driven troubleshooting assistant engineered to guide users in detecting, diagnosing, and resolving common PC hardware/software performance bottlenecks.", bullet_style))
    story.append(Paragraph("&bull; Integrated cloud-backed knowledge bases with Firebase to deliver instantaneous diagnostic suggestions and step-by-step remediation procedures.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 2: PC Diagnostic Utility
    p2_data = [
        [
            Paragraph("<b>PC Diagnostic Utility & System Health Scanner</b>", item_title),
            Paragraph("<b>Python &bull; Automation &bull; Diagnostics</b>", ParagraphStyle('ProjTech2', parent=body_style, alignment=2, textColor=accent_color, fontName='Helvetica-Bold'))
        ]
    ]
    p2_table = Table(p2_data, colWidths=[350, 190])
    p2_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p2_table)
    story.append(Paragraph("&bull; Developed an automated system diagnostic tool for rapid hardware health evaluation, CPU/memory usage telemetry, and storage integrity assessment.", bullet_style))
    story.append(Paragraph("&bull; Reduced troubleshooting inspection time through automated metric reporting and intuitive error code summaries.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 3: Responsive Web Portfolio & Development Projects
    p3_data = [
        [
            Paragraph("<b>DARBS Digital Portfolio & Interactive Web Applications</b>", item_title),
            Paragraph("<b>HTML5 &bull; CSS3 &bull; JavaScript &bull; Git</b>", ParagraphStyle('ProjTech3', parent=body_style, alignment=2, textColor=accent_color, fontName='Helvetica-Bold'))
        ]
    ]
    p3_table = Table(p3_data, colWidths=[350, 190])
    p3_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p3_table)
    story.append(Paragraph("&bull; Designed modern responsive web interfaces featuring glassmorphic design systems, dynamic JSON data loading, and cross-browser compatibility.", bullet_style))
    story.append(Spacer(1, 4))

    # 6. Certifications & Academic Achievements
    story.append(Paragraph("Certifications & Training", section_heading))
    cert_data = [
        [
            Paragraph("&bull; <b>Cisco Networking Academy</b> &ndash; Verified Networking and IT Fundamentals Certification", bullet_style),
            Paragraph("Cisco NetAcad", ParagraphStyle('CertIss', parent=body_style, alignment=2, textColor=text_muted))
        ],
        [
            Paragraph("&bull; <b>DEVCON Sui Move Code Camp 2026</b> &ndash; Blockchain & Smart Contract Development Level 1", bullet_style),
            Paragraph("DEVCON", ParagraphStyle('CertIss2', parent=body_style, alignment=2, textColor=text_muted))
        ],
        [
            Paragraph("&bull; <b>BSIT Technical Seminar & Skills Workshop 2026</b> &ndash; IT Infrastructure & Applications", bullet_style),
            Paragraph("Torres Capitol College", ParagraphStyle('CertIss3', parent=body_style, alignment=2, textColor=text_muted))
        ]
    ]
    cert_table = Table(cert_data, colWidths=[420, 120])
    cert_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(cert_table)

    doc.build(story)
    print(f"Resume generated successfully at: {output_path}")

if __name__ == '__main__':
    targets = [
        "c:/Digital_Portfolio_Darbs---Jonelle-Gebolingo-main/assets/docs/Jonelle_Gebolingo_Resume.pdf",
        "c:/Digital_Portfolio_Darbs---Jonelle-Gebolingo-main/public/assets/docs/Jonelle_Gebolingo_Resume.pdf",
        "c:/Digital_Portfolio_Darbs---Jonelle-Gebolingo-main/Jonelle_Gebolingo_Resume.pdf"
    ]
    for target in targets:
        create_resume(target)
