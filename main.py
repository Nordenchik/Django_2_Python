import django_setup as django_setup

from school_app.models import *

print("Виберіть дію:")
print("1. Створити квіз")
print("2. Створити питання")
print("3. Створити варіант відповіді")
print("4. Переглянути всі квізи")
print("5. Переглянути всі питання для квізу")
print("6. Оновити квіз")
print("7. Видалити квіз")

choice = int(input("Введіть номер дії: "))

if choice == 1:
    title = input("Введіть назву квізу: ")
    description = input("Введіть опис квізу: ")
    quiz = Quiz.objects.create(title=title, description=description)
    print(f"Створено квіз: {quiz}")

elif choice == 2:
    quiz_id = input("Введіть ID квізу: ")
    content = input("Введіть текст питання: ")
    quiz = Quiz.objects.get(id = quiz_id)
    question = Question.objects.create(quiz=quiz, content=content)
    print(f"Створено питання: {question}")

elif choice == 3:
    question_id = input("Введіть ID питання: ")
    content = input("Введіть варіант відповіді: ")
    is_correct = input("Правильна відповідь? (так/ні): ").lower() == 'так'
    question = Question.objects.get(id = question_id)
    option = Option.objects.create(question=question, content=content, is_correct=is_correct)
    print(f"Створено варіант відповіді: {option}")

elif choice == 4:
    quizzes = Quiz.objects.all()
    for quiz in quizzes: print(f"ID: {quiz.id}, Назва: {quiz.title}, Опис: {quiz.description}")

elif choice == 5:
    quiz_id = input("Введіть ID квізу: ")
    quiz = Quiz.objects.get(id = quiz_id)
    questions = quiz.questions.all()
    for question in questions: print(f"ID: {question.id}, Питання: {question.content}")

elif choice == 6:
    quiz_id = input("Введіть ID квізу для оновлення: ")
    quiz = Quiz.objects.get(id = quiz_id)
    title = input(f"Нова назва ({quiz.title}): ") or quiz.title
    description = input(f"Новий опис ({quiz.description}): ") or quiz.description
    quiz.title = title
    quiz.description = description
    quiz.save()
    print(f"Оновлено квіз: {quiz}")

elif choice == 7:
    quiz_id = input("Введіть ID квізу для видалення: ")
    quiz = Quiz.objects.get(id = quiz_id)
    quiz.delete()
    print("Квіз видалено")

else: print("Невірний вибір")