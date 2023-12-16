# Создаем структуру модуля в баше
mkdir my_module
cd my_module
touch __init__.py __manifest__.py

# Добавляем директории и файлы
mkdir controllers models views static security data tests
touch controllers/__init__.py controllers/main_controller.py controllers/other_controller.py
touch models/__init__.py models/my_model.py models/another_model.py
touch views/my_model_views.xml views/other_model_views.xml
mkdir static/description static/src
touch security/ir.model.access.csv security/my_module_security.xml
touch data/my_module_data.xml
touch tests/__init__.py tests/test_my_module.py
