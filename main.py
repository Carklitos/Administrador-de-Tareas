import os
import time

#vars

tasks = []

def add_task():
    task = str(input('\nQué tarea deseas agregar? '))
    if task.isdigit():
        print('Error: La tarea no es una cadena de texto.')
        return main()
    else:
        tasks.append({"task": task, "completed": False})
        time.sleep(0.5)
        print('Tarea agregada correctamente.')
        return main()


def view_task():
    print('\nTu lista:')
    for index, task in enumerate(tasks):
        print(f"{index + 1}. [{ 'x' if task['completed'] else ' '}] {task['task']}")
    print('\nEscribe "0" para volver.')
    fdh = input()
    if fdh == '0':
        os.system('cls')
        return main()

def del_task():
    print('\nEscribe el número de la tarea que deseas eliminar: ')
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['task']}")
    print('\nEscribe "0" para volver.')

    task_number = int(input()) - 1
    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        print(f"\nLa tarea '{deleted_task['task']}' ha sido eliminada.")
        print('\n---------------------------------------')
        return del_task()
    elif task_number == -1:
        os.system('cls')
        return main()
    else:
        print("El número de tarea ingresado no es válido.")
        time.sleep(1)
        return del_task()
    
def complete_task():
    print('\nEscribe el número de la Tarea que deseas marcar como completada:')
    for index, task in enumerate(tasks):
        print(f"{index + 1}. [{ 'x' if task['completed'] else ' '}] {task['task']}")
    print('\nEscribe "0" para volver.')

    task_number = int(input()) - 1

    if task_number == -1:
        os.system('cls')
        return main()
    elif 0 <= task_number < len(tasks):
        if tasks[task_number]['completed']:
            tasks[task_number]['completed'] = False
            print(f"\nLa tarea '{tasks[task_number]['task']}' ha sido desmarcada como completada.")
        else:
            tasks[task_number]['completed'] = True
            print(f"\nLa tarea '{tasks[task_number]['task']}' ha sido marcada como completada.")
        print('\n---------------------------------------')
        return complete_task()
    else:
        print("El número de tarea ingresado no es válido.")
        time.sleep(1)
        return complete_task()



def main():
    print('\n--- Administrador de tareas --- ')
    print('1. Agregar Tareas')
    print('2. Ver Tareas')
    print('3. Eliminar Tarea')
    print('4. Marcar como Completada')

    ans = input()
    if ans == '1':
        os.system('cls')
        print('\033[4mAgregar Tarea\033[0m')
        add_task()
    elif ans == '2':
        os.system('cls')
        print('\033[4mVer Tareas\033[0m')
        view_task()
    elif ans == '3':
        os.system('cls')
        print('\033[4mEliminar Tareas\033[0m')
        del_task()
    elif ans == '4':
        os.system('cls')
        print('\033[4mMarcar como Completada\033[0m')
        complete_task()
    else:
        os.system('cls')
        print('No has seleccionado correctamente una de las opciones')

if __name__ == '__main__':
    main()