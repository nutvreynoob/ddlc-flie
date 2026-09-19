# 🎀 Doki Doki Literature Club! Mod Workspace (`ddlc-flie`)

Welcome to the **Doki Doki Literature Club! (DDLC)** mod development repository! This repository contains a fully decompiled, functional, and ready-to-build modding environment built on **Ren'Py 6.99.12.4**.

---

## 📌 Features & Configurations

* **Decompiled Source Files:** Includes decompiled `.rpy` scripts for Chapter 0, custom definitions, screens, and GUI layouts.
* **Pre-configured Definitions (`00_definitions.rpy`):**
  * Handled `AnimatedMask` displayable classes for glitch/special visual effects.
  * Native DDLC transitions (`dissolve_scene_full`, `dissolve_scene_half`).
  * Registered audio mappings under the `audio` namespace (`bgm/`).
  * Pre-defined character declarations (`s`, `m`, `n`, `y`, `mc`) and `.chr` file restoration functions.
  * Positional character transforms (`t11`, `t21`, `t22`, `t31`, `t32`, `t33`).
* **GUI Compatibility:** Preserved original DDLC pink polka-dot GUI assets and resolved Ren'Py `Layout` / `yesno_prompt` exception errors.

---

## 🛠️ Requirements & Setup

### Prerequisites
* **Ren'Py SDK:** Version `6.99.12.4`(https://www.renpy.org/release/6.99.12) (Recommended for original DDLC mod compatibility). 
* **Git:** For version control.

### Installation & Launch

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/nutvreynoob/ddlc-flie.git](https://github.com/nutvreynoob/ddlc-flie.git)
