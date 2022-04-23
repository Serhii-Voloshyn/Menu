from tasks.my_tasks import task_88a, task_88b, task_322


def main():

    # Dictionary of tasks. Key - task number, value - function of that task
    tasks = {"exit": exit, "88a":task_88a, "88b":task_88b, "322":task_322}

    # Prints info
    print("Aviable tasks: ")
    [print(f"{number + 1} - {key}") for number, key in enumerate(tasks.keys())]

    # Main loop
    while True:
        try:
            # Prints results
            print(f"Result: {tasks[input('Enter task number: ')]()}")
        except KeyError:
            print("Wrong task, try again.")


if __name__ == "__main__":
    main()
