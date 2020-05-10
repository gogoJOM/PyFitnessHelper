import setuptools

with open("README.md", "r", encoding="utf8") as readme:
    description = readme.read()

with open('requirements.txt', "r", encoding="utf8") as requirements:
    requires = requirements.read().splitlines()

setuptools.setup(
    name="PyFitnessHelper",
    version="0.0.2",
    author="Artemii Zakharov, Ekaterina Safronova",
    author_email="artemy00797@yandex.ru, katyasafit@gmail.com",
    description="Helper to manage your calories intake",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gogoJOM/PyFitnessHelper",
    packages=setuptools.find_packages(),
    package_data={
        'PyFitnessPackage': ['tmp/*',
                             'locales/ru/LC_MESSAGES/*']
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    python_requires='>=3.7',
)
