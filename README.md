# dino-game-dark-mode
An automated chrome dino game Using ```PIL``` and ```Pyautogui``` with dark mode support.

### How it works
All you need to know is in [this article](https://medium.com/analytics-vidhya/automate-chrome-dino-game-using-python-pyautogui-and-pil-eeb839005ccf) credits [@ayushgemini](https://github.com/ayushgemini)

### Why write another code then ?
* To add 3 features
  1. Linux support
  2. Handle dark mode 
  3. Automatic switch to chrome window 

#### Linux Support 
```ImageGrab``` is not supported in linux, its replacement is [pyscreenshot](https://pypi.org/project/pyscreenshot/) and ```pyautogui``` also has built-in [screenshot](https://pyautogui.readthedocs.io/en/latest/screenshot.html) method but both are slow and inconsistent.
[mss](https://python-mss.readthedocs.io/examples.html#pil) fixes these issues, its both fast and cross-platform.

#### Handle dark mode 
After score goes around 700 the game inverts the colour turning into dark mode and our logic breaks. 
I fixed it using random pixel on screen which is white in normal mode and turns dark in dark mode. 
Based on its colour two different functions are called. Function for dark mode is written by inversing the conditions.
The chosen pixel should never come in way of dinosaur,bird or cactus otherwise it will satisfy conditions of dark mode (prefer pixel below the ground line of game)

#### Automatic switch to chrome window
In original code first chrome tab is opened then program is runned in terminal and then focus is switched to browser window, to avoide registering key presses in terminal ```time.sleep()``` is used.
these steps are automated using [webdrivers](https://www.selenium.dev/documentation/en/) of ```selenium``` 

#### Others
* The game only uses keyboard inputs so initially I considered using [keyboard](https://pypi.org/project/keyboard/) library as its relatively small. 
but scrapped the idea later as this library needs root permissions for ubuntu and is still in beta phase.
* I also considered ```OpenCv``` but lot of online forums suggested using ```PIL``` for basic tasks as its lightweight and simple

### How to run 
+ Install ```python3.5+``` ([preferably 3.7](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)). 
+ Install [pip3](https://stackoverflow.com/questions/37954008/proper-way-to-install-pip-on-ubuntu) 
+ Download [chrome driver.](https://sites.google.com/a/chromium.org/chromedriver/downloads) 
+ Install [chrome driver.](https://christopher.su/2015/selenium-chromedriver-ubuntu/
) (for ubuntu)
+ Run ``` pip3 install -r requirement.txt ```
+ Run ``` python3 dino.py ```

### Why did I not fork and contribute in original code ?
+ #### Pixel values 
  pixel values for each screen may differ based on its resolution. so I would have to change pixel values in original code to make it work on my pc but then the code would not work on original authors pc.

+ Being beginner, I prefer doing everything from scratch, it helps me better understand the concepts

### Helpful notes
+ pixel cordinates start at (0,0) from top left corner of the screen, x coordinates increase towards right, y coordinates increase towards bottom 
+ wrong version of chromedriver gives
  ``` ChromeDriver error “unknown error: cannot get automation extension”```
  if this error occures update chromedriver(preffered) or downgrade chrome browser
