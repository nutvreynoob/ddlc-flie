# script.rpy

label start:
    # ตั้งค่าเริ่มต้นของ DDLC
    $ anticheat = persistent.anticheat
    $ chapter = 0
    
    # วิ่งต่อไปที่เนื้อเรื่อง Chapter 0
    call ch0_main from _call_ch0_main
    
    return