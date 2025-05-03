from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
import math

class HeartWidget(Widget):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.t = 0
        Clock.schedule_interval(self.update, 1/30)

    def update(self, dt):
        self.t += dt
        self.canvas.clear()
        with self.canvas:
            Color(1, 0, 0)
            points = []
            scale = 120 + 20 * math.sin(2 * math.pi * self.t)
            for angle in range(0, 360, 2):
                rad = math.radians(angle)
                x = 16 * math.sin(rad)**3
                y = 13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad)
                points.append(self.center_x + x * scale / 20)
                points.append(self.center_y + y * scale / 20)
            Line(points=points, width=3)

class HeartApp(App):
    def build(self):
        return HeartWidget()

if __name__ == '__main__':
    HeartApp().run()