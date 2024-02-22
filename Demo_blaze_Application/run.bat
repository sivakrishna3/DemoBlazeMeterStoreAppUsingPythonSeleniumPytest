rem pytest -s -v -m "regression or sanity"  testCases/test_About_Us_Page.py
rem pytest -s -v -m "regression"  testCases/test_About_Us_Page.py
pytest -s -v --html=Reports/About_Us_Page.html testCases/test_About_Us_Page.py