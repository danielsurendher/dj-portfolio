from django.shortcuts import render


def home(request):
    context = {
        "profile": {
            "name": "Akash B",
            "role": "Backend Developer — Python & Django",
            "email": "danielsurendher@gmail.com",
            "phone": "+91 80722 29219",
            "phone_link": "+918072229219",
            "location": "Nagapattinam, Tamil Nadu",
            "address": "No.138, T.M.S.S.S, Sellur, Nagapattinam",
            "github": "https://github.com/danielsurendher",
            "github_label": "github.com/danielsurendher",
            "project_github": "https://github.com/danielsurendher/Gtec-site",
        },
        "skills": [
            {"title": "Backend & Database", "items": ["Python", "Django", "MySQL"]},
            {"title": "Frontend", "items": ["HTML", "CSS", "JavaScript (Basic)", "jQuery"]},
            {"title": "Tools & Professional", "items": ["Git", "GitHub", "Microsoft Office", "Communication", "Problem-Solving", "Team Collaboration"]},
        ],
        "experiences": [
            {
                "date": "2024 – 2025",
                "title": "Supervisor & Clearing and Forwarding Incharge",
                "company": "Ramco Cements Ltd",
                "points": [
                    "Managed daily warehouse and logistics operations, ensuring timely dispatch and receipt of cement consignments.",
                    "Coordinated with transporters, dealers and sales teams to support smooth distribution.",
                    "Maintained documentation including billing, delivery challans and stock registers.",
                ],
            },
            {
                "date": "2023",
                "title": "Mathematics Tutor",
                "company": "Focus Edumatics",
                "points": [
                    "Provided academic support and explained mathematical concepts.",
                    "Helped students strengthen problem-solving skills and prepare assignments and examinations.",
                ],
            },
            {
                "date": "2022",
                "title": "Front-End Developer Trainee",
                "company": "Iyeal Solution",
                "points": [
                    "Assisted in creating basic web pages using HTML and CSS.",
                    "Helped arrange page content, apply styles, check pages and fix small errors.",
                    "Worked with the team on assigned front-end tasks.",
                ],
            },
        ],
        "education": [
            {"year": "2017 – 2021", "qualification": "B.Tech — Information Technology", "institution": "EGS Pillay Engineering College", "score": "77.20%"},
            {"year": "2016 – 2017", "qualification": "Higher Secondary (HSC)", "institution": "St. Anthony's Hr. Sec. School", "score": "62.25%"},
            {"year": "2014 – 2015", "qualification": "SSLC", "institution": "St. Anthony's Hr. Sec. School", "score": "78.00%"},
        ],
    }
    return render(request, "portfolio/index.html", context)
