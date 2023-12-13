def gather_credits(credits_needed, *args):
    courses_enrolled = []
    earned_credits = 0
    for element in args:
        if earned_credits >= credits_needed:
            break
        course, course_credits = element
        if course not in courses_enrolled:
            courses_enrolled.append(course)
            earned_credits += course_credits
    if earned_credits >= credits_needed:
        return (f"Enrollment finished! Maximum credits: {earned_credits}.\n"
                f"Courses: {', '.join(sorted(courses_enrolled))}")
    return f"You need to enroll in more courses! You have to gather {credits_needed - earned_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


