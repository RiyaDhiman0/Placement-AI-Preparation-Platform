# 🎯 PlacementPro - AI-Powered Placement Preparation Portal

A comprehensive web application designed to help students prepare for campus placements with technical interview practice, soft skills training, aptitude tests, mock interviews, previous year questions, AI-powered feedback, and personalized study roadmaps.

---

## ✨ Features

### ✅ Technical Interview Preparation
- 15+ questions covering Data Structures, Algorithms, OOP, Databases, Operating Systems, Networks, and System Design
- Topic-wise filtering and random question generation
- Keyword-based answer scoring with model answers

### ✅ Soft Skills Improvement
- 12 real-world workplace scenarios across 5 categories: Communication, Teamwork, Leadership, Problem Solving, Adaptability
- AI-powered response evaluation with scoring and feedback
- Key points to cover for each scenario

### ✅ Aptitude Tests
- 15 quantitative aptitude questions across categories (Speed & Distance, Probability, Work & Time, etc.)
- Random 10-question tests with multiple choice options
- Instant scoring with detailed result breakdown

### ✅ Mock Interviews
- Simulated 5-question interviews (3 Technical + 2 HR)
- Per-question scoring based on keyword matching
- Overall grade (A/B/C/D) with detailed feedback

### ✅ Previous Year Placement Questions
- 12 questions from Google, Microsoft, Amazon, Meta (2023-2024)
- Filter by company and year
- Answer hints for each question

### ✅ AI-Powered Feedback & Scoring
- Analyzes answers for Clarity, Depth, and Relevance
- Color-coded score visualization (Green/Yellow/Orange/Red)
- Actionable suggestions for improvement
- Answer statistics (word count, characters, sentences)

### ✅ Personalized Preparation Roadmap
- Generates a 3-phase study plan based on:
  - Target role (Software Engineer, Data Scientist, etc.)
  - Experience level (Beginner/Intermediate/Advanced)
  - Time available (1/2/3 months)
  - Weak areas (multi-select)
- Daily schedule for each phase
- Success tips and weak area focus recommendations

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask (installed automatically)

### Installation

```bash
# Navigate to the project directory
cd "C:\Users\Riyadhiman\OneDrive\Documents\PlacementPro"

# Install Flask (if not already installed)
pip install flask

# Run the application
python app.py
```

### Access the Application
Open your browser and go to: **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
PlacementPro/
├── app.py                    # Flask backend with all API routes
├── test_app.py               # Automated test suite
├── README.md                 # Project documentation
├── data/
│   ├── questions.json        # Technical, aptitude & previous year questions
│   └── soft_skills.json      # Soft skills scenarios
├── templates/                # HTML templates (Jinja2)
│   ├── base.html             # Navigation & layout template
│   ├── index.html            # Landing page with login
│   ├── dashboard.html        # User dashboard with stats & progress
│   ├── technical.html        # Technical Q&A practice
│   ├── soft_skills.html      # Scenario-based practice
│   ├── aptitude.html         # Multiple choice tests
│   ├── mock_interview.html   # Full interview simulation
│   ├── previous_questions.html # Filterable company questions
│   ├── ai_feedback.html      # AI answer analysis
│   └── roadmap.html          # Personalized study planner
├── static/
│   ├── css/
│   │   └── style.css         # Modern responsive UI (700+ lines)
│   └── js/
│       └── main.js           # Navigation & interactivity
```

---

## 🧪 Running Tests

```bash
python test_app.py
```

The test suite validates:
- ✅ Landing page loads correctly
- ✅ Login functionality
- ✅ Technical question API
- ✅ Aptitude test generation
- ✅ Soft skills scenarios
- ✅ AI feedback analysis
- ✅ Roadmap generation
- ✅ Previous questions filtering
- ✅ Mock interview system
- ✅ Answer checking
- ✅ Page route redirects

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Backend programming language |
| **Flask** | Web framework (routing, sessions, APIs) |
| **Jinja2** | Template engine for HTML rendering |
| **HTML5/CSS3** | Frontend structure and styling |
| **JavaScript** | Client-side interactivity and API calls |
| **Font Awesome** | Icons and visual elements |
| **Google Fonts** | Typography (Inter font family) |

---

## 🎨 UI/UX Highlights

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern Gradient Theme**: Purple/teal color scheme with glassmorphism effects
- **Animated Elements**: Progress rings, score bars, floating icons
- **Interactive Feedback**: Real-time scoring with color-coded results
- **Smooth Navigation**: Fixed navbar with hamburger menu for mobile

---

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page |
| `/login` | POST | User login |
| `/dashboard` | GET | User dashboard |
| `/technical` | GET | Technical prep page |
| `/api/technical/random` | GET | Random technical question |
| `/api/technical/check` | POST | Check technical answer |
| `/soft-skills` | GET | Soft skills page |
| `/api/soft-skills/scenario` | GET | Random scenario |
| `/api/soft-skills/evaluate` | POST | Evaluate soft skills response |
| `/aptitude` | GET | Aptitude test page |
| `/api/aptitude/start` | GET | Start aptitude test |
| `/api/aptitude/submit` | POST | Submit aptitude test |
| `/mock-interview` | GET | Mock interview page |
| `/api/mock-interview/start` | GET | Start mock interview |
| `/api/mock-interview/evaluate` | POST | Evaluate interview |
| `/previous-questions` | GET | Previous questions page |
| `/api/previous-questions/filter` | GET | Filter previous questions |
| `/ai-feedback` | GET | AI feedback page |
| `/api/ai-feedback/analyze` | POST | Analyze answer |
| `/roadmap` | GET | Roadmap page |
| `/api/roadmap/generate` | POST | Generate roadmap |
| `/api/progress/save` | POST | Save user progress |
| `/api/progress/load` | GET | Load user progress |

---

## 📝 License

This project is created for educational purposes to help students prepare for campus placements.

---

## 🤝 Contributing

Feel free to fork this project, add more questions, improve the UI, or enhance the AI feedback algorithms. Contributions are welcome!

---

*Made with ❤️ for placement preparation*