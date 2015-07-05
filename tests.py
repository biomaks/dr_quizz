import unittest
from app.views import QuestionList, Check
from app.models import Question, Answer

class TestQuestionList(unittest.TestCase):

    def setUp(self):
        self.question_list = QuestionList()

    def prepare_questions(self):
        questions_unsigned = []
        questions_signed = []
        for i in range(100):
            q_unsigned = Question(id=i, real_id=i, signed=False, question='This is question '+str(i))
            questions_unsigned.append(q_unsigned)
        for i in range(100):
            q_signed = Question(id=i, real_id=i, signed=True, sign_name='TestSignName'+str(i), question='This is question '+str(i))
            questions_signed.append(q_signed)
        return questions_signed, questions_unsigned

    def test_define_qty(self):
        defined5 = self.question_list.define_qty(5)
        defined10 = self.question_list.define_qty(10)
        defined20 = self.question_list.define_qty(20)
        defined40 = self.question_list.define_qty(40)
        self.assertTrue(defined5[0] == 1 and defined5 [1] == 4)
        self.assertTrue(defined10[0] == 4 and defined10 [1] == 6)
        self.assertTrue(defined20[0] == 7 and defined20 [1] == 13)
        self.assertTrue(defined40[0] == 10 and defined40 [1] == 30)

    def test_generate_random_numbers(self):
        count = 100
        qty = 10
        random_list = self.question_list.generate_random_numbers(count, qty)
        self.assertTrue(type(random_list) is list)
        self.assertEquals(len(random_list), 10)

    def test_get_questions(self):
        prepared_questions = self.prepare_questions()
        question_list = self.question_list.get_questions(20, (100,100), prepared_questions)
        self.assertEquals(len(question_list), 20)
        self.assertIsInstance(question_list[10], Question)

class TestCheck(unittest.TestCase):

    def setUp(self):
        self.check = Check()


if __name__ == '__main__':
    unittest.main()