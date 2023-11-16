import time
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

    def __le__(self, other):
        return self.ram <= other.ram and \
               self.cpu_cores <= other.cpu_cores and \
               self.gpu_count <= other.gpu_count


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

    def add_task(self, task: Task):
        """
        Time complexity - O(logn)
        As AVLTree does not allow to store multiple task with identical keys
        We will store with keys like {priority}_{index}
        Where index will be equal to current timestamp
        This will allow us to process tasks in FIFO order
        """
        priority = task.priority
        next_task_key = f'{priority}_{time.time()}'
        self.priority_tree.update({next_task_key: task})

    def get_task(self, available_resources: Resources) -> Union[Task, None]:
        """
        Time complexity for extracting task - O(logn)
        We go through all tasks in sorted order
        as AVLTree is BST
        """
        for task_key, current_task in self.priority_tree.items():
            if current_task.resources <= available_resources:
                self.priority_tree.pop(task_key)
                return current_task
        return None
      