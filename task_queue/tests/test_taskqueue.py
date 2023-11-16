from src.task_queue import Resources, Task, TaskQueue


res1 = Resources(ram=10, cpu_cores=10, gpu_count=10)
res2 = Resources(ram=5, cpu_cores=9, gpu_count=5)
res3 = Resources(ram=2, cpu_cores=2, gpu_count=2)
res4 = Resources(ram=6, cpu_cores=6, gpu_count=6)
res5 = Resources(ram=8, cpu_cores=8, gpu_count=8)
res6 = Resources(ram=12, cpu_cores=12, gpu_count=12)


task3 = Task(id=3,
    priority=3,
    resources=res3,
    content='', result='')

task2 = Task(id=2,
    priority=2,
    resources=res2,
    content='', result='')

task1 = Task(id=3,
    priority=1,
    resources=res1,
    content='', result='')

task4 = Task(id=4,
    priority=2,
    resources=res4,
    content='', result='')

task5 = Task(id=5,
    priority=2,
    resources=res5,
    content='', result='')

task6 = Task(id=6,
    priority=2,
    resources=res6,
    content='', result='')


def test_add_task():
    tq = TaskQueue()
    tq.add_task(task3)
    tq.add_task(task2)
    tq.add_task(task1)
    tq.add_task(task4)
    tq.add_task(task5)
    assert len(tq.priority_tree) == 5


def test_get_task():
    tq = TaskQueue()
    tq.add_task(task3)
    tq.add_task(task2)
    tq.add_task(task1)
    tq.add_task(task4)
    tq.add_task(task5)
    available_resources = Resources(ram=10, cpu_cores=10, gpu_count=10)
    task = tq.get_task(available_resources)
    assert task is task1
    tq.add_task(task6)
    available_resources = Resources(ram=7, cpu_cores=7, gpu_count=7)
    task = tq.get_task(available_resources)
    assert task is task4
    available_resources = Resources(ram=8, cpu_cores=8, gpu_count=8)
    task = tq.get_task(available_resources)
    assert task is task5
    available_resources = Resources(ram=3, cpu_cores=3, gpu_count=3)
    task = tq.get_task(available_resources)
    assert task is task3
    available_resources = Resources(ram=5, cpu_cores=9, gpu_count=5)
    task = tq.get_task(available_resources)
    assert task is task2
    available_resources = Resources(ram=12, cpu_cores=12, gpu_count=12)
    task = tq.get_task(available_resources)
    assert task is task6
    





