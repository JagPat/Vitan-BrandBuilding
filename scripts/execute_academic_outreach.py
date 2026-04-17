import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Zoho SMTP Configuration
SMTP_HOST = os.environ.get("ZOHO_SMTP_HOST", "smtp.zoho.in")
SMTP_PORT = int(os.environ.get("ZOHO_SMTP_PORT", 465))
SMTP_USER = os.environ.get("ZOHO_SMTP_USER", "jp@vitan.in")
SMTP_PASS = os.environ.get("ZOHO_SMTP_PASS")

ABSTRACT = """
ACADEMIC AUTHORITY ABSTRACT
Architecture is often judged in the moment of presentation, but its real test starts when people begin using the space every day. This session explores how design decisions influence movement, comfort, behavior, and long-term usefulness in lived environments. Drawing from practice-based experience in western India, the talk looks at how human-centered thinking, contextual response, and execution discipline help projects remain meaningful beyond visual appeal. The objective is to give students a more grounded lens on architecture as something people inhabit, not just something they view.
"""

BIO = """
SHORT FOUNDER BIO
Jagrut Patel leads Vitan Architects with a practice lens rooted in human-centered design, contextual response, and projects that remain strong in real use, not only on presentation boards. His work emphasizes architecture that supports everyday life through clarity, long-term relevance, and buildable thinking. In academic settings, his strongest contribution is connecting design intent with what actually happens when spaces are inhabited, operated, and maintained.
"""

EMAILS = [
    {
        "to": "sameep.padora@cept.ac.in",
        "subject": "Architecture beyond the render: A conversation on built consequence",
        "body": """Dear Sameep,

I have long admired CEPT's commitment to pushing the intellectual boundaries of design culture. At Vitan Architects, we have been focusing our practice on the "translation layer"—the space between a design's intent and how it actually performs once inhabited.

I would welcome the opportunity to visit CEPT for a guest lecture or a design conversation with your students. I've titled the talk "How everyday buildings quietly shape the people who use them." The session avoids promotional narratives, focusing instead on how design decisions—rooted in the climate and context of western India—influence movement, comfort, and long-term behavior.

The goal is to provide students with a grounded lens on architecture as something people inhabit, not just something they view.

I have included a short abstract and bio below for your review. I look forward to the possibility of engaging with the CEPT community.

Warm regards,

Jagrut Patel
Principal Architect, Vitan Architects
"""
    },
    {
        "to": "director.ia@nirmauni.ac.in",
        "subject": "Connecting design intent with practice reality: Guest Lecture proposal",
        "body": """Dear Rekha,

Nirma University has a strong reputation for producing architects who understand both the creative and practical demands of the profession. At Vitan Architects, we believe that the strongest design quality is always paired with execution discipline.

I am writing to propose a guest lecture for your students titled "How everyday buildings quietly shape the people who use them." The talk explores how human-centered thinking and contextual response help projects remain meaningful and functional long after the presentation phase ends.

In addition to the lecture, I would be happy to participate in a portfolio review session or provide an internship information brief for your senior students, focusing on the transition from design intent to lived project reality.

I've included an abstract and brief bio below. I would be delighted to discuss how this session might best fit into your current academic calendar.

Warm regards,

Jagrut Patel
Principal Architect, Vitan Architects
"""
    },
    {
        "to": "snehal.nagarsheth@anu.edu.in",
        "subject": "Architecture for human impact: A studio talk proposal",
        "body": """Dear Snehal,

Anant University's focus on the social and human impact of design aligns deeply with our philosophy at Vitan Architects. We believe architecture's real test begins when the presentation boards are put away and everyday life starts in the space.

I would love to visit your studio for a talk on "How everyday buildings quietly shape the people who use them." This session focuses on architecture as a series of decisions that influence behavior, clarity, and long-term usability. We will look at how human-centered thinking—grounded in our shared Ahmedabad context—can create outcomes that are socially and functionally meaningful.

Our aim is to encourage students to see architecture through the lens of those who move, gather, and live within it.

Please find the talk abstract and my bio below. I hope to have the chance to share these perspectives with your students.

Warm regards,

Jagrut Patel
Principal Architect, Vitan Architects
"""
    }
]

def send_email(to_addr, subject, body):
    msg = MIMEMultipart()
    msg["From"] = f"Jagrut Patel <{SMTP_USER}>"
    msg["To"] = to_addr
    msg["Subject"] = subject
    
    full_body = body + "\n\n---\n" + ABSTRACT + "\n\n---\n" + BIO
    msg.attach(MIMEText(full_body, "plain"))
    
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print(f"Successfully sent email to {to_addr}")
        return True
    except Exception as e:
        print(f"Failed to send email to {to_addr}: {e}")
        return False

if __name__ == "__main__":
    if not SMTP_PASS:
        print("Error: ZOHO_SMTP_PASS environment variable not set.")
        exit(1)
        
    for email_data in EMAILS:
        send_email(email_data["to"], email_data["subject"], email_data["body"])
