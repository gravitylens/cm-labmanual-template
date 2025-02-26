## Using Skytap
Before beginning the exercises, here are a few tips to help you navigate the labs more effectively.  Understanding these can make for a much more enjoyable lab experience.

When you arrive in the lab environment, the machines will have already booted in the correct order to ensure service dependencies are met.  You may notice some machines are not already running, these are rarely-used, resource-intensive machines.  The guide will instruct you to start them when they are needed.
 
::: pagebreak :::

### Connecting to a Virtual Machine
Click on the large monitor icon to connect to a virtual machine with the HTML 5 client.  This will provide a **console** connection to the virtual machine.

![Large Monitor Icon](images/Skytap-Console-Connect.png)  

::: pagebreak :::

### Using the Guide on Small Screens
The default appearance of this lab manual will be as a panel to the right of the virtual machine.  This works great on larger screens allowing you to have the lab and instructions side-by-side.  However, this can be difficult to use on screens that do not have enough space to display everything at once.  There are several features to help you deal with this problem.

#### Resize the Guide
You can shrink the size of the right panel to allow more space for the virtual machine.

![Grow or Shrink the Guide](images/Skytap-Resize-Guide.png)  

If images are too small as a result. Click on the image to see it full screen.


[\\]: #TODO: Improve this screenshot with arrows.

#### Pop out the Guide
**Popout** the Guide to move it another browser tab or even another device.

![Skytap Popout](images/Skytap-Popout.png)

Then you can collapse the lab manual panel and leave all available screen space for the virtual machine.

::: pagebreak ::: 

### Copy and Paste
You can copy/paste between a virtual machine and your local machine.  Skytap will attempt to do this whenever you use `ctrl-v` or `ctrl-c` in a virtual machine.  This can be unreliable as it may have trouble syncing with your local clipboard.  For better results use the clipboard button on the Skytap Toolbar to manipulate the contents of the virtual machine's clipboard directly.  Using `right-click` to copy and paste inside the virtual machine will only attempt to use the VM clipboard for more reliable results.

![Clipboard Button](images/Skytap-Clipboard.png)

There are also instances of ^^copyable text^^ throughout the guide.  Whenever you click on one of these ^^copyable texts^^, you can paste that value into the VM with `right-click` or `ctrl-v`.  Be patient, as it usually takes a second or two to work.

::: pagebreak ::: 

### Tips for Maximum Productivity
Use the Skytap Toolbar on each virtual machine to maximize your ability to efficiently interact with that machine.

#### Fullscreen
The fullscreen icon will resize your virtual screen to adapt to your computer's screen settings to avoid scrolling.  Putting your browser in fullscreen mode also creates more screen space for virtual machine and minimizes distractions.

![Fullscreen Button](images/Skytap-Resize.png)

#### Bandwidth Settings
You may need to adjust your bandwidth setting on slower connections.  This will reduce the image quality of the connection to conserve bandwidth

![Bandwidth Button](images/Skytap-Bandwidth.png)

Skytap recommends at least 1.2 Mbps bandwidth per VM console session running.  However, latency is usually biggest cause of poor performance.

#### CTRL-ALT-DEL
Use the Ctrl-Alt-Del button on the tool bar to send a `Ctrl-Alt-Del` to the virtual machine.

![Ctrl-Alt-Del Button](images/Skytap-C-A-D.png)  

#### Using VPNs
Connecting to Skytap while connected to a VPN can cause additional network latency.  It can also fool the GeoIP locator system in Skytap into provisioning your lab in a region that is not ideal for your location, which could cause even more serious latency issues.  Try avoiding VPN connections to improve the responsiveness of virtual machines.

::: pagebreak :::

### Global Users
By default, the lab machines are configured to use a US English keyboard layout.  If you use a machine with a different keyboard layout, you may experience odd behavior from your lab machines.  The solution is to install the keyboard layout for your keyboard on your lab machines.  Follow the process below to find and configure the correct keyboard layout for your keyboard.

From the Start Menu, go to Settings > Time & Language > Language > Add a language.

![Windows Add Language](images/Windows-Add-Language.png)  

Select your language.  Click Next.  You can uncheck the options for voice and handwriting and then click Install.

![Windows Select Language](images/Windows-Select-Language.png)  

info>Note: If you use an alternate keyboard layout (e.g., AZERTY, Dvorak), you can click the options next to your language to install that.  Otherwise, close the Language window.

In the system tray, click ENG, then choose your keyboard layout.  You may switch back and forth between keyboard layouts.  Your instructor may need to switch back to ENG to help you with exercises, so please do not uninstall any language options.

![Windows Switch Language](images/Windows-Switch-Language.png)  
 
::: pagebreak :::
