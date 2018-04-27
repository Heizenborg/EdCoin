class Course:
	def __init__(self, title, school, status):
		self.title = title
		self.school = school
		self.status = status

class CourseContract:
	def __init__(self, student, complete, courses):
		self.student = student
		self.complete = complete
		self.courses = courses

	def add_course(self, course):
		#returns contract with new course added
		return self.courses.append(course)

	def remove_course(self, course):
		if course in self.courses:
			return self.courses.remove(course)
		else:
			print("student was not enrolled in ", course)
