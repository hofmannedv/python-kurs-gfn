# Ausnahmebehandlung

werte = [1,2,3]
while True:
    try:
        v = werte.pop()
        durchschnitt = sum(werte) / len(werte)
        print(werte)
    except IndexError:
        print("fehlerhafter Zugriff auf die Liste")
    except NameError:
        print("Variable nicht definiert")
    except ZeroDivisionError:
        # print("Division durch Null")
        print("Liste abgearbeitet")
        break
    else:
        print("Fertig.")
    finally:
        print("das wird immer ausgeführt.")

