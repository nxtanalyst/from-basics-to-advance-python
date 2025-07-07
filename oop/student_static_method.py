'''Scenario: Student Report with Static Method Notice

In a school management system, each student’s average score in multiple subjects needs to be computed. The Stu class represents an individual student with their name and subject scores.

The average() method helps calculate the average score for reporting.

The hello() method is a static utility message, useful for testing or informational logging. Static methods like this are used when the method logic doesn't depend on instance-specific data.

This design keeps the average logic tied to the student while allowing shared utility methods via @staticmethod, such as logging or system checks, without needing to access student-specific data.

'''
class Stu:
    @staticmethod
    def hello():
        print('Checking My Static Method')

    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def average(self):
        return f'Average of: {sum(self.subject)/len(self.subject)}'

S3=Stu('Haroon',[10,12,14])
print(S3.average())
S3.hello()