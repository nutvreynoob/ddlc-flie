# 00_definitions.rpy
# บังคับให้โหลด Class และ Utility สำคัญก่อนสคริปต์อื่นเสมอ

# 1. ระบบ Core Class
init -9999 python:
    import pygame

    # Class สำหรับทำ Effect AnimatedMask (ใช้ในฉาก Glitch / Act 3 / script-ch30)
    class AnimatedMask(renpy.Displayable):
        def __init__(self, child, mask, maskb, delay=0.10, frames=32, **properties):
            super(AnimatedMask, self).__init__(**properties)
            self.child = renpy.displayable(child)
            self.mask = renpy.displayable(mask)
            self.maskb = renpy.displayable(maskb)
            self.delay = delay
            self.frames = frames

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            mr = renpy.render(self.mask, width, height, st, at)
            mbr = renpy.render(self.maskb, width, height, st, at)
            
            cw, ch = cr.get_size()
            render = renpy.Render(cw, ch)
            
            # สลับเฟรมตามช่วงเวลา st (Shown Time)
            if int(st / self.delay) % 2 == 0:
                render.blit(cr, (0, 0))
                render.blit(mr, (0, 0), focus=False, main=False)
            else:
                render.blit(cr, (0, 0))
                render.blit(mbr, (0, 0), focus=False, main=False)
                
            renpy.redraw(self, self.delay)
            return render

        def visit(self):
            return [ self.child, self.mask, self.maskb ]

# 2. ป้องกัน AttributeError ตอนกด Quit/Esc ออกจากเกม
init -1000 python:
    layout.full_about = ""
    if not hasattr(layout, 'yesno_prompt'):
        def yesno_prompt(screen, message):
            return renpy.invoke_in_new_context(layout.invoke_yesno_prompt, screen, message)
        layout.yesno_prompt = yesno_prompt

# 3. นิยามเพิ่มเติมสำหรับ Effect หน้าจอ
init -999:
    image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)

# 4. ระบบ Transition
init -990 python:
    dissolve_scene_full = MultipleTransition([
        False, Dissolve(1.0),
        Solid("#000"), Pause(1.0),
        Solid("#000"), Dissolve(1.0),
        True
    ])
    dissolve_scene_half = MultipleTransition([
        False, Dissolve(0.5),
        Solid("#000"), Pause(0.5),
        Solid("#000"), Dissolve(0.5),
        True
    ])

# 5. ระบบเพลง
init -980 python in audio:
    t1 = "bgm/1.ogg"
    t2 = "bgm/2.ogg"
    t3 = "bgm/3.ogg"
    t4 = "bgm/4.ogg"
    t5 = "bgm/5.ogg"

# 6. ฟังก์ชันจัดการไฟล์ตัวละคร .chr
init -970 python:
    import os
    def restore_character(name):
        try:
            with open(config.gamedir + "/../characters/" + name + ".chr", "w") as f:
                f.write("Restore")
        except:
            pass

    def restore_all_characters():
        restore_character("sayori")
        restore_character("natsuki")
        restore_character("yuri")
        restore_character("monika")

# 7. ระบบตัวละครหลัก
init -960 python:
    s = DynamicCharacter("s_name", image='sayori', what_prefix='"', what_suffix='"', ctb_page='sayori')
    m = DynamicCharacter("m_name", image='monika', what_prefix='"', what_suffix='"', ctb_page='monika')
    n = DynamicCharacter("n_name", image='natsuki', what_prefix='"', what_suffix='"', ctb_page='natsuki')
    y = DynamicCharacter("y_name", image='yuri', what_prefix='"', what_suffix='"', ctb_page='yuri')
    mc = DynamicCharacter("player", what_prefix='"', what_suffix='"')

    s_name = "Sayori"
    m_name = "Monika"
    n_name = "Natsuki"
    y_name = "Yuri"

# 8. ผูก Path รูปภาพพื้นหลัง
image bg residential_day = "images/bg/residential.png"
image bg house = "images/bg/house.png"
image bg class = "images/bg/class.png"
image bg club_day = "images/bg/club.png"