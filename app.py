import os
import json
import random
import datetime
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "placement_portal_secret_key_2026"

# ============================================================
# DATA LOADING
# ============================================================

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("dashboard.html", username=session["username"])

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "Student")
    session["username"] = username
    return jsonify({"success": True, "username": username})

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# ============================================================
# TECHNICAL INTERVIEW PREPARATION
# ============================================================

@app.route("/technical")
def technical():
    if "username" not in session:
        return redirect(url_for("index"))
    questions = load_json("questions.json")
    return render_template("technical.html", questions=questions)

@app.route("/api/technical/random")
def technical_random():
    questions = load_json("questions.json")
    topic = request.args.get("topic", "all")
    if topic != "all":
        filtered = [q for q in questions["technical"] if q["topic"] == topic]
    else:
        filtered = questions["technical"]
    if not filtered:
        return jsonify({"error": "No questions found"}), 404
    q = random.choice(filtered)
    return jsonify(q)

@app.route("/api/technical/check", methods=["POST"])
def technical_check():
    data = request.get_json()
    user_answer = data.get("answer", "").strip().lower()
    correct_answer = data.get("correct_answer", "").strip().lower()
    keywords = data.get("keywords", [])
    
    score = 0
    for kw in keywords:
        if kw.lower() in user_answer:
            score += 1
    
    max_score = len(keywords) if keywords else 1
    percentage = int((score / max_score) * 100) if max_score > 0 else 0
    
    is_correct = percentage >= 60 or user_answer == correct_answer
    
    return jsonify({
        "is_correct": is_correct,
        "score": percentage,
        "feedback": "Great answer!" if is_correct else "Review the correct answer and try again."
    })

# ============================================================
# SOFT SKILLS IMPROVEMENT
# ============================================================

@app.route("/soft-skills")
def soft_skills():
    if "username" not in session:
        return redirect(url_for("index"))
    scenarios = load_json("soft_skills.json")
    return render_template("soft_skills.html", scenarios=scenarios)

@app.route("/api/soft-skills/scenario")
def soft_skills_scenario():
    scenarios = load_json("soft_skills.json")
    category = request.args.get("category", "all")
    if category != "all":
        filtered = [s for s in scenarios if s["category"] == category]
    else:
        filtered = scenarios
    if not filtered:
        return jsonify({"error": "No scenarios found"}), 404
    s = random.choice(filtered)
    return jsonify(s)

@app.route("/api/soft-skills/evaluate", methods=["POST"])
def soft_skills_evaluate():
    data = request.get_json()
    user_response = data.get("response", "").strip()
    tips = data.get("tips", [])
    
    word_count = len(user_response.split())
    tips_mentioned = sum(1 for tip in tips if tip.lower() in user_response.lower())
    
    if word_count < 5:
        score = 20
        feedback = "Your response is too brief. Try to elaborate more."
    elif tips_mentioned >= len(tips) * 0.5:
        score = 85 + tips_mentioned * 5
        feedback = "Excellent response! You covered key points well."
    elif tips_mentioned > 0:
        score = 50 + tips_mentioned * 10
        feedback = "Good start! Try to include more key points in your response."
    else:
        score = 30
        feedback = "Consider reviewing the tips and incorporating them into your response."
    
    score = min(score, 100)
    
    return jsonify({
        "score": score,
        "word_count": word_count,
        "feedback": feedback
    })

# ============================================================
# APTITUDE TESTS
# ============================================================

@app.route("/aptitude")
def aptitude():
    if "username" not in session:
        return redirect(url_for("index"))
    questions = load_json("questions.json")
    return render_template("aptitude.html", questions=questions["aptitude"])

@app.route("/api/aptitude/start")
def aptitude_start():
    questions = load_json("questions.json")
    apt_questions = questions["aptitude"]
    selected = random.sample(apt_questions, min(10, len(apt_questions)))
    session["aptitude_answers"] = {q["id"]: q["answer"] for q in selected}
    return jsonify({"questions": selected, "total": len(selected)})

@app.route("/api/aptitude/submit", methods=["POST"])
def aptitude_submit():
    data = request.get_json()
    answers = data.get("answers", {})
    correct_answers = session.get("aptitude_answers", {})
    
    correct_count = 0
    total = len(correct_answers)
    results = []
    
    for qid, correct in correct_answers.items():
        user_ans = answers.get(qid, "")
        is_correct = user_ans == correct
        if is_correct:
            correct_count += 1
        results.append({
            "id": qid,
            "user_answer": user_ans,
            "correct_answer": correct,
            "is_correct": is_correct
        })
    
    percentage = int((correct_count / total) * 100) if total > 0 else 0
    
    return jsonify({
        "score": correct_count,
        "total": total,
        "percentage": percentage,
        "results": results,
        "passed": percentage >= 60
    })

# ============================================================
# MOCK INTERVIEWS
# ============================================================

@app.route("/mock-interview")
def mock_interview():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("mock_interview.html")

@app.route("/api/mock-interview/start")
def mock_interview_start():
    questions = load_json("questions.json")
    tech_questions = questions["technical"]
    hr_questions = load_json("soft_skills.json")
    
    interview_questions = []
    
    # Pick 3 technical questions
    tech_selected = random.sample(tech_questions, min(3, len(tech_questions)))
    for q in tech_selected:
        interview_questions.append({
            "type": "technical",
            "question": q["question"],
            "topic": q["topic"],
            "keywords": q.get("keywords", []),
            "correct_answer": q["answer"]
        })
    
    # Pick 2 HR questions
    hr_selected = random.sample(hr_questions, min(2, len(hr_questions)))
    for q in hr_selected:
        interview_questions.append({
            "type": "hr",
            "question": q["scenario"],
            "category": q["category"],
            "tips": q.get("tips", []),
            "correct_answer": q.get("ideal_response", "")
        })
    
    random.shuffle(interview_questions)
    session["mock_questions"] = interview_questions
    session["mock_index"] = 0
    
    return jsonify({
        "questions": interview_questions,
        "total": len(interview_questions)
    })

@app.route("/api/mock-interview/evaluate", methods=["POST"])
def mock_interview_evaluate():
    data = request.get_json()
    answers = data.get("answers", [])
    questions = session.get("mock_questions", [])
    
    total_score = 0
    max_score = len(questions) * 100
    feedback_list = []
    
    for i, q in enumerate(questions):
        user_ans = answers[i] if i < len(answers) else ""
        word_count = len(user_ans.split())
        
        if q["type"] == "technical":
            keywords = q.get("keywords", [])
            score = sum(1 for kw in keywords if kw.lower() in user_ans.lower())
            score = int((score / len(keywords)) * 100) if keywords else 50
            if word_count < 5:
                score = max(score - 30, 0)
        else:
            tips = q.get("tips", [])
            score = sum(1 for tip in tips if tip.lower() in user_ans.lower())
            score = int((score / len(tips)) * 100) if tips else 50
            if word_count < 10:
                score = max(score - 20, 0)
        
        total_score += score
        feedback_list.append({
            "question": q["question"],
            "type": q["type"],
            "score": score,
            "word_count": word_count,
            "feedback": "Excellent!" if score >= 80 else "Good, but could improve." if score >= 50 else "Needs improvement."
        })
    
    overall = int(total_score / max_score * 100) if max_score > 0 else 0
    
    return jsonify({
        "overall_score": overall,
        "feedback": feedback_list,
        "total_questions": len(questions),
        "grade": "A" if overall >= 80 else "B" if overall >= 60 else "C" if overall >= 40 else "D"
    })

# ============================================================
# PREVIOUS YEAR PLACEMENT QUESTIONS
# ============================================================

@app.route("/previous-questions")
def previous_questions():
    if "username" not in session:
        return redirect(url_for("index"))
    questions = load_json("questions.json")
    return render_template("previous_questions.html", questions=questions["previous_year"])

@app.route("/api/previous-questions/filter")
def previous_questions_filter():
    questions = load_json("questions.json")
    company = request.args.get("company", "all")
    year = request.args.get("year", "all")
    
    filtered = questions["previous_year"]
    if company != "all":
        filtered = [q for q in filtered if q["company"].lower() == company.lower()]
    if year != "all":
        filtered = [q for q in filtered if str(q["year"]) == year]
    
    return jsonify({"questions": filtered, "count": len(filtered)})

# ============================================================
# AI FEEDBACK AND SCORING
# ============================================================

@app.route("/ai-feedback")
def ai_feedback():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("ai_feedback.html")

@app.route("/api/ai-feedback/analyze", methods=["POST"])
def ai_feedback_analyze():
    data = request.get_json()
    answer = data.get("answer", "")
    question_type = data.get("type", "general")
    
    word_count = len(answer.split())
    sentences = len([s for s in answer.split(".") if s.strip()])
    avg_word_length = sum(len(w) for w in answer.split()) / max(word_count, 1)
    
    # Analyze quality
    clarity_score = min(100, int((sentences / max(word_count / 10, 1)) * 20))
    depth_score = min(100, int(word_count * 2))
    relevance_score = 75  # Default relevance
    
    if question_type == "technical":
        depth_score = min(100, int(word_count * 3))
        if any(kw in answer.lower() for kw in ["algorithm", "complexity", "data structure", "function", "class", "object"]):
            relevance_score += 15
    elif question_type == "hr":
        clarity_score = min(100, int((sentences / max(word_count / 8, 1)) * 25))
        if any(kw in answer.lower() for kw in ["team", "experience", "learn", "skill", "project"]):
            relevance_score += 15
    
    overall = int((clarity_score + depth_score + relevance_score) / 3)
    
    suggestions = []
    if word_count < 20:
        suggestions.append("Provide a more detailed response with specific examples.")
    if sentences < 3:
        suggestions.append("Structure your answer into multiple sentences for better clarity.")
    if avg_word_length > 7:
        suggestions.append("Try using simpler words for better communication.")
    if clarity_score < 50:
        suggestions.append("Focus on making your response clearer and more structured.")
    if depth_score < 50:
        suggestions.append("Add more technical depth and specific details to your answer.")
    
    return jsonify({
        "overall_score": overall,
        "clarity": clarity_score,
        "depth": depth_score,
        "relevance": relevance_score,
        "word_count": word_count,
        "suggestions": suggestions,
        "grade": "Excellent" if overall >= 80 else "Good" if overall >= 60 else "Average" if overall >= 40 else "Needs Improvement"
    })

# ============================================================
# PERSONALIZED PREPARATION ROADMAP
# ============================================================

@app.route("/roadmap")
def roadmap():
    if "username" not in session:
        return redirect(url_for("index"))
    return render_template("roadmap.html")

@app.route("/api/roadmap/generate", methods=["POST"])
def roadmap_generate():
    data = request.get_json()
    target_role = data.get("role", "Software Engineer")
    experience = data.get("experience", "beginner")
    time_available = data.get("time", "3 months")
    weak_areas = data.get("weak_areas", [])
    
    weeks = 12 if time_available == "3 months" else 8 if time_available == "2 months" else 4
    
    roadmap = {
        "target_role": target_role,
        "experience_level": experience,
        "duration": time_available,
        "total_weeks": weeks,
        "phases": []
    }
    
    # Phase 1: Foundation
    phase1_weeks = max(2, weeks // 4)
    phase1 = {
        "name": "Foundation Building",
        "duration": f"{phase1_weeks} weeks",
        "focus": "Core Concepts & Fundamentals",
        "tasks": [
            "Review basic data structures (Arrays, Linked Lists, Stacks, Queues)",
            "Master time & space complexity analysis",
            "Practice basic algorithms (Sorting, Searching, Recursion)",
            "Strengthen OOP concepts and principles",
            "Start daily aptitude practice (15-20 questions)"
        ],
        "daily_schedule": {
            "morning": "2 hours - Data Structures & Algorithms",
            "afternoon": "1 hour - Aptitude Practice",
            "evening": "1 hour - Communication Skills"
        }
    }
    
    # Phase 2: Advanced Topics
    phase2_weeks = max(2, weeks // 3)
    phase2 = {
        "name": "Advanced Preparation",
        "duration": f"{phase2_weeks} weeks",
        "focus": "Advanced Topics & Problem Solving",
        "tasks": [
            "Study advanced data structures (Trees, Graphs, Hash Tables)",
            "Practice dynamic programming problems",
            "Learn system design basics",
            "Solve previous year company questions",
            "Participate in mock interviews"
        ],
        "daily_schedule": {
            "morning": "2 hours - Advanced DSA Problems",
            "afternoon": "1.5 hours - Company-Specific Questions",
            "evening": "1 hour - Soft Skills & HR Preparation"
        }
    }
    
    # Phase 3: Interview Preparation
    phase3_weeks = weeks - phase1_weeks - phase2_weeks
    phase3 = {
        "name": "Interview Ready",
        "duration": f"{phase3_weeks} weeks",
        "focus": "Mock Interviews & Final Preparation",
        "tasks": [
            "Take full-length mock interviews (at least 3 per week)",
            "Review and analyze interview performance",
            "Practice coding on whiteboard/notepad",
            "Prepare for HR and behavioral questions",
            "Revise all concepts and weak areas"
        ],
        "daily_schedule": {
            "morning": "2 hours - Mock Interviews & Review",
            "afternoon": "1 hour - Company Research & Resume Prep",
            "evening": "1 hour - Relaxation & Confidence Building"
        }
    }
    
    roadmap["phases"] = [phase1, phase2, phase3]
    
    # Add weak area focus
    if weak_areas:
        roadmap["weak_area_focus"] = {
            "areas": weak_areas,
            "recommendation": f"Focus extra time on: {', '.join(weak_areas)}. Dedicate at least 30 minutes daily to these topics."
        }
    
    # Add company-specific tips
    roadmap["tips"] = [
        "Start each day with a coding problem to build consistency",
        "Maintain a preparation journal to track progress",
        "Join study groups or coding communities for motivation",
        "Take regular breaks to avoid burnout",
        "Practice explaining solutions out loud (important for interviews)",
        "Review and update your resume weekly",
        "Stay updated with industry trends and technologies"
    ]
    
    return jsonify(roadmap)

# ============================================================
# PROGRESS TRACKING
# ============================================================

@app.route("/api/progress/save", methods=["POST"])
def progress_save():
    data = request.get_json()
    session["progress"] = data
    return jsonify({"success": True})

@app.route("/api/progress/load")
def progress_load():
    progress = session.get("progress", {})
    return jsonify(progress)

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    app.run(debug=True, port=5000)