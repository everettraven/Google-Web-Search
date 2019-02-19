import webbrowser


x = input("what would you like to google search?\n")

url = "https://www.google.com/search?source=hp&ei=BdJdXOuoEaLX5gLIiYDoAg&q="+ x + "&btnK=Google+Search&oq=" + x + "&gs_l=psy-ab.3..35i39j0l5j0i131j0l3.1186311.1186882..1187255...13.0..0.341.1225.1j2j2j1......0....1..gws-wiz.....6.mbPPqJHDrD8"

webbrowser.open_new(url)