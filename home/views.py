from django.shortcuts import render
from home.models import Code
import pyautogui, time, subprocess
from PIL import Image

# Create your views here.
def index(request): 
    if request.method == 'POST':
        testbench = request.POST.get('testbench')
        code = request.POST.get('code')
        vericode = Code(testbench=testbench, code=code)
        vericode.save()
        TB = Code.objects.all()[0].testbench
        CODE = Code.objects.all()[0].code
        
        #   CREATING A VERILOG CODE AND SAVING AS TEXT
        file = open("C://Users//DELL//Dropbox//My PC (DESKTOP-CQ96EOI)//Desktop//ModelSim//verilogcode.v", "w+")
        file.write(CODE)
        file.close()

        #   OPENING MODELSIM, SKIPPING INITIAL STEPS AND MAXIMIZING IT
        subprocess.call("C://intelFPGA//20.1//modelsim_ase//win32aloem//modelsim.exe")
        time.sleep(2)
        click1 = pyautogui.locateCenterOnScreen("identifiers/jumpstart.png.png")
        pyautogui.click(click1)
        time.sleep(1)
        click2 = pyautogui.locateCenterOnScreen("identifiers/open.png.png")
        pyautogui.click(click2)
        time.sleep(1)
        click3 = pyautogui.locateCenterOnScreen("identifiers/ok.png.png")
        pyautogui.click(click3)
        time.sleep(4)
        pyautogui.keyDown('alt')
        pyautogui.press(' ')
        pyautogui.press('x')
        pyautogui.keyUp('alt')
        time.sleep(2)
        click4 = pyautogui.locateCenterOnScreen("identifiers/import.png.png")
        pyautogui.click(click4)
        time.sleep(5)
        click5 = pyautogui.locateCenterOnScreen("identifiers/file.png.png")
        pyautogui.click(click5)
        time.sleep(1)
        click6 = pyautogui.locateCenterOnScreen("identifiers/select.png.png")
        pyautogui.click(click6)
        time.sleep(1)
        click7 = pyautogui.locateCenterOnScreen("identifiers/simulate.png.png")
        pyautogui.click(click7)
        time.sleep(2)
        click8 = pyautogui.locateCenterOnScreen("identifiers/start.png.png")
        pyautogui.click(click8)
        time.sleep(2)
        click9 = pyautogui.locateCenterOnScreen("identifiers/work.png.png")
        pyautogui.click(click9)
        time.sleep(1)
        pyautogui.write("work."+TB)
        time.sleep(1)
        click10 = pyautogui.locateCenterOnScreen("identifiers/lesgo.png.png")
        pyautogui.click(click10)
        time.sleep(15)
        click11 = pyautogui.locateCenterOnScreen("identifiers/add.PNG")
        pyautogui.click(click11)
        time.sleep(2)
        click12 = pyautogui.locateCenterOnScreen("identifiers/addclick.png.png")
        pyautogui.click(click12)
        time.sleep(2)
        click13 = pyautogui.locateCenterOnScreen("identifiers/add2.png.png")
        pyautogui.click(click13)
        time.sleep(2)
        click14 = pyautogui.locateCenterOnScreen("identifiers/addwave.png.png")
        pyautogui.click(click14)
        time.sleep(1)
        click15 = pyautogui.locateCenterOnScreen("identifiers/wave.png.png")
        pyautogui.click(click15)
        time.sleep(2)
        click16 = pyautogui.locateCenterOnScreen("identifiers/runlength.png.png")
        pyautogui.click(click16)
        time.sleep(1)
        pyautogui.write('50')
        time.sleep(1)
        click17 = pyautogui.locateCenterOnScreen("identifiers/run.png.png")
        pyautogui.click(click17)
        time.sleep(1)
        click18 = pyautogui.locateCenterOnScreen("identifiers/zoom.png.png")
        pyautogui.click(click18)

        #   TAKING ITS SCREENSHOT
        i=1
        while(i<2):
            time.sleep(5)
            img = pyautogui.screenshot()
            img.save("static\simulation"+str(i)+".png")
            i=i+1
            
        # CROPPING THE IMAGE
        i=1
        while(i<2):
            image = Image.open("static\simulation"+str(i)+".png")
            area = (0, 175, img.width, 675)
            cropped_image = image.crop(area)
            time.sleep(1)
            cropped_image.save("static\simulation_cropped"+str(i)+".png")
            i=i+1

        # CLOSING MODELSIM
        time.sleep(2)
        click19 = pyautogui.locateCenterOnScreen("identifiers/close.png.png")
        pyautogui.click(click19)
        time.sleep(1)
        click20 = pyautogui.locateCenterOnScreen("identifiers/closeyes.png.png")
        pyautogui.click(click20)

    return render(request, 'index.html')
    