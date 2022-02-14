from pynput.keyboard import Key,  Controller
from pywinauto.application import Application
import win32gui
import win32ui
import ctypes
from ctypes import wintypes
from ctypes import windll
from PIL import Image
import pyautogui
import time
import keyboard

keyboard = Controller()

############################################
############### Funções ####################
############################################

def shinykeyboard():
    #reset
    keyboard.press('a')
    keyboard.press('s')
    keyboard.press('d')
    keyboard.press('f')
    time.sleep(0.1)
    keyboard.release('a')
    keyboard.release('s')
    keyboard.release('d')
    
    #1 - tela inicial -
    time.sleep(1.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #2
    time.sleep(0.2)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.6)
    #3
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #4
    time.sleep(0.2)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(1.55)
    #5
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #1
    time.sleep(0.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.5)
    #2
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #3
    time.sleep(0.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.5)
    #4
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #5
    time.sleep(0.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.7)
    
    #11 - comprando pokemon -
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #
    time.sleep(0.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #12
    time.sleep(0.06)
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    time.sleep(0.06)
    #13
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    #14
    time.sleep(0.1)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.1)
    #
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.5)
    #15
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    #16
    time.sleep(0.07)
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    time.sleep(0.01)

    #11 - comprando pokemon -
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #
    time.sleep(0.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #12
    time.sleep(0.06)
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    time.sleep(0.06)
    #13
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    #14
    time.sleep(0.1)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.1)
    #
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.5)
    #15
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    #16
    time.sleep(0.07)
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    time.sleep(0.01)

    #11 - comprando pokemon -
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #
    time.sleep(0.5)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #12
    time.sleep(0.06)
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    time.sleep(0.06)
    #13
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    #14
    time.sleep(0.1)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.1)
    #
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.5)
    #15
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    #16
    time.sleep(0.07)
    keyboard.press('d')
    time.sleep(0.5)
    keyboard.release('d')
    time.sleep(0.01)
    
    # - checando se é shiny -
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('s')
    #
    time.sleep(0.01)
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    time.sleep(0.01)
    #5
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #6
    time.sleep(0.3)
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    time.sleep(0.3)
    #7
    keyboard.press('f')
    time.sleep(0.5)
    keyboard.release('f')
    #
    time.sleep(0.37)
    keyboard.press('k')
    time.sleep(0.5)
    keyboard.release('k')
    time.sleep(1)
    

def shinykeyboard2():
    #
    keyboard.press('k')
    time.sleep(0.1)
    keyboard.release('k')
    time.sleep(1)
    #
    

def shinykeyboard3():
    #
    keyboard.press('k')
    time.sleep(0.1)
    keyboard.release('k')
    #

def takePicture(hwnd, int):
	left, top, right, bot = win32gui.GetWindowRect(hwnd)
	w = right - left
	h = bot - top

	hwndDC = win32gui.GetWindowDC(hwnd)
	mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
	saveDC = mfcDC.CreateCompatibleDC()

	saveBitMap = win32ui.CreateBitmap()
	saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

	saveDC.SelectObject(saveBitMap)

	# Change the line below depending on whether you want the whole window
	# or just the client area.
	#result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
	result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

	bmpinfo = saveBitMap.GetInfo()
	bmpstr = saveBitMap.GetBitmapBits(True)

	im = Image.frombuffer(
	    'RGB',
	    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
	    bmpstr, 'raw', 'BGRX', 0, 1)

	win32gui.DeleteObject(saveBitMap.GetHandle())
	saveDC.DeleteDC()
	mfcDC.DeleteDC()
	win32gui.ReleaseDC(hwnd, hwndDC)

	if result == 1:
	    #PrintWindow Succeeded
		if int == 0:
			im.save('base' + str(hwnd) + '.png')
		else:
			im.save("current" + str(hwnd) + ".png")

def takePicture2(hwnd, int):
	left, top, right, bot = win32gui.GetWindowRect(hwnd)
	w = right - left
	h = bot - top

	hwndDC = win32gui.GetWindowDC(hwnd)
	mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
	saveDC = mfcDC.CreateCompatibleDC()

	saveBitMap = win32ui.CreateBitmap()
	saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

	saveDC.SelectObject(saveBitMap)

	# Change the line below depending on whether you want the whole window
	# or just the client area.
	#result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
	result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

	bmpinfo = saveBitMap.GetInfo()
	bmpstr = saveBitMap.GetBitmapBits(True)

	im = Image.frombuffer(
	    'RGB',
	    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
	    bmpstr, 'raw', 'BGRX', 0, 1)

	win32gui.DeleteObject(saveBitMap.GetHandle())
	saveDC.DeleteDC()
	mfcDC.DeleteDC()
	win32gui.ReleaseDC(hwnd, hwndDC)

	if result == 1:
	    #PrintWindow Succeeded
		if int == 0:
			im.save("current2" + str(hwnd) + ".png")

def takePicture3(hwnd, int):
	left, top, right, bot = win32gui.GetWindowRect(hwnd)
	w = right - left
	h = bot - top

	hwndDC = win32gui.GetWindowDC(hwnd)
	mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
	saveDC = mfcDC.CreateCompatibleDC()

	saveBitMap = win32ui.CreateBitmap()
	saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

	saveDC.SelectObject(saveBitMap)

	# Change the line below depending on whether you want the whole window
	# or just the client area.
	#result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
	result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

	bmpinfo = saveBitMap.GetInfo()
	bmpstr = saveBitMap.GetBitmapBits(True)

	im = Image.frombuffer(
	    'RGB',
	    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
	    bmpstr, 'raw', 'BGRX', 0, 1)

	win32gui.DeleteObject(saveBitMap.GetHandle())
	saveDC.DeleteDC()
	mfcDC.DeleteDC()
	win32gui.ReleaseDC(hwnd, hwndDC)

	if result == 1:
	    #PrintWindow Succeeded
		if int == 0:
			im.save("current3" + str(hwnd) + ".png")

############################################
############# PRINTADOR 2000 ###############
############################################
			
pyautogui.click()
handle = win32gui.GetForegroundWindow()
MOUSE_X, MOUSE_Y = pyautogui.position()
r = win32gui.GetWindowRect(handle);
takePicture(handle, 0)

user32 = ctypes.windll.user32
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(handle, ctypes.byref(pid))

pyautogui.click()
handle = win32gui.GetForegroundWindow()
MOUSE_X, MOUSE_Y = pyautogui.position()
r = win32gui.GetWindowRect(handle);
takePicture2(handle, 0)

user32 = ctypes.windll.user32
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(handle, ctypes.byref(pid))

pyautogui.click()
handle = win32gui.GetForegroundWindow()
MOUSE_X, MOUSE_Y = pyautogui.position()
r = win32gui.GetWindowRect(handle);
takePicture3(handle, 0)

user32 = ctypes.windll.user32
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(handle, ctypes.byref(pid))

start_time = time.time()
last_time = start_time
relative_x = MOUSE_X-r[0]
relative_y = MOUSE_Y-r[1]
im1 = Image.open('base' + str(handle) + '.png')
Normal_Color = im1.getpixel( (relative_x,relative_y) )
im1.close()
print("Base color = " + str(Normal_Color))
found_shiny = False;
c = 0
			
while (not found_shiny):
        shinykeyboard()
        takePicture(handle, 1)

        im1 = Image.open("current" + str(handle) + ".png")
        
        New_Color = im1.getpixel( (relative_x,relative_y) )
        im1.close()

        if New_Color != Normal_Color:
            found_shiny = True;
            c += 1;
            print("Pokemon shiny encontrado em ",c,"encontros, congratulations!")
            print('Duração ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
            pyautogui.alert('DRATINI SHINY GARAE!!')

        elif New_Color == Normal_Color:
                c += 1;
                print("Nada de shiny, Encontros: ",c);   
                shinykeyboard2()
                takePicture2(handle, 1)

                im2 = Image.open("current2" + str(handle) + ".png")
        
                New_Color2 = im2.getpixel( (relative_x,relative_y) )
                im2.close()

                if New_Color2 != Normal_Color:
                    found_shiny = True;
                    c += 1;
                    print("Pokemon shiny encontrado em ",c,"encontros, congratulations!")
                    print('Duração ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
                    pyautogui.alert('DRATINI SHINY GARAE!!')

                elif New_Color2 == Normal_Color:
                    c += 1;
                    print("Nada de shiny, Encontros: ",c);
                    shinykeyboard3()
                    takePicture3(handle, 1)

                    im3 = Image.open("current3" + str(handle) + ".png")
        
                    New_Color3 = im3.getpixel( (relative_x,relative_y) )
                    im3.close()

                    if New_Color3 != Normal_Color:
                        found_shiny = True;
                        c += 1;
                        print("Pokemon shiny encontrado em ",c,"encontros, congratulations!")
                        print('Duração ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
                        pyautogui.alert('DRATINI SHINY GARAE!!')

                    elif New_Color3 == Normal_Color:
                        c += 1;
                        print("Nada de shiny, Encontros: ",c)
                        time.sleep(2)

    
