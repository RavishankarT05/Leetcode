class Solution(object):
    def countStudents(self, students, sandwiches):
        while students:
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            elif students.count(sandwiches[0])==0:
                break
            else:
                students.append(students.pop(0))
        return len(students)