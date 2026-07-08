import json
import urllib.request

BASE = "http://127.0.0.1:5000"

# Test landing page
print("=== Testing Landing Page ===")
f = urllib.request.urlopen(f"{BASE}/")
assert "PlacementPro" in f.read().decode()
print("✅ Landing page loads correctly")

# Test login
print("\n=== Testing Login ===")
req = urllib.request.Request(
    f"{BASE}/login",
    data=json.dumps({"username": "TestUser"}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)
f = urllib.request.urlopen(req)
data = json.loads(f.read())
assert data["success"] == True
print("✅ Login works correctly")

# Test technical random question
print("\n=== Testing Technical Questions ===")
f = urllib.request.urlopen(f"{BASE}/api/technical/random?topic=all")
data = json.loads(f.read())
assert "question" in data
assert "topic" in data
print(f"✅ Random question loaded: {data['topic']}")

# Test aptitude test
print("\n=== Testing Aptitude API ===")
f = urllib.request.urlopen(f"{BASE}/api/aptitude/start")
data = json.loads(f.read())
assert "questions" in data
assert data["total"] > 0
print(f"✅ Aptitude test started with {data['total']} questions")

# Test soft skills
print("\n=== Testing Soft Skills ===")
f = urllib.request.urlopen(f"{BASE}/api/soft-skills/scenario?category=all")
data = json.loads(f.read())
assert "scenario" in data
assert "category" in data
print(f"✅ Soft skills scenario loaded: {data['category']}")

# Test AI feedback
print("\n=== Testing AI Feedback ===")
req = urllib.request.Request(
    f"{BASE}/api/ai-feedback/analyze",
    data=json.dumps({"answer": "I have experience with Python and data structures. I worked on several projects.", "type": "technical"}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)
f = urllib.request.urlopen(req)
data = json.loads(f.read())
assert "overall_score" in data
assert "suggestions" in data
print(f"✅ AI feedback generated: score={data['overall_score']}%")

# Test roadmap
print("\n=== Testing Roadmap ===")
req = urllib.request.Request(
    f"{BASE}/api/roadmap/generate",
    data=json.dumps({"role": "Software Engineer", "experience": "beginner", "time": "3 months", "weak_areas": ["Algorithms"]}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)
f = urllib.request.urlopen(req)
data = json.loads(f.read())
assert "phases" in data
assert len(data["phases"]) == 3
print(f"✅ Roadmap generated for {data['target_role']} ({data['duration']})")

# Test previous questions filter
print("\n=== Testing Previous Questions ===")
f = urllib.request.urlopen(f"{BASE}/api/previous-questions/filter?company=Google&year=2024")
data = json.loads(f.read())
assert "questions" in data
print(f"✅ Filtered questions for Google 2024: {data['count']} found")

# Test mock interview
print("\n=== Testing Mock Interview ===")
f = urllib.request.urlopen(f"{BASE}/api/mock-interview/start")
data = json.loads(f.read())
assert "questions" in data
assert data["total"] == 5
print(f"✅ Mock interview started with {data['total']} questions")

# Test dashboard pages exist (redirect when not logged in)
print("\n=== Testing Page Routes ===")
pages = ["/technical", "/soft-skills", "/aptitude", "/mock-interview", "/previous-questions", "/ai-feedback", "/roadmap"]
for page in pages:
    req = urllib.request.Request(f"{BASE}{page}")
    f = urllib.request.urlopen(req)
    # Should not error out - should redirect to index page
    content = f.read().decode()
    assert "PlacementPro" in content, f"Page {page} should redirect to landing page"
print("✅ All page routes redirect correctly when not logged in")

# Test technical check
print("\n=== Testing Technical Answer Check ===")
req = urllib.request.Request(
    f"{BASE}/api/technical/check",
    data=json.dumps({
        "answer": "An array stores elements in contiguous memory while a linked list uses pointers",
        "correct_answer": "test",
        "keywords": ["contiguous", "pointers", "memory"]
    }).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)
f = urllib.request.urlopen(req)
data = json.loads(f.read())
assert "score" in data
assert "is_correct" in data
print(f"✅ Answer check works: score={data['score']}%")

print("\n" + "=" * 50)
print("🎉 ALL TESTS PASSED!")
print("=" * 50)