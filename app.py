from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "resume-career-project"


# =====================================================
# DATABASE CONNECTION
# =====================================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Samiksha22",
    database="resume_career_db"
)


# =====================================================
# CAREER SKILLS
# =====================================================

profession_skills = {

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "statistics",
        "power bi",
        "data visualization"
    ],

    "Python Developer": [
        "python",
        "oop",
        "flask",
        "database",
        "git",
        "problem solving"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "responsive design",
        "backend",
        "git"
    ],

    "Software Tester": [
        "testing",
        "manual testing",
        "test case",
        "bug reporting",
        "automation testing",
        "sdlc"
    ],

    "Teacher": [
        "teaching",
        "communication",
        "subject knowledge",
        "lesson planning",
        "classroom management",
        "presentation"
    ],

    "Database Administrator": [
        "sql",
        "mysql",
        "database",
        "database security",
        "backup and recovery",
        "linux"
    ],

    "Business Analyst": [
        "excel",
        "sql",
        "communication",
        "requirement analysis",
        "power bi",
        "problem solving"
    ],

    "UI/UX Designer": [
        "ui/ux",
        "figma",
        "wireframing",
        "user research",
        "prototyping",
        "design"
    ],

    "Cybersecurity Analyst": [
        "networking",
        "linux",
        "cybersecurity",
        "security tools",
        "ethical hacking",
        "cryptography"
    ],

    "AI/ML Engineer": [
        "python",
        "mathematics",
        "statistics",
        "machine learning",
        "data processing",
        "deep learning"
    ]
}


# =====================================================
# CAREER ROADMAPS
# =====================================================

roadmaps = {

    "Data Analyst": [
        "Learn Excel and basic data handling",
        "Learn SQL and database concepts",
        "Learn Python for Data Analysis",
        "Learn Statistics basics",
        "Learn Power BI and Data Visualization",
        "Practice with real-world datasets",
        "Create projects and prepare for interviews"
    ],

    "Python Developer": [
        "Learn Python basics",
        "Learn Functions and OOP",
        "Learn Python Libraries",
        "Learn File and Database Handling",
        "Build Python Projects",
        "Learn Flask or Django",
        "Prepare for Python Developer interviews"
    ],

    "Web Developer": [
        "Learn HTML",
        "Learn CSS",
        "Learn JavaScript basics",
        "Learn Responsive Web Design",
        "Learn Backend basics",
        "Build Web Projects",
        "Prepare for Web Developer interviews"
    ],

    "Software Tester": [
        "Learn Software Testing basics",
        "Learn SDLC and STLC",
        "Learn Manual Testing",
        "Learn Test Case Design",
        "Learn Bug Reporting",
        "Learn Automation Testing basics",
        "Prepare for Testing interviews"
    ],

    "Teacher": [
        "Improve Communication Skills",
        "Learn Subject Knowledge",
        "Learn Teaching Methods",
        "Learn Lesson Planning",
        "Practice Teaching",
        "Learn Classroom Management",
        "Prepare for Teaching opportunities"
    ],

    "Database Administrator": [
        "Learn Database Concepts",
        "Learn SQL",
        "Learn MySQL",
        "Learn Database Security",
        "Learn Backup and Recovery",
        "Practice Database Management",
        "Prepare for DBA interviews"
    ],

    "Business Analyst": [
        "Learn Business Analysis basics",
        "Improve Communication Skills",
        "Learn Excel",
        "Learn SQL basics",
        "Learn Data Visualization",
        "Learn Requirement Analysis",
        "Prepare for Business Analyst interviews"
    ],

    "UI/UX Designer": [
        "Learn UI/UX fundamentals",
        "Learn User Research",
        "Learn Wireframing",
        "Learn Figma basics",
        "Create UI/UX Designs",
        "Build a Design Portfolio",
        "Prepare for UI/UX opportunities"
    ],

    "Cybersecurity Analyst": [
        "Learn Computer Networking",
        "Learn Operating System basics",
        "Learn Cybersecurity fundamentals",
        "Learn Security Tools",
        "Learn Ethical Hacking basics",
        "Practice Security Labs",
        "Prepare for Cybersecurity interviews"
    ],

    "AI/ML Engineer": [
        "Learn Python",
        "Learn Mathematics basics",
        "Learn Statistics",
        "Learn Machine Learning basics",
        "Learn Data Processing",
        "Build Machine Learning Projects",
        "Prepare for AI/ML opportunities"
    ]
}


# =====================================================
# LEARNING RESOURCES
# =====================================================

learning_resources_data = {

    "Data Analyst": [
        ("Excel", "YouTube Tutorials / Microsoft Learn"),
        ("SQL", "W3Schools / YouTube Tutorials"),
        ("Python", "W3Schools / YouTube Tutorials"),
        ("Statistics", "Khan Academy"),
        ("Power BI", "Microsoft Learn / YouTube Tutorials"),
        ("Data Visualization", "YouTube Tutorials")
    ],

    "Python Developer": [
        ("Python", "W3Schools / YouTube Tutorials"),
        ("OOP", "YouTube Tutorials"),
        ("Flask", "YouTube Tutorials"),
        ("Database", "W3Schools / YouTube Tutorials"),
        ("Git", "YouTube Tutorials"),
        ("Problem Solving", "YouTube / Practice Platforms")
    ],

    "Web Developer": [
        ("HTML", "W3Schools / YouTube Tutorials"),
        ("CSS", "W3Schools / YouTube Tutorials"),
        ("JavaScript", "W3Schools / YouTube Tutorials"),
        ("Responsive Design", "YouTube Tutorials"),
        ("Backend", "YouTube Tutorials"),
        ("Git", "YouTube Tutorials")
    ],

    "Software Tester": [
        ("Software Testing", "YouTube Tutorials"),
        ("SDLC / STLC", "YouTube Tutorials"),
        ("Manual Testing", "YouTube Tutorials"),
        ("Test Cases", "YouTube Tutorials"),
        ("Bug Reporting", "YouTube Tutorials"),
        ("Automation Testing", "YouTube Tutorials")
    ],

    "Teacher": [
        ("Communication", "YouTube / Online Courses"),
        ("Subject Knowledge", "Books / YouTube Tutorials"),
        ("Teaching Methods", "YouTube / Online Courses"),
        ("Lesson Planning", "YouTube Tutorials"),
        ("Presentation", "YouTube Tutorials"),
        ("Classroom Management", "YouTube / Online Courses")
    ],

    "Database Administrator": [
        ("Database Concepts", "W3Schools / YouTube Tutorials"),
        ("SQL", "W3Schools / YouTube Tutorials"),
        ("MySQL", "YouTube Tutorials / W3Schools"),
        ("Database Security", "YouTube Tutorials"),
        ("Backup and Recovery", "YouTube Tutorials"),
        ("Linux", "YouTube Tutorials")
    ],

    "Business Analyst": [
        ("Business Analysis", "YouTube / Online Courses"),
        ("Communication", "YouTube / Online Courses"),
        ("Excel", "YouTube Tutorials / Microsoft Learn"),
        ("SQL", "W3Schools / YouTube Tutorials"),
        ("Data Visualization", "YouTube Tutorials"),
        ("Requirement Analysis", "YouTube / Online Courses")
    ],

    "UI/UX Designer": [
        ("UI/UX Fundamentals", "YouTube Tutorials"),
        ("User Research", "YouTube / Online Courses"),
        ("Wireframing", "YouTube Tutorials"),
        ("Figma", "YouTube Tutorials"),
        ("Prototyping", "YouTube Tutorials"),
        ("Design Portfolio", "YouTube Tutorials")
    ],

    "Cybersecurity Analyst": [
        ("Networking", "YouTube Tutorials"),
        ("Operating Systems", "YouTube Tutorials"),
        ("Cybersecurity", "YouTube / Online Courses"),
        ("Security Tools", "YouTube Tutorials"),
        ("Ethical Hacking", "YouTube / Online Courses"),
        ("Security Labs", "YouTube Tutorials")
    ],

    "AI/ML Engineer": [
        ("Python", "W3Schools / YouTube Tutorials"),
        ("Mathematics", "Khan Academy / YouTube"),
        ("Statistics", "Khan Academy"),
        ("Machine Learning", "YouTube / Online Courses"),
        ("Data Processing", "YouTube Tutorials"),
        ("Deep Learning", "YouTube / Online Courses")
    ]
}


# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


# =====================================================
# REGISTER
# =====================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        cursor = db.cursor(buffered=True)

        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (%s, %s, %s)
        """, (name, email, password))

        db.commit()

        return redirect("/")

    return render_template("register.html")


# =====================================================
# LOGIN
# =====================================================

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT *
        FROM users
        WHERE email = %s AND password = %s
    """, (email, password))

    user = cursor.fetchone()

    if user:

        session["user_id"] = user[0]
        session["user_name"] = user[1]

        return redirect("/dashboard")

    return "Invalid email or password"


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    user_name = session.get("user_name")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT skills
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    has_profile = False
    suggested_career = ""
    match_count = 0
    total_skills = 6
    match_percentage = 0

    if profile_data:

        has_profile = True

        user_skills = (profile_data[0] or "").lower()

        career_scores = {}

        for career_name, required_skills in profession_skills.items():

            score = 0

            for skill in required_skills:

                if skill in user_skills:
                    score += 1

            career_scores[career_name] = score

        suggested_career = max(
            career_scores,
            key=career_scores.get
        )

        match_count = career_scores[suggested_career]

        total_skills = len(
            profession_skills[suggested_career]
        )

        match_percentage = round(
            (match_count / total_skills) * 100
        )

    return render_template(
        "dashboard.html",
        user_name=user_name,
        has_profile=has_profile,
        suggested_career=suggested_career,
        match_count=match_count,
        total_skills=total_skills,
        match_percentage=match_percentage
    )


# =====================================================
# CREATE PROFILE
# =====================================================

@app.route("/profile", methods=["GET", "POST"])
def profile():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    if request.method == "POST":

        education = request.form["education"]
        phone = request.form["phone"]
        skills = request.form["skills"]
        experience = request.form["experience"]
        summary = request.form["summary"]

        cursor = db.cursor(buffered=True)

        cursor.execute("""
            INSERT INTO profiles
            (user_id, education, phone, skills, experience, summary)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            user_id,
            education,
            phone,
            skills,
            experience,
            summary
        ))

        cursor.execute("""
            INSERT INTO activity
            (user_id, activity)
            VALUES (%s, %s)
        """, (
            user_id,
            "Profile Created"
        ))

        db.commit()

        return redirect("/dashboard")

    return render_template("profile.html")


# =====================================================
# EDIT PROFILE
# =====================================================

@app.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    if request.method == "POST":

        education = request.form["education"]
        phone = request.form["phone"]
        skills = request.form["skills"]
        experience = request.form["experience"]
        summary = request.form["summary"]

        cursor.execute("""
            SELECT id
            FROM profiles
            WHERE user_id = %s
            ORDER BY id DESC
            LIMIT 1
        """, (user_id,))

        profile_data = cursor.fetchone()

        if profile_data:

            cursor.execute("""
                UPDATE profiles
                SET education = %s,
                    phone = %s,
                    skills = %s,
                    experience = %s,
                    summary = %s
                WHERE id = %s
            """, (
                education,
                phone,
                skills,
                experience,
                summary,
                profile_data[0]
            ))

        else:

            cursor.execute("""
                INSERT INTO profiles
                (user_id, education, phone, skills, experience, summary)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                user_id,
                education,
                phone,
                skills,
                experience,
                summary
            ))

        cursor.execute("""
            INSERT INTO activity
            (user_id, activity)
            VALUES (%s, %s)
        """, (
            user_id,
            "Profile Updated"
        ))

        db.commit()

        return redirect("/dashboard")

    cursor.execute("""
        SELECT education, phone, skills, experience, summary
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    return render_template(
        "edit_profile.html",
        profile=profile_data
    )


# =====================================================
# RESUME
# =====================================================

@app.route("/resume", methods=["GET", "POST"])
def resume():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        objective = request.form["objective"]
        education = request.form["education"]
        skills = request.form["skills"]
        experience = request.form["experience"]
        projects = request.form["projects"]
        certifications = request.form["certifications"]

        cursor = db.cursor(buffered=True)

        cursor.execute("""
            INSERT INTO activity
            (user_id, activity)
            VALUES (%s, %s)
        """, (
            user_id,
            "Resume Created"
        ))

        db.commit()

        return render_template(
            "resume_preview.html",
            name=name,
            email=email,
            phone=phone,
            objective=objective,
            education=education,
            skills=skills,
            experience=experience,
            projects=projects,
            certifications=certifications
        )

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT name, email
        FROM users
        WHERE id = %s
    """, (user_id,))

    user = cursor.fetchone()

    return render_template(
        "resume.html",
        user=user
    )


# =====================================================
# CAREER GUIDANCE / CAREER SUGGESTION
# =====================================================

@app.route("/analyze")
def analyze():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT skills, experience, summary
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    skills = (profile_data[0] or "").lower()

    available_skills = []

    for skill_list in profession_skills.values():

        for skill in skill_list:

            if skill in skills and skill.title() not in available_skills:
                available_skills.append(skill.title())

    career_scores = {}

    for profession, required_skills in profession_skills.items():

        score = 0

        for skill in required_skills:

            if skill in skills:
                score += 1

        career_scores[profession] = score

    career_name = max(
        career_scores,
        key=career_scores.get
    )

    match_count = career_scores[career_name]

    missing_skills = []

    for skill in profession_skills[career_name]:

        if skill not in skills:
            missing_skills.append(skill.title())

    cursor.execute("""
        INSERT INTO activity
        (user_id, activity)
        VALUES (%s, %s)
    """, (
        user_id,
        "Career Analysis Checked"
    ))

    db.commit()

    return render_template(
        "analysis.html",
        available_skills=available_skills,
        missing_skills=missing_skills,
        career=career_name,
        careers=list(profession_skills.keys()),
        match_count=match_count
    )


# =====================================================
# SKILL GAP ANALYSIS
# =====================================================

@app.route("/skill-gap")
def skill_gap():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT skills
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    user_skills = (profile_data[0] or "").lower()

    career_scores = {}

    for career_name, required_skills in profession_skills.items():

        score = 0

        for skill in required_skills:

            if skill in user_skills:
                score += 1

        career_scores[career_name] = score

    selected_career = max(
        career_scores,
        key=career_scores.get
    )

    required_skills = profession_skills[selected_career]

    available_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in user_skills:
            available_skills.append(skill.title())
        else:
            missing_skills.append(skill.title())

    return render_template(
        "skill_gap.html",
        selected_career=selected_career,
        available_skills=available_skills,
        missing_skills=missing_skills
    )


# =====================================================
# CAREER COMPARISON
# =====================================================

@app.route("/career-comparison")
def career_comparison():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT skills
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    user_skills = (profile_data[0] or "").lower()

    comparisons = {}

    for career_name, required_skills in profession_skills.items():

        matching_skills = []

        for skill in required_skills:

            if skill in user_skills:
                matching_skills.append(skill.title())

        total_skills = len(required_skills)
        match_count = len(matching_skills)

        percentage = round(
            (match_count / total_skills) * 100
        )

        comparisons[career_name] = {
            "matching_skills": matching_skills,
            "match_count": match_count,
            "total_skills": total_skills,
            "percentage": percentage
        }

    return render_template(
        "career_comparison.html",
        comparisons=comparisons
    )


# =====================================================
# LEARNING RESOURCES
# =====================================================

@app.route("/learning-resources")
def learning_resources():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT id
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    return render_template(
        "learning_resources.html",
        learning_resources=learning_resources_data
    )


# =====================================================
# CAREER ROADMAP
# =====================================================

@app.route("/career")
def career():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT id
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    selected_career = request.args.get(
        "career",
        "Data Analyst"
    )

    roadmap = roadmaps.get(
        selected_career,
        roadmaps["Data Analyst"]
    )

    return render_template(
        "career.html",
        roadmap=roadmap,
        selected_career=selected_career
    )


# =====================================================
# COMPLETE ROADMAP STEP
# =====================================================

@app.route("/complete", methods=["POST"])
def complete():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    step = request.form["step"]
    selected_career = request.form["career"]

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        INSERT INTO progress
        (user_id, step, status)
        VALUES (%s, %s, %s)
    """, (
        user_id,
        step,
        "Completed"
    ))

    db.commit()

    return redirect(
        "/progress/" + selected_career
    )


# =====================================================
# PROGRESS TRACKING
# =====================================================

@app.route("/progress/<path:selected_career>")
def progress(selected_career):

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT id
        FROM profiles
        WHERE user_id = %s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    profile_data = cursor.fetchone()

    if not profile_data:
        return redirect("/profile")

    roadmap = roadmaps.get(
        selected_career,
        roadmaps["Data Analyst"]
    )

    cursor.execute("""
        SELECT step
        FROM progress
        WHERE user_id = %s
        AND status = 'Completed'
    """, (user_id,))

    completed_steps = [
        row[0]
        for row in cursor.fetchall()
    ]

    return render_template(
        "progress.html",
        roadmap=roadmap,
        completed_steps=completed_steps,
        selected_career=selected_career
    )


# =====================================================
# ADMIN LOGIN
# =====================================================

@app.route("/admin", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor(buffered=True)

        cursor.execute("""
            SELECT id
            FROM admin
            WHERE username = %s AND password = %s
        """, (username, password))

        admin = cursor.fetchone()

        if admin:
            session["admin"] = True
            session["admin_id"] = admin[0]

            return redirect("/admin/dashboard")

        else:
            return render_template(
                "admin_login.html",
                error="Invalid username or password"
            )

    return render_template("admin_login.html")
# =====================================================
# ADMIN DASHBOARD
# =====================================================

@app.route("/admin/dashboard")
def admin_dashboard():

    if not session.get("admin"):
        return redirect("/admin")

    cursor = db.cursor(buffered=True)

    # Total users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Total profiles
    cursor.execute("SELECT COUNT(*) FROM profiles")
    total_profiles = cursor.fetchone()[0]

    # Recent users
    cursor.execute("""
        SELECT id, name, email
        FROM users
        ORDER BY id DESC
    """)
    users = cursor.fetchall()

    # User activities
    cursor.execute("""
        SELECT 
            activity.id,
            users.name,
            users.email,
            activity.activity,
            activity.activity_time
        FROM activity
        JOIN users ON activity.user_id = users.id
        ORDER BY activity.activity_time DESC
    """)
    activities = cursor.fetchall()

    return render_template(
        "admin_dashboard.html",
        total_users=total_users,
        total_profiles=total_profiles,
        users=users,
        activities=activities
    )

@app.route("/admin/users")
def admin_users():

    if not session.get("admin"):
        return redirect("/admin")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT id, name, email
        FROM users
        ORDER BY id DESC
    """)

    users = cursor.fetchall()

    return render_template(
        "admin_users.html",
        users=users
    )

@app.route("/admin/profiles")
def admin_profiles():
    if not session.get("admin"):
        return redirect("/admin")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT users.name,
               users.email,
               profiles.education,
               profiles.phone,
               profiles.skills,
               profiles.experience
        FROM profiles
        JOIN users ON profiles.user_id = users.id
        ORDER BY profiles.id DESC
    """)

    profiles = cursor.fetchall()

    return render_template(
        "admin_profiles.html",
        profiles=profiles
    )
@app.route("/admin/resumes")
def admin_resumes():
    if not session.get("admin"):
        return redirect("/admin")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT users.name,
               users.email,
               profiles.education,
               profiles.skills,
               profiles.experience,
               profiles.summary
        FROM profiles
        JOIN users ON profiles.user_id = users.id
        ORDER BY profiles.id DESC
    """)

    resumes = cursor.fetchall()

    return render_template(
        "admin_resumes.html",
        resumes=resumes
    )

@app.route("/admin/career-suggestions")
def admin_career_suggestions():
    if not session.get("admin"):
        return redirect("/admin")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT users.name,
               users.email,
               profiles.skills
        FROM profiles
        JOIN users ON profiles.user_id = users.id
        ORDER BY profiles.id DESC
    """)

    users = cursor.fetchall()

    suggestions = []

    for user in users:

        name = user[0]
        email = user[1]
        skills = (user[2] or "").lower()

        career_scores = {}

        for career_name, required_skills in profession_skills.items():

            score = 0

            for skill in required_skills:
                if skill.lower() in skills:
                    score += 1

            career_scores[career_name] = score

        suggested_career = max(
            career_scores,
            key=career_scores.get
        )

        suggestions.append(
            (name, email, suggested_career)
        )

    return render_template(
        "admin_career_suggestions.html",
        suggestions=suggestions
    )

@app.route("/admin/activities")
def admin_activities():

    if not session.get("admin"):
        return redirect("/admin")

    cursor = db.cursor(buffered=True)

    cursor.execute("""
        SELECT
            users.name,
            users.email,
            activity.activity,
            activity.activity_time
        FROM activity
        JOIN users
        ON activity.user_id = users.id
        ORDER BY activity.activity_time DESC
    """)

    activities = cursor.fetchall()

    return render_template(
        "admin_activities.html",
        activities=activities
    )

# =====================================================
# LOGOUT
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =====================================================
# RUN
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)