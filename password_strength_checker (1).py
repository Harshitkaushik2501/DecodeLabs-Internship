"""
Project 1: Password Strength Checker
DecodeLabs Industrial Training Kit

Features:
- Input validation (Gatekeeper Rule)
- Password strength classification: Weak / Medium / Strong
- Checks:
    * Length
    * Uppercase letters
    * Lowercase letters
    * Numbers
    * Special characters
"""

import re


def validate_password(password: str) -> bool:
    """Basic input validation."""
    return isinstance(password, str) and len(password.strip()) > 0


def evaluate_password(password: str):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, feedback


def main():
    print("=" * 45)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("Enter password: ")

    if not validate_password(password):
        print("Invalid input. Password cannot be empty.")
        return

    strength, score, feedback = evaluate_password(password)

    print(f"\nStrength: {strength}")
    print(f"Score: {score}/6")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)


if __name__ == "__main__":
    main()
