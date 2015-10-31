from django.test import TestCase
from candidate.models import Candidate
# Create your tests here.
class CandidateTestClass(TestCase):
    def setUp(self):
        #Objeto Valido
        Candidate.objects.create(fullname="Alexandre Sebrao", email="alexandre.sebrao@gmail.com", html_grade="7", css_grade="3", javascript_grade = "10", python_grade="8", django_grade = "10", ios_grade="10", android_grade="6"  )

    def test_candidate(self):
        alexandresebrao = Candidate.objects.get(fullname="Alexandre Sebrao")

        self.assertEqual(alexandresebrao.fullname, 'Alexandre Sebrao')
        self.assertEqual(alexandresebrao.email, 'alexandre.sebrao@gmail.com')
        self.assertEqual(alexandresebrao.html_grade, 7)
        self.assertEqual(alexandresebrao.css_grade, 3)
        self.assertEqual(alexandresebrao.javascript_grade, 10)
        self.assertNotEqual(alexandresebrao.python_grade, 11)
        self.assertEqual(alexandresebrao.python_grade, 8)
        self.assertEqual(alexandresebrao.django_grade, 10)
        self.assertEqual(alexandresebrao.ios_grade, 10)
        self.assertEqual(alexandresebrao.android_grade, 6)
