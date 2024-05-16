This is simple project to scan NPTEL course cerificates. The source code code can be modified accordingly to scan other certificates also.<br>
**NOTE:** This code is valid only and only if the cerificate has a QR code to verify the certificate contents.
**STEPS:**

1. First convert the NPTEL Certificate from PDF format into JPG, JPEG or PNG image format. It can done by any online tool or by clicking _save_ _as_ in Acrobat Reader.
2. Load all the certificate images into a single folder.
3. Clone this repo in any folder of convinience.
4. Add the cloned git folder path to system path variable.
5. Open terminal from the certificates folder.
6. Run `pip install -r requirements.txt` to install all the required modules.
7. Run `nptel_check` in the terminal.
8. The program should execute and give you the scanned QR contents.<br>
