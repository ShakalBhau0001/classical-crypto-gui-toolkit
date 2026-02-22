# classical-crypto-gui-toolkit

## Project Structure

```bash
classical-crypto-gui-toolkit/
│
├── core/                        
│   ├── __init__.py
│   ├── utils.py
│   │
│   ├── ciphers/
│   │   ├── __init__.py
│   │   ├── caesar.py
│   │   ├── rail_fence.py
│   │   ├── row_column.py
│   │   └── playfair.py
│   │
│   └── attacks/
│       ├── __init__.py
│       ├── caesar_brute.py
│       └── rail_fence_brute.py
│
├── gui/
│   ├── __init__.py
│   ├── app.py
│   ├── main_window.py
│   ├── theme.py
│   ├── validators.py
│   │
│   ├── panels/
│   │   ├── __init__.py
│   │   ├── cipher_panel.py       
│   │   ├── attack_panel.py
│   │   ├── about_panel.py
│   │   │
│   │   ├── attacks/
│   │   │   ├── __init__.py
│   │   │   ├── caesar_attack_panel.py
│   │   │   └── railfence_attack_panel.py
│   │   │
│   │   └── ciphers/               
│   │       ├── __init__.py
│   │       ├── caesar_panel.py
│   │       ├── rail_fence_panel.py
│   │       ├── row_column_panel.py
│   │       └── playfair_panel.py
│   │
│   └── components/
│       ├── __init__.py
│       ├── sidebar.py
│       ├── text_area.py
│       ├── action_buttons.py
│       ├── base_attack_frame.py
│       └── base_cipher_frame.py
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```
