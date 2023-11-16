import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name="task-queue",
    version="1.0.0",
    author="Ivan Bolelov",
    description="Task Queue",
    install_requires=requirements,
    python_requires=">=3.6",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    # entry_points={"console_scripts": ["llm-linter=cli.main:main"]},
)