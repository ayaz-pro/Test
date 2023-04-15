import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    import AJX
    AJX.run()
elif "64" in a:
    import AJX64
    OP64.run()
