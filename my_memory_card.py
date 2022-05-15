#создай приложение для запоминания информации
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QGroupBox, QButtonGroup,
    QHBoxLayout, QMessageBox, QRadioButton, QPushButton
)
from random import shuffle
from random import randint
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
question_list = []
question_list.append(Question("Какой государственный язык Бразилии?", "Португальский", "Латинский", "Испанский", "Английский"))
question_list.append(Question("Какой национальности не существует?", "Смурфы", "Ненцы", "Немцы", "Нанайцы"))
question_list.append(Question("Какой сегодня день недели?", "Пятница", "Вторник", "Воскресенье", "Понедельник"))
question_list.append(Question("Какой язык программирования мы изучаем?", "Python", "C++", "C", "Pascal"))
question_list.append(Question("Столица России?", "Москва",'Париж', "Нью-Йорк", "Санкт-Петербург"))
question_list.append(Question("Сколько лет Путину?", '69', '79', "65", "50"))
question_list.append(Question("В каком году Рим пал?", "476", "500", "460", "350"))
question_list.append(Question("Сколько лет Маинкрафту?", "10", "15", "8", "9"))
question_list.append(Question("Какого цвета в флаге России нет?", "зеленый", "синий", "красный", "белый"))
question_list.append(Question("Сколько лет Джо Байдену?", "79", "80", "75", "76ыыыыыыыыыыыыыыыыыыыыыыыыыыЫЫЫЫЫ"))
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.resize(400, 400)
main_win.setWindowTitle('Memory Card')
 
#вопрос и кнопка ответа
lbl_question = QLabel("Очень сложный вопрос")
btn_answer = QPushButton("Ответить")
 
#создаем форму вопроса
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант1')
rbtn_2 = QRadioButton('Вариант2')
rbtn_3 = QRadioButton('Вариант3')
rbtn_4 = QRadioButton('Вариант4')
 
#сразу соединяем радиокнопки в одну группу
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
# размещаем радиокнопки в группе вопроса
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1, alignment=Qt.AlignCenter) 
layout_ans2.addWidget(rbtn_2, alignment=Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment=Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment=Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
# группу вопроса сразу показать
RadioGroupBox.show()
 
#группа с ответом
AnsGroupBox = QGroupBox("Результат теста")
lbl_ans1 = QLabel("Правильно/Неправильно")
lbl_ans2 = QLabel("Правильный ответ будет тут")
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lbl_ans1)
layout_ans4.addWidget(lbl_ans2)
AnsGroupBox.setLayout(layout_ans4)
#группу ответа поначалу спрячем
AnsGroupBox.hide()
 
#заполнение основного лейаута
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
 
layoutH1.addWidget(lbl_question, alignment=Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox)
layoutH2.addWidget(AnsGroupBox)
layoutH3.addStretch(1)
layoutH3.addWidget(btn_answer, stretch=2)
layoutH3.addStretch(1)
 
layout_main.addLayout(layoutH1, stretch=2)
layout_main.addLayout(layoutH2, stretch=6)
layout_main.addLayout(layoutH3, stretch=1)
 
main_win.setLayout(layout_main)
main_win.show()
 
# начало функциональной части
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    lbl_question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_ans2.setText(q.right_answer)
 
def show_answer():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_answer.setText("Следующий вопрос")
 
def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_answer.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
def show_result(res):
    '''показать результат - установим переданный текст в надпись "результат" и покажем панель ответов'''
    lbl_ans1.setText(res)
    print('Рейтинг:', main_win.score/main_win.total*100, '%')
    show_answer()
 
def check_answer():
    '''проверить вариант ответа и показать панель ответов'''
    if answers[0].isChecked():
        show_result("Правильно")
        main_win.score += 1
    else:
        show_result("Неправильно")
 
def click_OK():
    if btn_answer.text() == "Следующий вопрос":
        next_question()
    else:
        check_answer()
 
def next_question():
    main_win.total += 1
    main_win.current += 1
    current = randint(0, len(question_list) - 1)
    # if main_win.current >= len(question_list):
        # main_win.current = 0
    ask(question_list[current])
    show_question()
 
main_win.current = -1
main_win.total =  0
main_win.score = 0
next_question()
# ask(question_list[main_win.current])
 
btn_answer.clicked.connect(click_OK)
 
app.exec_()