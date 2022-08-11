cmd /k "C:\SeleniumPython\nopCommerce\venv\Scripts\activate.bat" & "pytest -n=10 -m "sanity" --html=./Reports/MarkerReport.html testCases/ --browser chrome"
pause
