# -*- coding: utf-8 -*-
"""
主题管理模块 - 支持明暗主题切换
包含共享的样式定义，供其他模块导入使用
"""

# ============ 共享对话框样式 ============

# 浅色主题对话框样式
LIGHT_DIALOG_STYLE = """
    QDialog {
        background: #FFFFFF;
        font-family: 'Microsoft YaHei UI', sans-serif;
    }
"""

LIGHT_INPUT_STYLE = """
    QLineEdit {
        padding: 8px 12px;
        border: 1px solid #B8D4E8;
        border-radius: 6px;
        background: #FFFFFF;
        font-size: 13px;
        color: #1A1A1A;
    }
    QLineEdit:focus {
        border: 2px solid #0078D4;
    }
"""

LIGHT_BTN_CANCEL_STYLE = """
    QPushButton {
        background: #FFFFFF; color: #1A1A1A; border: 1px solid #C0C0C0;
        border-radius: 6px; font-size: 13px;
    }
    QPushButton:hover { background: #F0F0F0; }
"""

LIGHT_BTN_OK_STYLE = """
    QPushButton {
        background: #0078D4; color: white; border: none;
        border-radius: 6px; font-size: 13px;
    }
    QPushButton:hover { background: #1084D9; }
"""

LIGHT_MENU_STYLE = """
    QMenu {
        background: #FFFFFF;
        border: none;
        border-radius: 12px;
        padding: 8px 4px;
    }
    QMenu::item {
        padding: 10px 40px 10px 16px;
        color: #333333;
        border-radius: 6px;
        font-size: 13px;
        margin: 2px 6px;
    }
    QMenu::item:selected {
        background: #F0F0F0;
        color: #333333;
    }
    QMenu::item:disabled {
        color: #AAAAAA;
    }
    QMenu::separator {
        height: 1px;
        background: #EEEEEE;
        margin: 6px 16px;
    }
"""

# 深色主题对话框样式
DARK_DIALOG_STYLE = """
    QDialog {
        background: #161b22;
        font-family: 'Microsoft YaHei UI', sans-serif;
    }
"""

DARK_INPUT_STYLE = """
    QLineEdit {
        padding: 8px 12px;
        border: 1px solid #30363d;
        border-radius: 6px;
        background: #0d1117;
        font-size: 13px;
        color: #c9d1d9;
    }
    QLineEdit:focus {
        border: 2px solid #58a6ff;
    }
"""

DARK_BTN_CANCEL_STYLE = """
    QPushButton {
        background: #21262d; color: #c9d1d9; border: 1px solid #30363d;
        border-radius: 6px; font-size: 13px;
    }
    QPushButton:hover { background: #30363d; }
"""

DARK_BTN_OK_STYLE = """
    QPushButton {
        background: #238636; color: white; border: none;
        border-radius: 6px; font-size: 13px;
    }
    QPushButton:hover { background: #2ea043; }
"""

DARK_MENU_STYLE = """
    QMenu {
        background: #21262d;
        border: none;
        border-radius: 12px;
        padding: 8px 4px;
    }
    QMenu::item {
        padding: 10px 40px 10px 16px;
        color: #c9d1d9;
        border-radius: 6px;
        font-size: 13px;
        margin: 2px 6px;
    }
    QMenu::item:selected {
        background: #30363d;
        color: #FFFFFF;
    }
    QMenu::item:disabled {
        color: #6e7681;
    }
    QMenu::separator {
        height: 1px;
        background: #30363d;
        margin: 6px 16px;
    }
"""

# ============ 主题配置 ============

# 浅色主题样式 - 纯净白色简约风格
LIGHT_THEME = {
    'name': 'light',
    'main_window': """
        QMainWindow { 
            background: #F5F5F7;
        }
    """,
    'content_area': """
        background: #F5F5F7;
        border-top-left-radius: 16px;
    """,
    'sidebar': """
        background: #FFFFFF;
        border-right: 1px solid #E5E5E5;
    """,
    'card': """
        QFrame {
            background-color: #FFFFFF;
            border: 1px solid #E5E5E5;
            border-radius: 12px;
        }
    """,
    'table': """
        QTableWidget {
            background-color: #FFFFFF;
            border: none;
            border-radius: 12px;
            gridline-color: transparent;
            outline: none;
            padding: 0px;
        }
        QTableWidget::item {
            padding: 12px 16px;
            border-bottom: 1px solid #F0F0F0;
            color: #1D1D1F;
            outline: none;
        }
        QTableWidget::indicator {
            width: 16px;
            height: 16px;
            margin-left: 2px;
        }
        QTableWidget::indicator:unchecked {
            border: 2px solid #C0C0C0;
            border-radius: 3px;
            background: #FFFFFF;
        }
        QTableWidget::indicator:unchecked:hover {
            border-color: #0078D4;
        }
        QTableWidget::indicator:checked {
            background: #0078D4;
            border: 2px solid #0078D4;
            border-radius: 3px;
            image: url(ui/check_light.svg);
        }
        QTableWidget::item:selected {
            background-color: #F5F5F7;
            color: #1D1D1F;
        }
        QTableWidget::item:hover:!selected {
            background-color: #FAFAFA;
        }
        QHeaderView::section {
            background: #FFFFFF;
            padding: 14px 16px;
            border: none;
            border-bottom: 1px solid #E5E5E5;
            font-weight: 500;
            font-size: 12px;
            color: #86868B;
            text-transform: none;
            letter-spacing: 0px;
        }
        QScrollBar:vertical {
            background: transparent;
            width: 6px;
            margin: 4px 2px;
        }
        QScrollBar::handle:vertical {
            background: #C7C7CC;
            border-radius: 3px;
            min-height: 30px;
        }
        QScrollBar::handle:vertical:hover {
            background: #8E8E93;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
    """,
    'badge_success': """
        QLabel {
            background-color: #E8F5E9;
            color: #2E7D32;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 12px;
            font-weight: 500;
        }
    """,
    'badge_error': """
        QLabel {
            background-color: #FFEBEE;
            color: #C62828;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 12px;
            font-weight: 500;
        }
    """,
    'badge_warning': """
        QLabel {
            background-color: #FFF8E1;
            color: #F57F17;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 12px;
            font-weight: 500;
        }
    """,
    'badge_info': """
        QLabel {
            background-color: #E3F2FD;
            color: #1565C0;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 12px;
            font-weight: 500;
        }
    """,
    'input': """
        QLineEdit {
            padding: 10px 16px;
            border: 1px solid #D1D1D6;
            border-radius: 8px;
            background: #FFFFFF;
            color: #1D1D1F;
            font-size: 14px;
        }
        QLineEdit:hover {
            background: #F5F5F7;
            border-color: #C7C7CC;
        }
        QLineEdit:focus {
            background: #FFFFFF;
            border-color: #0078D4;
        }
        QLineEdit::placeholder {
            color: #8E8E93;
        }
    """,
    'combo': """
        QComboBox {
            padding: 10px 14px;
            padding-right: 30px;
            border: 1px solid #D1D1D6;
            border-radius: 8px;
            background: #FFFFFF;
            color: #1D1D1F;
            font-size: 14px;
        }
        QComboBox:hover {
            background: #F5F5F7;
            border-color: #C7C7CC;
        }
        QComboBox:focus {
            border-color: #0078D4;
            background: #FFFFFF;
        }
        QComboBox::drop-down { 
            border: none; 
            width: 28px;
            subcontrol-position: center right;
            subcontrol-origin: padding;
            right: 8px;
        }
        QComboBox::down-arrow { 
            image: none; 
            border-left: 4px solid transparent;
            border-right: 4px solid transparent; 
            border-top: 5px solid #86868B; 
        }
        QComboBox QAbstractItemView {
            background: #FFFFFF;
            border: 1px solid #E5E5E5;
            selection-background-color: #E8F0FE;
            selection-color: #1D1D1F;
            color: #1D1D1F;
            outline: none;
            padding: 4px 0px;
        }
        QComboBox QAbstractItemView::item {
            padding: 10px 14px;
            min-height: 22px;
        }
        QComboBox QAbstractItemView::item:hover {
            background: #F0F0F5;
        }
        QComboBox QAbstractItemView::item:selected {
            background: #E8F0FE;
            color: #0078D4;
        }
    """,
    'combo_settings': """
        QComboBox {
            padding: 6px 12px;
            padding-right: 28px;
            border: 1px solid #D1D1D6;
            border-radius: 6px;
            background: #FFFFFF;
            color: #1D1D1F;
            font-size: 13px;
        }
        QComboBox:hover { border-color: #007AFF; }
        QComboBox:focus { border-color: #007AFF; }
        QComboBox::drop-down { 
            border: none; 
            width: 24px;
            subcontrol-position: center right;
            subcontrol-origin: padding;
            right: 6px;
        }
        QComboBox::down-arrow { 
            image: none; 
            border-left: 4px solid transparent;
            border-right: 4px solid transparent; 
            border-top: 5px solid #86868B; 
        }
        QComboBox QAbstractItemView {
            background: #FFFFFF;
            border: 1px solid #E5E5E5;
            border-radius: 8px;
            selection-background-color: #007AFF;
            selection-color: white;
            color: #1D1D1F;
            outline: none;
            padding: 4px;
        }
        QComboBox QAbstractItemView::item {
            padding: 8px 12px;
            border-radius: 4px;
            margin: 2px 4px;
            min-height: 20px;
        }
        QComboBox QAbstractItemView::item:hover {
            background: #F5F5F7;
        }
        QComboBox QAbstractItemView::item:selected {
            background: #007AFF;
            color: white;
        }
    """,
    'button_primary': """
        QPushButton {
            background-color: #007AFF;
            color: white;
            border: none;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 500;
        }
        QPushButton:hover { 
            background-color: #0056CC;
        }
        QPushButton:pressed { background-color: #004099; }
        QPushButton:disabled { background-color: #E5E5EA; color: #8E8E93; }
    """,
    'button_success': """
        QPushButton {
            background-color: #34C759;
            color: white;
            border: none;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 500;
        }
        QPushButton:hover { 
            background-color: #2AA147;
        }
        QPushButton:pressed { background-color: #248A3D; }
    """,
    'button_warning': """
        QPushButton {
            background-color: #FF9500;
            color: white;
            border: none;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 500;
        }
        QPushButton:hover { 
            background-color: #CC7700;
        }
        QPushButton:pressed { background-color: #995900; }
    """,
    'button_danger': """
        QPushButton {
            background-color: #FF3B30;
            color: white;
            border: none;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 500;
        }
        QPushButton:hover { 
            background-color: #CC2F26;
        }
        QPushButton:pressed { background-color: #99231D; }
    """,
    'button_default': """
        QPushButton {
            background-color: #FFFFFF;
            color: #1D1D1F;
            border: 1px solid #D1D1D6;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 400;
        }
        QPushButton:hover { 
            background-color: #F5F5F7;
            border-color: #C7C7CC;
        }
        QPushButton:pressed { background-color: #E5E5EA; }
    """,
    'button_subtle': """
        QPushButton {
            background-color: transparent;
            color: #007AFF;
            border: none;
            padding: 10px 16px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
        }
        QPushButton:hover { background-color: rgba(0,122,255,0.1); }
        QPushButton:pressed { background-color: rgba(0,122,255,0.15); }
    """,
    'colors': {
        'text': '#1D1D1F',
        'text_secondary': '#6E6E73',
        'text_muted': '#8E8E93',
        'accent': '#007AFF',
        'success': '#34C759',
        'danger': '#FF3B30',
        'warning': '#FF9500',
        'border': '#E5E5E5',
        'background': '#FFFFFF',
        'background_alt': '#F5F5F7',
        'card': '#FFFFFF',
    }
}

# 深色主题样式 - 参考现代深色UI设计
DARK_THEME = {
    'name': 'dark',
    'main_window': """
        QMainWindow { 
            background: #0d1117;
        }
    """,
    'content_area': """
        background: #0d1117;
        border-top-left-radius: 0px;
    """,
    'sidebar': """
        background: #161b22;
        border-right: 1px solid #30363d;
    """,
    'card': """
        QFrame {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
        }
    """,
    'table': """
        QTableWidget {
            background-color: #0d1117;
            border: 1px solid #30363d;
            border-radius: 12px;
            gridline-color: transparent;
            color: #c9d1d9;
            outline: none;
            padding: 4px;
        }
        QTableWidget::item {
            padding: 8px 12px;
            border-bottom: 1px solid #21262d;
            color: #c9d1d9;
            outline: none;
        }
        QTableWidget::indicator {
            width: 16px;
            height: 16px;
            margin-left: 2px;
        }
        QTableWidget::indicator:unchecked {
            border: 2px solid #484f58;
            border-radius: 3px;
            background: #21262d;
        }
        QTableWidget::indicator:unchecked:hover {
            border-color: #58a6ff;
        }
        QTableWidget::indicator:checked {
            background: #238636;
            border: 2px solid #238636;
            border-radius: 3px;
            image: url(ui/check_dark.svg);
        }
        QTableWidget::item:selected {
            background-color: #1f6feb33;
            color: #FFFFFF;
        }
        QTableWidget::item:hover:!selected {
            background-color: #161b22;
        }
        QHeaderView::section {
            background: #0d1117;
            padding: 16px 12px;
            border: none;
            border-bottom: 2px solid #30363d;
            font-weight: 600;
            font-size: 13px;
            color: #8b949e;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        QScrollBar:vertical {
            background: #0d1117;
            width: 8px;
            margin: 0px;
        }
        QScrollBar::handle:vertical {
            background: #30363d;
            border-radius: 4px;
            min-height: 40px;
        }
        QScrollBar::handle:vertical:hover {
            background: #484f58;
        }
    """,
    'badge_success': """
        QLabel {
            background-color: rgba(35, 134, 54, 0.2);
            color: #3fb950;
            border: 1px solid rgba(35, 134, 54, 0.4);
            border-radius: 10px;
            padding: 4px 8px;
            font-size: 12px;
            font-weight: 600;
        }
    """,
    'badge_error': """
        QLabel {
            background-color: rgba(218, 54, 51, 0.2);
            color: #f85149;
            border: 1px solid rgba(218, 54, 51, 0.4);
            border-radius: 10px;
            padding: 4px 8px;
            font-size: 12px;
            font-weight: 600;
        }
    """,
    'badge_warning': """
        QLabel {
            background-color: rgba(158, 106, 3, 0.2);
            color: #d29922;
            border: 1px solid rgba(158, 106, 3, 0.4);
            border-radius: 10px;
            padding: 4px 8px;
            font-size: 12px;
            font-weight: 600;
        }
    """,
    'badge_info': """
        QLabel {
            background-color: rgba(56, 139, 253, 0.15);
            color: #58a6ff;
            border: 1px solid rgba(56, 139, 253, 0.4);
            border-radius: 10px;
            padding: 4px 8px;
            font-size: 12px;
            font-weight: 600;
        }
    """,
    'input': """
        QLineEdit {
            padding: 10px 16px;
            border: 1px solid #30363d;
            border-radius: 6px;
            background: #0d1117;
            color: #c9d1d9;
        }
        QLineEdit:focus {
            border: 1px solid #58a6ff;
            background: #0d1117;
        }
        QLineEdit::placeholder {
            color: #6e7681;
        }
    """,
    'combo': """
        QComboBox {
            padding: 10px 12px;
            border: none;
            border-radius: 8px;
            background: #21262d;
            color: #c9d1d9;
        }
        QComboBox:hover { background: #30363d; }
        QComboBox:focus { background: #30363d; }
        QComboBox::drop-down { border: none; width: 24px; }
        QComboBox::down-arrow { image: none; border-left: 5px solid transparent;
            border-right: 5px solid transparent; border-top: 6px solid #8b949e; }
        QComboBox QAbstractItemView {
            background: #161b22;
            border: 1px solid #30363d;
            selection-background-color: #1f6feb33;
            selection-color: #58a6ff;
            color: #c9d1d9;
            outline: none;
            padding: 6px;
        }
        QComboBox QAbstractItemView::item {
            padding: 10px 14px;
            min-height: 22px;
        }
        QComboBox QAbstractItemView::item:hover {
            background: #21262d;
        }
        QComboBox QAbstractItemView::item:selected {
            background: #1f6feb33;
            color: #58a6ff;
        }
    """,
    'button_primary': """
        QPushButton {
            background: #238636;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
        }
        QPushButton:hover { background: #2ea043; }
        QPushButton:pressed { background: #238636; }
        QPushButton:disabled { background: #21262d; color: #484f58; }
    """,
    'button_success': """
        QPushButton {
            background: #238636;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
        }
        QPushButton:hover { background: #2ea043; }
        QPushButton:pressed { background: #238636; }
    """,
    'button_warning': """
        QPushButton {
            background: #9e6a03;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
        }
        QPushButton:hover { background: #bb8009; }
        QPushButton:pressed { background: #9e6a03; }
    """,
    'button_danger': """
        QPushButton {
            background: #da3633;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
        }
        QPushButton:hover { background: #f85149; }
        QPushButton:pressed { background: #da3633; }
    """,
    'button_default': """
        QPushButton {
            background-color: #21262d;
            color: #c9d1d9;
            border: 1px solid #30363d;
            padding: 10px 24px;
            border-radius: 6px;
            font-size: 13px;
        }
        QPushButton:hover { 
            background-color: #30363d; 
            border-color: #8b949e;
        }
        QPushButton:pressed { background-color: #161b22; }
    """,
    'button_subtle': """
        QPushButton {
            background-color: transparent;
            color: #58a6ff;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 13px;
        }
        QPushButton:hover { background-color: rgba(88,166,255,0.1); }
        QPushButton:pressed { background-color: rgba(88,166,255,0.2); }
    """,
    'colors': {
        'text': '#c9d1d9',
        'text_secondary': '#8b949e',
        'text_muted': '#6e7681',
        'accent': '#58a6ff',
        'success': '#3fb950',
        'danger': '#f85149',
        'warning': '#d29922',
        'border': '#30363d',
        'background': '#0d1117',
        'background_alt': '#161b22',
        'card': '#161b22',
    }
}


class ThemeManager:
    """主题管理器 - 负责明暗主题切换"""
    
    def __init__(self, db, main_window):
        self.db = db
        self.main_window = main_window
        self.current_theme = 'light'
        self._theme_data = LIGHT_THEME
    
    def load_theme(self):
        """从数据库加载主题设置"""
        self.current_theme = self.db.get_setting('theme', 'light')
        self._theme_data = DARK_THEME if self.current_theme == 'dark' else LIGHT_THEME
        return self._theme_data
    
    def toggle_theme(self):
        """切换主题"""
        self.current_theme = 'dark' if self.current_theme == 'light' else 'light'
        self._theme_data = DARK_THEME if self.current_theme == 'dark' else LIGHT_THEME
        self.save_theme()
        return self._theme_data
    
    def save_theme(self):
        """保存主题设置到数据库"""
        self.db.set_setting('theme', self.current_theme)
    
    def get_theme(self):
        """获取当前主题数据"""
        return self._theme_data
    
    def is_dark(self):
        """是否为深色主题"""
        return self.current_theme == 'dark'
    
    def get_color(self, color_name):
        """获取主题颜色"""
        return self._theme_data['colors'].get(color_name, '#000000')
