from datetime import datetime

now = datetime.now()


class Item:
    created_at = now.strftime("%d.%m.%Y %H:%M:%S")
    updated_at = now.strftime("%d.%m.%Y %H:%M:%S")
    counter = 0


class Quiz(Item):
    quiz_id = Item.counter + 1
    Item.counter = quiz_id
    question_counter = 0
    question_dict = {}

    def __init__(self, title=input('quiz title: ')):
        self.title = title

    def __iter__(self):
        return self

    def __next__(self):
        text = input('your question: ')
        self.question_counter += 1
        self.question_dict[self.question_counter] = [text]
        y = input('add another question to this quiz?(y/n) ')
        if y == 'y':
            return f'question saved'
        raise StopIteration


my_quiz = Quiz()
for el in my_quiz:
    print(el)

print(f'{my_quiz.created_at}, {my_quiz.quiz_id}, {my_quiz.title}, {my_quiz.question_dict}')
