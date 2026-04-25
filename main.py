from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock
import time
import math

class AnalogClock(Widget):
    def update(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Background Circle
            Color(0.2, 0.2, 0.2)
            cx, cy = self.center
            radius = min(self.width, self.height) / 2 - 20
            Line(circle=(cx, cy, radius), width=2)

            # Hands logic
            t = time.localtime()
            h, m, s = t.tm_hour % 12, t.tm_min, t.tm_sec

            # Seconds (Red)
            Color(1, 0, 0)
            angle_s = math.radians(90 - s * 6)
            Line(points=[cx, cy, cx + math.cos(angle_s) * radius * 0.9, cy + math.sin(angle_s) * radius * 0.9], width=1.5)

            # Minutes (White)
            Color(1, 1, 1)
            angle_m = math.radians(90 - m * 6)
            Line(points=[cx, cy, cx + math.cos(angle_m) * radius * 0.7, cy + math.sin(angle_m) * radius * 0.7], width=2.5)

            # Hours (Cyan)
            Color(0, 1, 1)
            angle_h = math.radians(90 - (h * 30 + m * 0.5))
            Line(points=[cx, cy, cx + math.cos(angle_h) * radius * 0.5, cy + math.sin(angle_h) * radius * 0.5], width=4)

class WatchApp(App):
    def build(self):
        self.title = "Smart Watch Pro"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # UI Elements
        layout.add_widget(Label(text="MY SMART WATCH", font_size='24sp', bold=True, color=(0,1,1,1)))
        
        self.clock_widget = AnalogClock()
        layout.add_widget(self.clock_widget)
        
        Clock.schedule_interval(self.clock_widget.update, 1)
        
        btn = Button(text="PREMIUM ANALOG", size_hint=(1, 0.2), background_color=(0, 0.5, 0.5, 1))
        layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    WatchApp().run()
