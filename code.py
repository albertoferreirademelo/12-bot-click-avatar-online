import time
from win32com.client import Dispatch

Auto = Dispatch("AutoItX3.Control")
Auto.Run("calc.exe")
Auto.Run("notepad.exe")
time.sleep(1)
Auto.Send("AZERTYUIOP = ")
time.sleep(1)
titreFenetre = 'Calculatrice'
Auto.WinActivate(titreFenetre , '')
time.sleep(1)
Auto.Send("12345")
time.sleep(0.4)
Auto.Send("{+}")
time.sleep(0.4)
Auto.Send("54321")
time.sleep(0.4)
Auto.Send("{=}")
time.sleep(0.4)
Auto.Send("^c")
time.sleep(1)
Auto.WinClose(titreFenetre , '')
Auto.Send("^v")
Auto.Send("{ENTER}")