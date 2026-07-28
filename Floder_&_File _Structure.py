import os

structure = {
    "00_Setup_and_Environment": [
        "01_install_python.md", "02_setup_vscode.md", "03_virtualenv_setup.md",
        "04_git_and_github.md", "05_pip_and_packages.py", "06_conda_setup.md", "07_hello_world.py"
    ],
    "01_Basics": [
        "01_syntax.py", "02_comments_docstrings.py", "03_variables.py", "04_datatypes.py",
        "05_typecasting.py", "06_input_output.py", "07_operators.py",
        "08_conditionals.py", "09_loops.py", "10_functions_basics.py", "11_practice_basics.py"
    ],
    "02_Data_Structures": [
        "01_strings.py", "02_lists.py", "03_tuples.py", "04_sets.py", "05_dictionaries.py",
        "06_nested_ds.py", "07_list_comprehension.py", "08_dict_comprehension.py",
        "09_matrix_examples.py", "10_practice_ds.py"
    ],
    "03_Core_Concepts": [
        "01_functions_advanced.py", "02_lambda_functions.py", "03_map_filter_reduce.py",
        "04_recursion.py", "05_scope_variables.py", "06_modules_import.py",
        "07_builtin_functions.py", "08_packages.py", "09_datetime.py", "10_practice_core.py"
    ],
    "04_OOP": [
        "01_classes_objects.py", "02_attributes_methods.py", "03_constructors.py",
        "04_inheritance.py", "05_polymorphism.py", "06_encapsulation.py", "07_abstraction.py",
        "08_magic_methods.py", "09_class_static_methods.py", "10_practice_oop.py"
    ],
    "05_Error_Handling": [
        "01_exceptions.py", "02_try_except_finally.py", "03_raise_custom_errors.py",
        "04_assertions.py", "05_logging_basics.py", "06_practice_errors.py"
    ],
    "06_File_Handling": [
        "01_text_files.py", "02_csv_files.py", "03_json_files.py", "04_pickle_files.py",
        "05_xml_files.py", "06_context_manager.py", "07_practice_files.py"
    ],
    "07_Advanced_Python": [
        "01_iterators.py", "02_generators.py", "03_decorators.py", "04_closures.py", "05_regex.py",
        "06_multithreading.py", "07_multiprocessing.py", "08_async_await.py",
        "09_memory_management.py", "10_practice_advanced.py"
    ],
    "08_Modules_and_Libraries": [
        "math_module.py", "random_module.py", "statistics_module.py", "os_module.py", "sys_module.py",
        "shutil_module.py", "collections_module.py", "itertools_module.py", "functools_module.py", "pathlib_module.py"
    ],
    "09_Data_Science_Prep": [
        "numpy_basics.py", "pandas_basics.py", "matplotlib_intro.py", "seaborn_intro.py",
        "simple_statistics.py", "probability_basics.py", "hypothesis_testing.py",
        "data_cleaning.py", "exploratory_analysis.py", "mini_data_project.py"
    ],
    "10_Web_and_Automation": [
        "flask_basics.py", "django_intro.md", "fastapi_intro.py", "requests_module.py",
        "bs4_webscraping.py", "selenium_intro.py", "playwright_intro.py",
        "automation_examples.py", "rest_api_examples.py"
    ],
    "11_Machine_Learning_Basics": [
        "sklearn_intro.py", "regression_model.py", "classification_model.py",
        "clustering_model.py", "model_evaluation.py", "ml_practice.py"
    ],
    "12_Projects/beginner": [
        "calculator.py", "number_guess.py", "todo_list.py", "rock_paper_scissors.py", "password_generator.py"
    ],
    "12_Projects/intermediate": [
        "student_management.py", "weather_app_api.py", "expense_tracker.py", "quiz_app.py", "blog_cms.py"
    ],
    "12_Projects/advanced": [
        "ecommerce_store.py", "chat_app.py", "face_recognition_app.py", "sentiment_analysis.py", "recommendation_system.py"
    ],
    "13_Interview_Prep": [
        "01_python_theory_questions.md", "02_coding_patterns.py", "03_oop_questions.py",
        "04_ds_algorithms.py", "05_sql_with_python.py", "06_system_design_basics.md", "07_mock_interview_questions.md"
    ]
}

# Create folders and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file}\n")

print("✅ Folder & file structure created successfully!")
