from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton, QButtonGroup, 
        QPushButton, QLabel)
from random import shuffle, randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = [] 
q1 = Question("Самая длинная река в мире", "Амазонка", "Конго", "Нил", "Волга")
questions_list.append(q1)           
q2 = Question("Имя Месси", "Лионель", "Криштиану", "Иван", "Златан")
questions_list.append(q2)
q3 = Question("Кто был первым призедентом в США", "Вашингтон", "Сталин", "Путин", "Обама")
questions_list.append(q3)
q4 = Question("Столица России", "Москва", "Санкт-Петербург", "Волгоград", "Владивосток")
questions_list.append(q4)
q5 = Question("Как переводится слово read", "читать", "играть", "гулять", "петь")
questions_list.append(q5)
q6 = Question("Кто выиграл золотой мяч в 2021 году", "Месси", "Роналду", "Левандовски", "Неймар")
questions_list.append(q6)
q7 = Question("Самая первая буква в английском алфавите", "A", "B", "C", "Q")
questions_list.append(q7)
q8 = Question("Имя Пушкина", "Александр", "Алексей", "Сергей", "Владимир")
questions_list.append(q8)
q9 = Question("В какой стране создали хоккей", "Канада", "Россия", "США", "Англия")
questions_list.append(q9)
q10 = Question("Самая высокая гора", "Эверест", "Эльбрус", "Альпы", "Олимп")
app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(700, 500)
 
# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_question = QLabel('В каком году основана Москва?')
 
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1247')
rbtn_2 = QRadioButton('1147')
rbtn_3 = QRadioButton('1159')
rbtn_4 = QRadioButton('1259')
 
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
 
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()  
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


    


 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
 
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно")
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')    
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно")
            print("Рейтинг:", (window.score/window.total*100), "%")     
def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)

    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question] 
    ask(q)   

        
def start_test():
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()
def show_correct(res):
    lb_result.setText(res)
    show_result()

window.setLayout(layout_card)
btn_OK.clicked.connect(start_test)
window.score = 0
window.total = 0
next_question() # проверяем, что панель ответов показывается при нажатии на кнопку

window.show()
app.exec()

