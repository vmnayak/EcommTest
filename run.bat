call C:\SeleniumPython\nopCommerce\venv\Scripts\activate.bat
call pytest -n=10 -m "sanity" --html=./Reports/MarkerReport.html testCases/ --browser chrome
call pause
