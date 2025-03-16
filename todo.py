


def display_menu(menu):
    print('Todo List Menu: ')

    for count, element in enumerate(menu, start=1):
        print(f'{count}. {element}')

def view_tasks(tasks):
    if len(tasks) == 0:
        print('No task created yet.')
    else:
        for count, value in enumerate(tasks, start=1):
            print(f'{count}. {value}')

    print()


def get_user_input(menu):
    try:
        user_input = int(input('Enter your choice: '))
        if user_input < 1 or user_input > len(menu):
         raise
        return user_input
    except:
        print('Invalid input')


def create_task(tasks):
    try:
        created_task = input('Enter a new task ')
        if created_task.isspace() or len(created_task) == 0:
            raise ValueError
        return tasks.append(created_task)
    except ValueError:
        print('Invalid Input')
    print(' ')

    return tasks

def remove_task(tasks):

    view_tasks(tasks)
    while True:
        try:
                if len(tasks) == 0:
                    print('There is no task available')

                else:
                    task_number = int(input('Enter the task number: '))
                    if task_number < 1 or task_number > len(tasks):
                        raise  ValueError
                    
                    tasks.pop(task_number-1)
                    break
        except ValueError:
                print('Invalid number input')
    
    return tasks


def main():

    menu = [
    'View Tasks',
    'Add a task',
    'Remove a Task',
    'Exit'
]
    tasks = []

    
    while True:
        display_menu(menu)
        user_choice = get_user_input(menu)

        match user_choice:
            case 1:
                view_tasks(tasks)

            case 2: create_task(tasks)
            case 3: remove_task(tasks)
            case 4: break


if __name__== '__main__':
    main()
