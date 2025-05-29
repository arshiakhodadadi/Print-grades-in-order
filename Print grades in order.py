try:

  list_student = {}
  score_list = []
  def student(number):
    for _ in range(number):
      name = input("Enter your student's name :")
      list_student[name] = 0

  def run():
    number = int(input('Enter your number of students :'))
    student(number=number)

  run()
  print('List of students :',list_student)

  def enter_grades():
    for name,score in list_student.items():
      try:
        score = float(input('Enter student grades :'))
      except:
        print('Make sure you entered the score correctly as a number')
        break
      if score <= 20 and score >= 0:
        list_student[name] = score
      else :
        print('Please give your score between 0 and 20')
        continue
  
  enter_grades()

  def Order_of_grades():
    key_fond = None
    for i in range(21):
      for name,score in list_student.items():
        if score == i :
          key_fond = name
          score_list.append(key_fond)
    for i in score_list[::-1]:
      print(f'{i} :',list_student[i])  

  Order_of_grades()

finally:
  print('End of program')