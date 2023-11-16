import heapq
from typing import Union
from collections import defaultdict
from dataclasses import dataclass

from bintrees import AVLTree


@dataclass
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int


@dataclass
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str


class TaskQueue:
    def __init__(self):
        self.priority_tree = AVLTree()
        self.empty_nodes = defaultdict(list)
        self.num_tasks = defaultdict(int)

    def _task_satisfies_available_resources(self, task_resources: Resources, available_resources: Resources) -> bool:
        if task_resources.ram <= available_resources.ram and \
           task_resources.cpu_cores <= available_resources.cpu_cores and \
           task_resources.gpu_count <= available_resources.gpu_count:
            return True
        return False

    def add_task(self, task: Task):
        """
        Time complexity - O(logn)
        """
        priority = task.priority
        if len(self.empty_nodes[priority]) > 0:
            next_task_key = self.empty_nodes[priority][0]
            heapq.heappop(self.empty_nodes[priority])
        else:
            next_task_key = str(priority) + '_' + str(self.num_tasks[priority] + 1)
            self.num_tasks[priority] += 1
        self.priority_tree.update({next_task_key: task})

    def get_task(self, available_resources: Resources) -> Union[Task, None]:
        """
        Time complexity - O(logn)
        """
        for task_key, current_task in self.priority_tree.items():
            if self._task_satisfies_available_resources(current_task.resources, available_resources):
                priority = int(task_key.split('_')[0])
                self.priority_tree.pop(task_key)
                heapq.heappush(self.empty_nodes[priority], task_key)
                return current_task
        return None







            