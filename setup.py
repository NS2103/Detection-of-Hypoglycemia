from setuptools import setup, find_packages

# Function to load the contents of the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name="hypoglycemia_prediction",  # Replace with your project name
    version="0.1",  # Initial version
    packages=find_packages(),  # Automatically find and include all packages in the directory

    # Metadata about the project
    description="A project to predict hypoglycemia using machine learning",
    author="Nivedita Shukla",
    author_email="nivedita.shukla21@gmail.com",
    

    # Read the list of dependencies from the requirements.txt file
    install_requires=parse_requirements('requirements.txt'),

    # Include additional files into the package (if any)
    include_package_data=True,

    # Classifiers to specify the type of project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Example license
        "Operating System :: OS Independent",
    ],

    # Python version requirement
    python_requires=">=3.6",
)
