import ctypes as c, time as t
u = c.windll.user32; a = o = 0
print("Z: Start/Stop | T: Quit")
while not u.GetAsyncKeyState(84) & 32768:
    p = u.GetAsyncKeyState(90) & 32768
    if p and not o:
        a = not a; print("Autoclicker:", "ON" if a else "OFF"); t.sleep(0.2)
    o = p
    if a: u.mouse_event(2,0,0,0,0); u.mouse_event(4,0,0,0,0); t.sleep(0.01)
    else: t.sleep(0.02)
print("Exiting.")
