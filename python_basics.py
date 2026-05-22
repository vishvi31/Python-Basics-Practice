"""
================================================================
  Python Basics Practice
  Author     : Vishvi
  Topics     : Variables, Conditionals, Loops,
               Functions, List Comprehensions, OOP
  Environment: Jupyter Notebook
================================================================
"""

# ──────────────────────────────────────────────────────────
# 1️⃣  VARIABLES & DATA TYPES
# ──────────────────────────────────────────────────────────
print("=" * 50)
print("1️⃣  VARIABLES & DATA TYPES")
print("=" * 50)

name       = "Vishvi"
age        = 23
gpa        = 8.9
is_student = True
skills     = ["Python", "SQL", "ML", "NLP"]

print(f"Name    : {name}  → {type(name)}")
print(f"Age     : {age}   → {type(age)}")
print(f"GPA     : {gpa}   → {type(gpa)}")
print(f"Student : {is_student} → {type(is_student)}")
print(f"Skills  : {skills} → {type(skills)}")


# ──────────────────────────────────────────────────────────
# 2️⃣  CONDITIONALS
# ──────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("2️⃣  CONDITIONALS")
print("=" * 50)

score = 78

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} → Grade: {grade}")

# One-liner conditional (ternary)
status = "Pass" if score >= 60 else "Fail"
print(f"Status : {status}")


# ──────────────────────────────────────────────────────────
# 3️⃣  LOOPS
# ──────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("3️⃣  LOOPS")
print("=" * 50)

# For loop
print("\nFor loop — skills:")
for i, skill in enumerate(skills, 1):
    print(f"  {i}. {skill}")

# While loop
print("\nWhile loop — countdown:")
n = 5
while n > 0:
    print(f"  {n}...")
    n -= 1
print("  🚀 Go!")

# Loop with break and continue
print("\nBreak & Continue — skip SQL, stop at ML:")
for skill in skills:
    if skill == "SQL":
        continue          # skip
    if skill == "ML":
        break             # stop
    print(f"  → {skill}")


# ──────────────────────────────────────────────────────────
# 4️⃣  FUNCTIONS
# ──────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("4️⃣  FUNCTIONS")
print("=" * 50)

def greet(name, role="Data Scientist"):
    """Return a greeting string."""
    return f"Hello, {name}! You are a {role}."

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI and return category."""
    bmi = weight_kg / (height_m ** 2)
    if   bmi < 18.5: category = "Underweight"
    elif bmi < 25.0: category = "Normal"
    elif bmi < 30.0: category = "Overweight"
    else:            category = "Obese"
    return round(bmi, 2), category

def factorial(n):
    """Recursive factorial."""
    return 1 if n <= 1 else n * factorial(n - 1)

print(greet("Vishvi"))
print(greet("Aditi", "ML Engineer"))

bmi, cat = calculate_bmi(60, 1.65)
print(f"BMI: {bmi} → {cat}")

print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")


# ──────────────────────────────────────────────────────────
# 5️⃣  LIST COMPREHENSIONS
# ──────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("5️⃣  LIST COMPREHENSIONS")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares   = [x**2 for x in numbers]
evens     = [x for x in numbers if x % 2 == 0]
even_sq   = [x**2 for x in numbers if x % 2 == 0]

print(f"Numbers  : {numbers}")
print(f"Squares  : {squares}")
print(f"Evens    : {evens}")
print(f"Even²    : {even_sq}")

# Dict comprehension
word_lengths = {word: len(word) for word in skills}
print(f"Lengths  : {word_lengths}")


# ──────────────────────────────────────────────────────────
# 6️⃣  OOP — Object Oriented Programming
# ──────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("6️⃣  OOP — Classes & Objects")
print("=" * 50)

class DataScientist:
    """Represents a Data Scientist with skills and projects."""

    # Class variable
    field = "Data Science & AI"

    def __init__(self, name, age, skills):
        """Initialise with name, age and skills list."""
        self.name    = name
        self.age     = age
        self.skills  = skills
        self.projects = []

    def add_project(self, project):
        """Add a completed project."""
        self.projects.append(project)
        print(f"  ✅ Project added: {project}")

    def introduce(self):
        """Print a professional introduction."""
        print(f"\n  👩‍💻 {self.name} | Age: {self.age}")
        print(f"  Field   : {self.field}")
        print(f"  Skills  : {', '.join(self.skills)}")
        print(f"  Projects: {len(self.projects)}")
        for p in self.projects:
            print(f"    • {p}")

    def skill_count(self):
        return len(self.skills)

    def __str__(self):
        return f"DataScientist({self.name}, {self.skill_count()} skills)"


# Inheritance
class MLEngineer(DataScientist):
    """ML Engineer extends DataScientist with model deployment skills."""

    def __init__(self, name, age, skills, frameworks):
        super().__init__(name, age, skills)
        self.frameworks = frameworks

    def introduce(self):
        super().introduce()
        print(f"  Frameworks: {', '.join(self.frameworks)}")


# ── Create objects ────────────────────────────────────────
vishvi = DataScientist(
    name   = "Vishvi",
    age    = 23,
    skills = ["Python", "SQL", "Machine Learning", "NLP", "Data Visualisation"]
)

vishvi.add_project("SyriaTel Customer Churn Prediction (AUC 0.898)")
vishvi.add_project("Disneyland Reviews Sentiment Analysis (NLP)")
vishvi.add_project("Titanic Survival Analysis (Logistic Regression)")
vishvi.add_project("GitHub Intelligence Dashboard (Flask + Claude API)")
vishvi.introduce()

print(f"\n  __str__ : {vishvi}")

# ML Engineer subclass
ml_eng = MLEngineer(
    name       = "Aditi",
    age        = 28,
    skills     = ["Python", "Deep Learning", "Computer Vision"],
    frameworks = ["TensorFlow", "PyTorch", "Keras"]
)
ml_eng.add_project("Image Classification Model (ResNet50)")
ml_eng.introduce()


print("\n" + "=" * 50)
print("  ✅ Python Basics complete!")
print("  🟩 Committed to GitHub — green square earned!")
print("=" * 50)
