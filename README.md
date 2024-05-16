This is a simple project that scans NPTEL course certificates. The source code can also be modified accordingly to scan other certificates.<br>
**NOTE:** This code is only valid if the certificate has a QR code to verify the certificate contents.<br>
<br>
**STEPS:**<br>
1. First, convert the NPTEL Certificate from PDF format into JPG, JPEG, or PNG image format. It can done by any online tool or by clicking _save_ _as_ in Acrobat Reader.
2. Load all the certificate images into a single folder.
3. Clone this repo in any folder of convenience.
4. Copy the cloned repo folder path `"PATH"` .
5. Open the terminal from the certificates folder.
6. Run `pip install -r "PATH\requirements.txt"` to install all the required modules.
7. Run `python -u "PATH\nptel_check.py"` in the terminal.
8. The program should execute and give you the scanned QR contents.<br>
