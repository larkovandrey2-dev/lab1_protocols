from src.protocol import TaskProtocol


def process_tasks(source: object):
    if not isinstance(source, TaskProtocol):
        raise TypeError("Этот объект не поддерживается платформой")
    task = source.get_tasks()
    print(f"Платофрма обработала {len(task)} задач")

