import os

def create_project_template():
    
    # Define the project structure
    project_structure = {
        'src': ['__init__.py', 'DataCleaning.py','DataIngestion.py','DataEvaluvation.py','ModelDev.py'],

        'data': [],

        'steps': ['__init__.py','DataCleaning_step.py','DataIngestion_step.py','DataEvaluvation_step.py',
                  'ModelDev_step.py','ModelTraining.py'],
    }

    # Create the project directory
    project_path = os.path.join(os.getcwd())
    # os.makedirs(project_path, exist_ok=True)

    # Create subdirectories and files
    for directory, files in project_structure.items():
        directory_path = os.path.join(project_path, directory)
        os.makedirs(directory_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(directory_path, file)
            open(file_path, 'a').close()

        print(f"Created {directory_path}/")

    # print(f"\nProject template '{project_name}' created successfully!")

if __name__ == "__main__":
    create_project_template()
