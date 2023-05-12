import numpy as np
import PySimpleGUI as sg

def request_resources(process, resources_requested, available, allocation, maximum):
    need = maximum - allocation

    if (resources_requested > need[process]).any():
        return "Error: Request exceeds the maximum need.", None, None

    if (resources_requested > available).any():
        return "Error: Request exceeds the available resources.", None, None

    temp_allocation = allocation.copy()
    temp_allocation[process] += resources_requested

    safe_sequence = is_safe_state(available, temp_allocation, maximum)
    if safe_sequence is not None:
        temp_available = available - resources_requested
        return "The request can be granted.", safe_sequence, temp_available
    else:
        return "The request cannot be granted.", None, None

def is_safe_state(available, allocation, maximum):
    need = maximum - allocation
    work = available.copy()
    finish = [False] * len(allocation)
    safe_sequence = []

    while True:
        safe_process = -1
        for i in range(len(allocation)):
            if not finish[i] and (need[i] <= work).all():
                safe_process = i
                break

        if safe_process == -1:
            break

        work += allocation[safe_process]
        finish[safe_process] = True
        safe_sequence.append(safe_process)

    if all(finish):
        return safe_sequence
    else:
        return None

def main():
    sg.theme('LightGreen')

    resources_frame = [
        [sg.Text('Number of Resources'), sg.InputText(key='num_resources')],
        [sg.Text('Total Resources'), sg.InputText(key='total_resources')],
        [sg.Text('Available Resources'), sg.InputText(key='available_resources')],
    ]

    processes_frame = [
        [sg.Text('Number of Processes'), sg.InputText(key='num_processes')],
    ]

    allocation_frame = [
        [sg.Text('Current Allocation (one row per process)'), sg.Multiline(key='current_allocation')],
    ]

    maximum_frame = [
        [sg.Text('Maximum Need (one row per process)'), sg.Multiline(key='maximum_need')],
    ]

    request_frame = [
        [sg.Text('Process Requesting Resources'), sg.InputText(key='process')],
        [sg.Text('Resources Requested'), sg.InputText(key='resources_requested')],
    ]

    layout = [
        [sg.Frame('Resources', resources_frame)],
        [sg.Frame('Processes', processes_frame)],
        [sg.Frame('Current Allocation', allocation_frame)],
        [sg.Frame('Maximum Need', maximum_frame)],
        [sg.Frame('Resource Request', request_frame)],
        [sg.Button('Submit'), sg.Button('Exit')],
        [sg.Text(size=(40, 3), key='output')]
    ]

    window = sg.Window('Banker\'s Algorithm', layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Submit':
            try:
                num_resources = int(values['num_resources'])
                total_resources = np.array(list(map(int, values['total_resources'].split())))
                available_resources = np.array(list(map(int, values['available_resources'].split())))
                num_processes = int(values['num_processes'])
                current_allocation = np.array([list(map(int, row.split())) for row in values['current_allocation'].strip().split('\n')])
                maximum_need = np.array([list(map(int, row.split())) for row in values['maximum_need'].strip().split('\n')])
                process = int(values['process'])
                resources_requested = np.array(list(map(int, values['resources_requested'].split())))

                if len(total_resources) != num_resources or len(available_resources) != num_resources:
                    raise ValueError("Incorrect number of resources specified.")

                output, safe_sequence, temp_available = request_resources(process, resources_requested, available_resources, current_allocation, maximum_need)
                if safe_sequence:
                    output += f"\nSafe sequence: {', '.join(map(str, safe_sequence))}"
                window['output'].update(output)

            except Exception as e:
                window['output'].update("Error: Invalid input. Please check your input values.")

    window.close()

if __name__ == "__main__":
    main()