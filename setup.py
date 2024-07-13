from distutils.core import setup

setup(
    name="quizMe",
    version="0.1.0",
    install_requires=["PyYAML==6.0.1"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "quizMe = quizMe.main:main",
        ]
})
